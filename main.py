from flask import Flask, redirect, render_template, request
from caesar import encrypt
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods = ["GET", "POST"])
def index():
    rot_val = 0
    etext = ""
    if request.method == "POST":
        rot_val = int(request.form["r"])
        ptext = request.form["t"]
        etext = encrypt(ptext, rot_val)

    return render_template("index.html", rot = rot_val, txt = etext)

def main():
    app.run()

if __name__ == "__main__":
    main()
