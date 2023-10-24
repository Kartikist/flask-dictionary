from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def meaning():
    
    return render_template("dictionary.html")

@app.route("/api/v1/<word>")
def extract_meaning(word):
    defi = word.upper()
    dictionary = {"word:": word,
                  "defintion: ": defi}
    return dictionary
    
    

if __name__ == ("__main__"):
    app.run(debug=True)
    