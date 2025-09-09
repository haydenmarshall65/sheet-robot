#!/bin/bash

pyinstaller main.py sheetRobot.py gspreadFactory.py --name=sheet-robot --add-data=.env:. --add-data=sheet-robot-credentials.json:. --onefile --distpath=bin