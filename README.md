# roomie-bot
[![Build Status](https://travis-ci.com/dipzza/roomie-bot.svg?branch=master)](https://travis-ci.com/dipzza/roomie-bot)
[![codecov](https://codecov.io/gh/dipzza/roomie-bot/branch/master/graph/badge.svg?token=DR8OVMCUBX)](https://codecov.io/gh/dipzza/roomie-bot)

Roomie is a telegram bot with the tools to make life easier for a group of friends or roommates!  
It can help you track your group expenses or organize tasks.

You can use the instance @RoomieDipBot or create your own bot cloning the repository and following the instructions.

Roomie was initially develop for this great course: [curso-tdd](https://github.com/JJ/curso-tdd)

## Instructions

[Poetry](https://python-poetry.org/) is used to manage the project.

To install only the minimum dependencies necessary to run the bot
    
    poetry install --no-dev

To install all dependencies (for development or use of 'poetry run task')
    
    poetry install

To run the bot

1. First export an enviroment variable named 'TOKEN' with you telegram bot token.working
        
        export TOKEN="your_bot_token"

2. Then start the bot
        
        poetry run task bot
        
    or
        
        poetry run python -m roomie_bot

To run unit tests

    poetry run task test
    
To run coverage test

    poetry run task coverage

## Project Structure

+ All code is in the directory 'roomie-bot'.
	- The main module, [bot.py](roomie-bot/bot.py) is responsible for receiving and responding to telegram messages, getting the needed information from the following sub-modules.
	- The [database](roomie-bot/database/) module provides an interface to communicate with the database.
	- The [expenses](roomie-bot/expenses/) module implements the functionalities to monitor debts.
+ All tests are in the directory 'tests', with each file testing a corresponding module.

## Tools
+ Continuous Integration: Travis
+ Data Storage: SQLite
+ Dependecy Management: [Poetry](https://python-poetry.org/)
+ Language: Python with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot).
+ Logging: Python logging module.
+ Task Manager: [Taskipy](https://github.com/illBeRoy/taskipy)
+ Testing Framework: Pytest with pytest-cov

## Credits
RoomieBot is developed and maintained by Dipzza.

I thank the following for their much appreciated contributions

+ [AburoSenpai](https://github.com/AburoSenpai) Icon design.
+ [JJ](https://github.com/JJ) Teaching concepts to make quality software.

### Icon (provisional)

 ![Icono del bot](/img/robotito.png)
