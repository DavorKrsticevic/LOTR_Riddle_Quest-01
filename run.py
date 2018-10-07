import os
from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

user_list = []
user_answer = []
riddle_number = 0
# user_correct = 0
# user_wrong = 0

		

# def score_and_riddle_update():
# 	if check_user_answer(user_answer) == True:
#         	riddle_number + 1
# 		user_correct + 1
# 	if check_if_true_or_false == False:
# 		user_wrong + 1



@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "POST":
        user_list.append(request.form["username"])
        return redirect("/game")
    return render_template("index.html")

@app.route('/game', methods = ["GET","POST"])
def game():
    data = []
    with open ("data/riddles.json", "r") as jason_data:
        data = json.load(jason_data)
    if request.method == "POST":
        user_answer.append(request.form["answer"])
        if user_answer [-1] == data[riddle_number]["answer"]:
            print ("tocno")
        else:
            print ("pogresno")
        
    return render_template("game_page.html", user_list = user_list, riddles_data = data, user_answer=user_answer)
    

@app.route('/final_score')
def final_score():
    return render_template("final_score.html") 
    
@app.route('/contact')
def contact():
    return render_template("contact.html")



def check_user_answer(user_answer):
    data = []
    with open ("data/riddles.json", "r") as jason_data:
        data = json.load(jason_data)	
 	if user_answer == data [riddle_number]["answer"]:
 		return True
 	else: 
 		return False

    print check_user_answer(user_answer)

    print user_answer    


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)