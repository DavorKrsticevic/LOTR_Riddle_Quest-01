import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template("game_page.html")
    
@app.route('/final_score')
def final_score():
    return render_template("final_score.html")   
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)