from dotenv import dotenv_values
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory
import argparse

parser = argparse.ArgumentParser(prog="Sheet Robot", description="Modify and update Google Sheets files for hours tracking")

# first argument, the necessary file
parser.add_argument('file', help="The name of the file to edit.")

# next, the command available - read or write
commandGroup = parser.add_argument_group('Commands')
commandGroup.add_argument('-w', action="store_true", help="Write to the file given.")
commandGroup.add_argument('-r', action="store_true", help="Read from the file given.")

# finally, the data provided by the user
dataGroup = parser.add_argument_group('Data')
dataGroup.add_argument('--row', type=int, help="The row number to read/write to from the google sheet.")
dataGroup.add_argument('--date', type=str, help="The date the work was done.")
dataGroup.add_argument('--desc', type=str, help="The description of work done.")
dataGroup.add_argument('--hours', type=float, help="The hours worked.")

# TODO add reading command line arguments to let data be variable
if __name__ == "__main__":
    args = parser.parse_args()

    env_vars = dotenv_values(".env")
    service_account = GspreadFactory.createServiceAccount(path_to_credentials=env_vars["CREDENTIALS_JSON_FILE"])
    spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=args.file)
    
    robot = SheetRobot(spreadsheet=spreadsheet)

    if args.w == True and args.r == True:
        print("Cannot read and write at the same time. Provide only one argument")
    elif args.w == True:
        date = args.date
        desc = args.desc
        hours = args.hours
        row = args.row

        robot.fill_in_hours(spreadsheet=spreadsheet, date=date, desc=desc, hours=hours, optional_row_number=row)
    elif args.r == True:
        row = args.row
        if row == None:
            robot.print_all_data(spreadsheet=spreadsheet)
        else:
            data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=row)

            robot.print_row_data(data=data)
    else:
        print("Please choose whether to read or write to a google sheet.")