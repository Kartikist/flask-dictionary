from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route("/")
def meaning():

    return render_template("dictionary.html")


@app.route("/api/v1/<word>")
def extract_meaning(word):

    df = pd.read_csv("dictionary.csv")

    defi = df.loc[df["word"] == word]["definition"].squeeze()
    dictionary = {"word:": word,
                  "defintion: ": defi}
    return dictionary


if __name__ == ("__main__"):
    app.run(debug=True)
