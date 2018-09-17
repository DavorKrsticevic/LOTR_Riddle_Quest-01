import os
from flask import Flask, render_template, request

app = Flask(__name__)
user_score = []
user_list = []

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method == "POST":
        user_list.append(request.form["username"])
    return render_template("index.html")


@app.route('/game')
def game():
    return render_template("game_page.html", user_list = user_list)
    
@app.route('/final_score')
def final_score():
    return render_template("final_score.html") 
    
@app.route('/contact')
def contact():
    return render_template("contact.html")


#@app.route('/<username>')
#def user(username):
#    return "Hi " + username









#@app.route('/<username>/<score>')
#def send_message(username, score):
#    return "{0}: {1}".format(username, score)

#def userscore(username, score):
#    user_score.append("{}: {}".format(username, score))







    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)