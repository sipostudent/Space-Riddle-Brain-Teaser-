# SPACE RIDDLE - Guessing Game

## Table of contents

<!--ts-->

- [Table of contents](#table-of-contents)
- [About](#About)

  - [Goal](#Goal)
  - [Functionality](#Functionality)
  - [Initiation](#Initiation)

- [UX](#UX)

- [Technologies](#Technologies)

- [Features](#Features)
  - [Existing-Features](#Existing-Features)
  - [Features-Left-to-Implement](#Features-Left-to-Implement)
- [Testing](#Testing)

- [Deployment](#Deployment)

- [Credits](#Credits)
  - [Content](#Content)
  - [Media](#Media)
  - [Acknowledgements](#Acknowledgements)
    <!--te-->

## About

This application (app) is a game that asks players to guess the answer to a text-based riddle.

#### Goal

Create a multi-player guessing game, suitable for website usage. The core focus of this project is on functional game logic created with Python while utilising the Flask micro web framework which is also written in Python.

#### Functionality

- A web application game that asks players to guess the answer to a text-based riddle. Riddles are generated and presented to players in the form of text.
- Players enter their answer into a text field and submit using a form. If a player's guess is correct, they progress to the next riddle.
- If a player’s guess is incorrect, their incorrect solution is stored and printed below the riddle.
- Player’s given two chances total at a guess, after which point the game will progress to the next riddle regardless of whether or not the player has guessed the riddle answer correctly.
- The text area is reset to blank after every guess attempt, so players can guess again. Players are identified by a unique username which allows for multiple players to play an instance of the game at the same time.
- Top scores for the top three players are ranked and added to a leader board.

#### Initiation

Research to understand what apps of similar scope were already doing in terms of functionality which provided me with a list of what I consider to be feasible options for functionality implementations to acknowledge and consider pre-production.
