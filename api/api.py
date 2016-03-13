from flask import Flask, request
app = Flask(__name__)

SCRIPT_STRING = "alert('{}')"

@app.route("/api/v1/fun_ads.js")
def fun_ads():
    words_request = request.args.get('words') or "no args given"
    return SCRIPT_STRING.format(words_request)


if __name__ == "__main__":
    app.run(debug=True, port=5050)
