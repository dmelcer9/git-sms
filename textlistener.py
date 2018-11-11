from flask import Flask, request
from git import Repo
import os
import shutil

sourcepath = os.environ["GIT_REPO_PATH"]

shutil.rmtree("/tmp/smsrepo")

repo = Repo.clone_from("file://" + sourcepath, "/tmp/smsrepo")
index = repo.index
remote = repo.remotes[0]

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    
    body = request.values.get('Body', None)
    bodylines = [">>" + x for x in  body.split("\n")] if len(body) > 0 else []

    phonenum = request.values.get("From", None)
    phonenum = phonenum.replace("+", "")

    print(str(request.values))

    remote.pull()

    print(phonenum)
    print(body)

    numMedia = int(request.values.get('NumMedia', None))
    for media in range(numMedia):
        bodylines.append(">>Attachment: " + request.values.get('MediaUrl' + str(media), None))

    with open("/tmp/smsrepo/" + phonenum, "a") as file:
        file.write("\n" + "\n".join(bodylines) + "\n")

    index.add([phonenum])

    index.commit("Incoming message from %s" % (phonenum,))

    remote.push()


    return ("", 204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
