#!/bin/bash

pyinstaller main.py sheetRobot.py gspreadFactory.py --name=sheet-robot --add-data=.env:. --add-data=sheet-robot-credentials.json:. -p $HOME/projects/sheet-robot --onefile --distpath=bin