from flask import Flask, render_template
from datetime import datetime
app = Flask("Hello")

posts = [

            {
                "title": "FIM DOS TEMPOS",
                "body" : " O mundo vai acabar. E vai ser dia 30/02",
                "author" : "O Vidente",
                "created" : datetime (2012,12,25)
            },
            {
                "title": "Era tudo MENTIRA!!!",
                "body" : " Vidente mentiu era um charlatão, supera",
                "author" : "O Detetive",
                "created" : datetime (2012,12,26)
            }

        ]
@app.route("/")
def index():
    return render_template("index.html", posts = posts)


