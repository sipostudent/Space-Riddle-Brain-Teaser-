# SPACE RIDDLE - Guessing Game

## Table of Contents

<!--ts-->

- [About](#About)

  - [Goal](#Goal)
  - [Functionality](#Functionality)
  - [Initiation](#Initiation)

- [UX](#UX)

- [Technologies](#Technologies)

  - [Languages Frameworks Tools](#Languages-Frameworks-Tools)
  - [Other-Resources](#Other-Resources)

- [Features](#Features)

  - [Existing Features](#Existing-Features)
  - [Features-Left-to-Implement](#Features-Left-to-Implement)

- [Testing](#Testing)

- [Deployment](#Deployment)

  - [How the project got deployed to Heroku](#How-the-project-got-deployed-to-Heroku)
  - [How to run things locally](#How-to-run-things-locally)

- [Credits](#Credits)

  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)
    <!--te-->

## About

This application (app) is a game that asks players to guess the answer to a text-based riddle.

#### Goal

Create a multi-player guessing game, suitable for website usage. The core focus of this project is on functional game logic created with Python while utilising the Flask micro web framework also written in Python.

#### Functionality

- A web application game that requests that players surmise the response to a content-based riddle.
- Riddles are generated and presented to players in the form of text.
- Players enter their answer into a text field and submit using a form.
- If a player's guess is correct, they progress to the next riddle.
- If a player’s guess is incorrect, their incorrect solution is stored and printed below the riddle.
- Player’s given two chances total at a guess, after which point the game will progress to the next riddle regardless of whether or not the player has guessed the riddle answer correctly.
- The text area is reset to blank after every guess attempt so that players can guess again. Players are identified by a unique username which allows for multiple players to play an instance of the game at the same time.
- Top scores for the main three players are positioned and added to a leader board.

#### Initiation

Research to understand what apps of similar scope were already doing in terms of functionality which provided me with a list of what I consider to be feasible options for functionality implementations to acknowledge and consider pre-production.

## UX

- (Pending)

## Technologies

#### Languages Frameworks Tools

- [HTML5](https://www.w3.org/TR/html5/ "HTML5 Official Site")

  - Semantic markup language utilised as the shell of the site.

- [CSS3](https://www.w3.org/Style/CSS/ "Cascading Style Sheets Official Site")

  - Cascading Style Sheets as the design of the site.

- [jQuery](http://jquery.com/ "Cascading Style Sheets Official Site")

  - HTML document traversal and manipulation, event handling.

- [Bootstrap - v4.1.1](https://getbootstrap.com/docs/4.1/getting-started/introduction/ "Bootstrap Official Site")

  - Utilised for developing the entire UI and consistent throughout

- [Python 3.7.0](https://www.python.org/ "Python Official Site")

  - Utilised to compose the game logic.

- [GitHub](https://github.com/ "GitHub Official Site")

  - Utilised for committing code.

- [Heroku](https://www.heroku.com/ "Heroku Official Site")

  - Utilised for deploying the project.

- [Google Fonts](https://fonts.google.com/ "Google Fonts Official Site")

  - Saira font applied across the entire website

- [Font Awesome - v5.0.13](https://fontawesome.com/ "Fontawesome Official Site")

  - Source for all utilised icons

#### Other Resources

- https://getbootstrap.com/
- https://www.w3schools.com/
- https://stackoverflow.com/
- https://slack.com/

## Features

#### Existing Features

- Home Page

  - Used to access the user registration page field.

- User Registration

  - Utilised to enter player name and progress to game start.

- JSON

  - Store player high scores for each game play instance and hold the game riddles.

- Message Notifications

  - Inform a player of their current score, when errors are made in answer guessing and displaying player's the final score.

- Form
  - Enter player responses to the riddles.

#### Features Left to Implement

- More riddles, with an arbitrary determination, exhibited each time a player login/registers; thus, enabling them to play the game on different occasions without seeing similar riddles repeatedly.

- Audio sound/effects which would improve increase the user experience.

- The alternative to come back to the game with a current player name. Without secure player confirmation, which is beyond the scope of this module, there is currently no way to separate between a returning player and a player who has picked the equivalent player name as another player. Subsequently, players must choose another player name each time they register.

## Testing

- (Pending)

## Deployment

#### How the project got deployed to Heroku

1. Select Extensions and install Heroku-cli
2. In the terminal, type "Heroku" to initialise
3. In the terminal type "Heroku login."
4. Go to Heroku, select region, e.g. Europe, and then "Create New App."
5. In "Deployment method" section, select "GitHub Connect to GitHub."
6. In "Connect to GitHub" section, search for relevant project repository to connect to by pressing search and selecting or typing the repo name into "repo-name" field followed by pressing connect.
7. In the "Automatic deploys" section, select "enable automatic deploys."
8. In the "Manual deploy" section, Choose relevant branch to deploy, then click "Deploy Branch."
9. Select "Activity" tab and click on "View build log" to confirm notification of "Build succeeded and "Deployed" application.

#### How to run things locally

1. Download the project onto a PC and open with a source-code editor.
2. In the run.py file set the IP address to 127.0.0.1 and the PORT to 5000.
3. Install all of the prerequisites shown in the requirements.txt file.
4. Initiate the app by entering the following command into a relevant terminal: python run.py

## Credits

#### Content

- Except for the app (game) riddles, all written content is bespoke and created by the code author (Sipo Charles).

#### Media

- N/A

#### Acknowledgements

- I received inspiration for this project from visiting [miniclip.com](https://www.miniclip.com/games/en/ "Miniclip Official Site"), but mostly from my interaction with other students on Code Institute's Full Stack Software Development Programme.
