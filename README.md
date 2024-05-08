# Chessnlyzer - Local webapp to analyze my games

This app is to learn how

- to build an web-application with flask,
- to use the lichess.org api and
- to analyze my chess games.

## Programming Tools

To create this app I have used:

- Python, HTML, CSS
- Flask
- lichess.org-API-Client Berserk
- Jupyter Lab
- Fedora Linux 40 (arm64)

After attending the MLH Global Hack Week: API I wanted to explore the lichess.org API to do stuff with my chess game data. I decided to create an webapp to be able to display graphs and other analytical results.
I also decided that I want to use a python framework, because I did not feel confident enough to use Java Script.
After testing Django and Flask I went with Flask, for it to be the lighter framework. I had the feeling getting-started-part felt easier.

## Flask App

The Flask App is called chessnlyzer and has only one page so far.

The main feature is that it fetches my lichess account data and displays it on the index page.

### Directory Tree

### Main Components

The main components are

- the factory function, that initialyzes the app instance and registeres the other modules
- the database module db.py, that creates the sqlite connection and initializes the user table
- the simple blog module blog.py, that is interface to render the index page and the lichess client requests
- the lichess client clientLichess.py, that creates a session and fetches the latest ratings

## Main Application

The main application is still work in progress.

In chess-app/lab-lichess/CGames.py I am working an a rudimentary implementation of the chess game. The first step is to create the game engine that is able to play a complete game of chess.

CGames.py is the game implementation with classes for the Game, the Board, the Pieces and the Position.

The next step is to implement the chess app in the flask app and render a chess board to a separate web-app-site. The most difficult part for now is that I don't know how to connect the python app with the flask app. That will be one of the next milestones.

After that I want to integrate a game analyzing tool that summerizes good and bad moves.

In the future I want to concentrate on a anti-cheating toll. That is my main motivation. It is the worst to play someone online and have this feeling of being cheated on.
