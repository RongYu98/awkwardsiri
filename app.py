from flask import Flask, render_template, request, redirect, url_for, session
import awkwardsiri, urllib2, google, bs4, re


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("home.html")
    query = request.form["question"]
    answer = awkwardsiri.finder(query)
    print "-----------------------------------------------"
    print answer
    print "-----------------------------------------------"
    return render_template("home.html", response = answer, question = query)


if (__name__ == "__main__"):
        app.debug = True
        app.secret_key = "secret"
        app.run(host='0.0.0.0', port=8000)
