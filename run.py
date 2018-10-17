import os
from flask import Flask, render_template, request, redirect, session
import json

app = Flask(__name__)
app.secret_key = os.urandom(24)


user_list = []
user_answer = []


with open ("data/riddles.json", "r") as jason_data:
        riddle_data = json.load(jason_data)

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        user_list.append(request.form["username"])
        session['user_name'] = request.form['username']
        session['riddle_number'] = 0
        session['user_correct'] = 0
        session['user_wrong'] = 0
        return redirect("/game")
    return render_template("index.html")

@app.route('/game', methods=["GET","POST"])
def game():

    if request.method == "POST":
        previous_riddle_number = session['riddle_number']
        user_answer.append(request.form["answer"])
        if user_answer [-1] == riddle_data[previous_riddle_number]["answer"]:
            session['riddle_number'] += 1
            session['user_correct'] += 1
        else:
            session['user_wrong'] += 1
        print (session['riddle_number'], session['user_correct'], session['user_wrong'])
    return render_template("game_page.html", user_name = session['user_name'], riddles_data = riddle_data, user_answer=user_answer, riddle_number=session['riddle_number'])
    

@app.route('/final_score')
def final_score():
    return render_template("final_score.html") 
    
    
@app.route('/contact')
def contact():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)