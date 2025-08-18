from dotenv import dotenv_values
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory

if __name__ == "__main__":
    env_vars = dotenv_values(".env")
    service_account = GspreadFactory.createServiceAccount(path_to_credentials=env_vars["CREDENTIALS_JSON_FILE"])
    spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name="Hours_Task Tracker - Contractor - HM - 08.10 - 08.23")
    
    robot = SheetRobot(spreadsheet=spreadsheet)

    robot.fill_in_hours(spreadsheet=spreadsheet,
                         date="08.18.2025", 
                         desc="More work on productivity tool", 
                         hours=1)