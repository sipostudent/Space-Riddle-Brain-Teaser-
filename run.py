import os
import json
from flask import Flask, render_template, redirect, request
app = Flask(__name__)

player_score =0
riddle_index = 0
riddles = ""


@app.route('/')
def index():
    return render_template("index.html", title="Home Page | Space Riddle")


@app.route('/leaderboard')
def leaderboard():
    
    return render_template("leaderboard.html", title="Leaderboard | Space Riddle")


@app.route('/enterName', methods=["GET", "POST"])
def enterName():
    if request.method == "POST":
        username = request.form["username"]
        #redirecting before
        return redirect(username)
       
    return render_template("enterName.html", title="Enter Name | Space Riddle")


@app.route('/<username>', methods=["GET", "POST"])
def play(username):
    with open("data/riddles.json", "r") as json_data:
        riddles = json.load(json_data)
    riddle_index = 0

    if request.method == "POST":
        riddle_index = int(request.form["riddle_index"])
        player_score = int(request.form["score"])
        user_answer = request.form["answer"].lower()
        

        if user_answer in riddles[riddle_index]["answer"]:
            # Correct answer
            # Go to next riddle
            riddle_index += 1
            player_score += 1
            
        else:
         
            riddle_index += 1

            
            
            

        if riddle_index > 5:
            
            return render_template("leaderboard.html", title="Game Over", score = player_score)
        
    return render_template("answerRiddle.html", title="Play Game | Space Riddle", username=username, riddles=riddles, riddle_index=riddle_index, score=player_score)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=50,
            debug=True)
