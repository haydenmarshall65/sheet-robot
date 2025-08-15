from dotenv import dotenv_values
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory


if __name__ == "__main__":
    env_vars = dotenv_values(".env")
    service_account = GspreadFactory.createServiceAccount(path_to_credentials=env_vars["CREDENTIALS_JSON_FILE"])
    spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name="Example Spreadsheet")
    robot = SheetRobot()
    robot.fill_in_hours(spreadsheet, "08.12.2025", "Example description", 1.5)