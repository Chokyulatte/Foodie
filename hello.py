from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/address")
def selAddress():
    return render_template('addressPreference.html')


if __name__ == "__main__":
    app.run()