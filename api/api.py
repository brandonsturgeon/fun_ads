from flask import Flask, request
app = Flask(__name__)


@app.route("/api/v1/fun_ads.js")
def fun_ads():
    with open("js/fun_ads.js", "r") as js:
        SCRIPT_STRING = js.read()

    words_request = request.args.get('words') or "no args given"
    formatted = SCRIPT_STRING.replace("{TEXT}", words_request)
    return formatted


if __name__ == "__main__":
    app.run(debug=True, port=5050)
