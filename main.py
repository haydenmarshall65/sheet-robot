from dotenv import dotenv_values
from sheetRobot import SheetRobot

def initSheetRobot(path_to_credentials) -> SheetRobot:

    sheet_robot = SheetRobot(path_to_credentials=path_to_credentials)

    return sheet_robot


if __name__ == "__main__":
    env_vars = dotenv_values(".env")
    robot = initSheetRobot(path_to_credentials=env_vars["CREDENTIALS_JSON_FILE"])

    robot.set_current_spreadsheet("Example Spreadsheet")
    robot.fill_in_hours("08.12.2025", "Example description", 1.5)