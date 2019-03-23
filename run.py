import os
import json
from flask import Flask, render_template, request, redirect
from operator import itemgetter
app = Flask(__name__)

with open("data/highscores.json", "r") as json_data:
    highscores = json.load(json_data)

#highscores = [(10, 'Sipo'), (5, 'Matt')]
#print(highscores)
player_score = 0
# global userTry
# userTry = 0

# result = {
#                 "name" : "ZB",
#                 "score": 10
#             } 
# print(result)
# highscores.append(result)
# #toWrite = json.dump(highscores)
# print(highscores)

# with open("data/highscores.json", "w") as file:
#     json.dump(highscores, file)
    #file.writelines(str(toWrite))

def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)


def add_users(username):
    write_to_file("data/users.txt", username.title() + "\n")
    #username  = username


#username = ""
riddle_index = 0
riddles = ""


@app.route('/')
def index():
    return render_template("index.html", title="Home Page | Space Riddle")


@app.route('/leaderboard')
def leaderboard():
    with open("data/highscores.json", "r") as json_data:
        highscores = json.load(json_data)
    return render_template("leaderboard.html", title="Leaderboard | Space Riddle", highscores = highscores)


@app.route('/enterName', methods=["GET", "POST"])
def enterName():
    if request.method == "POST":
        username = request.form["username"]
        add_users(username)
        #redirecting before
        return redirect(username)
       #return render_template("answerRiddle.html", title="Answer Riddle | Space Riddle", username=username, riddle_index=riddle_index, riddles=riddles)
    return render_template("enterName.html", title="Enter Name | Space Riddle")


@app.route('/<username>', methods=["GET", "POST"])
def play(username):
    with open("data/riddles.json", "r") as json_data:
        riddles = json.load(json_data)
    riddle_index = 0
    player_score = 0
    incorrect = ''
    global user_Try
    user_Try = 0

    if request.method == "POST":
        riddle_index = int(request.form["riddle_index"])
        player_score = int(request.form["score"])
        user_answer = request.form["answer"].lower()
        
        user_Try = int(request.form["userTry"])

        print("user try: " + str(user_Try))

        if user_answer in riddles[riddle_index]["answer"]:
            # Correct answer
            # Go to next riddle
            riddle_index += 1
            player_score += 1
            incorrect = ''
        else:
            print("user try in else: " + str(user_Try))
            print(type(user_Try))
            
            if(user_Try == 1):
                user_Try -=1
                print("user try in other: " + str(user_Try))
                riddle_index += 1

            elif(user_Try == 0):
                incorrect = user_answer
                user_Try += 1
            
            
            

        if riddle_index > 5:
            #highscores.append((player_score, username.title()))
            #highscores.sort(reverse=True)
            #highscores.append({"name": username.title(), "score": player_score})
            
            
            result = {
                "name" : username,
                "score": player_score
            } 

            with open("data/highscores.json", "r") as json_data:
                highscores = json.load(json_data)

            highscores.append(result)
            highscores = sorted(highscores, key=itemgetter('score'), reverse=True)
            highscores = highscores[:-1]
            print(highscores)

            with open("data/highscores.json", "w") as file:
                json.dump(highscores, file)

            return render_template("leaderboard.html", title="Game Over", score = player_score, highscores=highscores)
        #print(username)
    return render_template("answerRiddle.html", title="Play Game | Space Riddle", username=username, riddles=riddles, riddle_index=riddle_index, score=player_score, incorrect = incorrect, userTry = user_Try)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=50,
            debug=True)
