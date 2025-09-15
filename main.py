from dotenv import load_dotenv
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory
import argparse
import os
import pathlib
import re

parser = argparse.ArgumentParser(prog="Sheet Robot", description="Modify and update Google Sheets files for hours tracking")

# first argument, the necessary file
parser.add_argument('file', help="The name of the file to edit.")

# next, the command available - read or write
commandGroup = parser.add_argument_group('Commands')
commandGroup.add_argument('-w', action="store_true", help="Write to the spreadsheet given.")
commandGroup.add_argument('-r', action="store_true", help="Read from the spreadsheet given.")
commandGroup.add_argument('-n', action="store_true", help="Create new spreadsheet using the file name given.")

# finally, the data provided by the user
dataGroup = parser.add_argument_group('Data')
dataGroup.add_argument('--row', type=int, help="The row number to read/write to from the google sheet.")
dataGroup.add_argument('--date', type=str, help="The date the work was done.")
dataGroup.add_argument('--desc', type=str, help="The description of work done.")
dataGroup.add_argument('--hours', type=float, help="The hours worked.")

# TODO add reading command line arguments to let data be variable
if __name__ == "__main__":
    print("Starting Sheet Robot...")
    try:
        HOME = os.getenv("HOME")
        env_file_path = pathlib.Path(HOME+"/projects/sheet-robot/.env")
        load_dotenv(env_file_path)
        args = parser.parse_args()

        credentials_path = pathlib.Path(HOME+"/projects/sheet-robot/" + os.getenv("CREDENTIALS_JSON_FILE"))
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=credentials_path)
        

        if args.n == True:
            worksheet = GspreadFactory.createNewSpreadSheet(credentials_path, args.file)
        else:
            worksheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=args.file)

        robot = SheetRobot(worksheet=worksheet)

        if args.w == True and args.r == True:
            print("Cannot read and write at the same time. Provide only one argument")
        elif args.w == True:
            date = args.date
            desc = args.desc
            hours = args.hours
            row = args.row

            if date == None:
                date = input("What is the date of work done?: MM/DD/YYYY \n")
                # validate
                pattern = "[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{4}"
                while True:
                    if not re.fullmatch(pattern=pattern, string=date):
                        date = input("Please enter a valid date format: MM/DD/YYYY \n")
                    else:
                        break


            if desc == None:
                desc = input("What is the description of work done?\n")
            if hours == None:
                while True:
                    try:
                        hours_str = input("How many hours worked? Please enter in decimal format, i.e. 1 or 2.5\n")
                        hours = float(hours_str)
                        break
                    except:
                        print("Please input a valid decimal number.")
            if row == None:
                while True:
                    try:
                        row_input = input("Which row number? Leave empty if not applicable.\n")
                        if row_input == "":
                            break
                        else:
                            row = int(row_input)
                            break
                    except:
                        print("Please input a valid row number.")
                
            robot.fill_in_hours(worksheet=worksheet, date=date, desc=desc, hours=hours, optional_row_number=row)
        elif args.r == True:
            row = args.row
            if row == None:
                robot.print_all_data(worksheet=worksheet)
            else:
                data = robot.read_data_on_row(worksheet=worksheet, row_number=row)
                row_data = []
                row_data.append(data["date"])
                row_data.append(data["desc"])
                row_data.append(data["hours"])

                robot.print_row_data(data=row_data)
        else:
            print("Please choose whether to read or write to a google sheet.")
    except KeyboardInterrupt:
        print("Sheet Robot shutting down...")
    finally:
        print("Sheet Robot shutting down...")