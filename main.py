from dotenv import dotenv_values
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory

# TODO add reading command line arguments to let data be variable
if __name__ == "__main__":
    env_vars = dotenv_values(".env")
    service_account = GspreadFactory.createServiceAccount(path_to_credentials=env_vars["CREDENTIALS_JSON_FILE"])
    spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name="Hours_Task Tracker - Contractor - HM - 08.19 - 08.23")
    
    robot = SheetRobot(spreadsheet=spreadsheet)

    # robot.fill_in_hours(spreadsheet=spreadsheet,
    #                      date="08.22.2025", 
    #                      desc="Project Setup", 
    #                      hours=1.5)
    
    data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=9)
    print(data["date"] + " | " + data["desc"] + " | " + data["hours"])