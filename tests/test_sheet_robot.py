from dotenv import dotenv_values
import os
import pytest

current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)

# now we can import the module in the directory.
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory

class TestSheetRobot:
    _env_vars = None

    def test_can_add_data(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)
        date = "01.01.2025"
        desc = "example"
        hours = 2
        assert robot.fill_in_hours(spreadsheet=spreadsheet, date=date, desc=desc, hours=hours) == True, "Cannot fill in hours."
    
    def test_can_read_data(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)
        date = "01.01.2025"
        desc = "example"
        hours = "2"
        row_data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=9)
        assert row_data['date'] == date and row_data['desc'] == desc and row_data['hours'] == hours, "Data read does not match."
    
    def test_can_delete_data(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)

        row_to_delete = int(robot._current_cell.split("A")[1]) - 1
        robot.delete_hours_log(spreadsheet=spreadsheet, row_number=row_to_delete)
        data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=row_to_delete)

        empty_date = data["date"] == None or data["date"] == "Empty"
        empty_desc = data["desc"] == None or data["desc"] == "Empty"
        empty_hours = data["hours"] == None or float(data["hours"]) == 0

        assert empty_date == True and empty_desc == True and empty_hours == True, "Data was not deleted from row."
    
    def test_can_print_row_data(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)

        data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=9)
        row_data = []
        row_data.append(data["date"])
        row_data.append(data["desc"])
        row_data.append(data["hours"])
        assert robot.print_row_data(data=row_data) == True, "Could not print row data."
        
    def test_can_print_all_data(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)

        assert robot.print_all_data(spreadsheet=spreadsheet) == True
        
    # def _data_is_from_empty_row(self, data: dict):
    #     empty_date = data["date"] == None or data["date"] == "Empty"
    #     empty_desc = data["desc"] == None or data["desc"] == "Empty"
    #     empty_hours = data["hours"] == None or data["hours"] == 0

    #     print(f'empty_date = {empty_date}')

    #     if empty_date and empty_desc and empty_hours:
    #         return True
    #     else:
    #         return False