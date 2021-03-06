from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/<text>")
def main_page(text):
    return render_template('main.html', text=text)

if __name__ == "__main__":
    app.run(debug=True)
