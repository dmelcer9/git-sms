from Flask import Flask, request

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)
    
    print(body)

if __name__ == "__main__"
    app.run(debug=True)