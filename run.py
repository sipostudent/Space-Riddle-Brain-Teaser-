import os
import json
from flask import Flask, render_template, request, redirect
from operator import itemgetter
app = Flask(__name__)

with open("data/highscores.json", "r") as json_data:
    highscores = json.load(json_data)


player_score = 0


def write_to_file(filename, data):
    with open(filename, "a") as file:
        file.writelines(data)


def add_users(username):
    write_to_file("data/users.txt", username.title() + "\n")


riddle_index = 0
riddles = ""


@app.route('/')
def index():
    return render_template("index.html", title="HOME | SPACE RIDDLE")


@app.route('/leaderboard')
def leaderboard():
    with open("data/highscores.json", "r") as json_data:
        highscores = json.load(json_data)
    return render_template("leaderboard.html", title="RANK | SPACE RIDDLE", highscores=highscores)


@app.route('/enter_name', methods=["GET", "POST"])
def enter_name():
    if request.method == "POST":
        username = request.form["username"]
        add_users(username)

        return redirect(username)

    return render_template("enter_name.html", title="REGISTER | SPACE RIDDLE")


@app.route('/<username>', methods=["GET", "POST"])
def play(username):
    with open("data/riddles.json", "r") as json_data:
        riddles = json.load(json_data)
    riddle_index = 0
    player_score = 0
    incorrect = ''
    global user_try
    user_try = 0

    if request.method == "POST":
        riddle_index = int(request.form["riddle_index"])
        player_score = int(request.form["score"])
        user_answer = request.form["answer"].lower()

        user_try = int(request.form["userTry"])

        print("user try: " + str(user_try))

        if user_answer == riddles[riddle_index]["answer"]:

            riddle_index += 1
            player_score += 1
            incorrect = ''
        else:
            print("user try == else: " + str(user_try))
            print(type(user_try))

            if(user_try == 1):
                user_try -= 1
                print("user try == other: " + str(user_try))
                riddle_index += 1

            elif(user_try == 0):
                incorrect = user_answer
                user_try += 1

        if riddle_index > 5:

            result = {
                "name": username,
                "score": player_score
            }

            with open("data/highscores.json", "r") as json_data:
                highscores = json.load(json_data)

            highscores.append(result)
            highscores = sorted(
                highscores, key=itemgetter('score'), reverse=True)

            with open("data/highscores.json", "w") as file:
                json.dump(highscores, file)

            return render_template("leaderboard.html", title="GAME OVER", score=player_score, highscores=highscores)

    return render_template("answer_riddle.html", title="PLAY | SPACE RIDDLE", username=username, riddles=riddles, riddle_index=riddle_index, score=player_score, incorrect=incorrect, userTry=user_try)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
            port=os.environ.get('PORT', '5000'))