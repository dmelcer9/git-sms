from flask import Flask, request

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    
    print(body)

    return ("", 204)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
