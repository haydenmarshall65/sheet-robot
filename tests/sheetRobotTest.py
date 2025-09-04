from dotenv import dotenv_values
import os

current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)

# now we can import the module in the directory.
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory

class SheetRobotTester:
    _env_vars = None

    total_tests = 5

    def run_tests(self) -> bool:
        self._env_vars = dotenv_values(parent + '/.env')

        tests_passed = 0
        if self.testCanAddData() == 1:
            tests_passed += 1
            print("canAddData: ✓")
        else:
            print("canAddData: X")
        if self.testCanReadData() == 1:
            tests_passed += 1
            print("canReadData: ✓")
        else:
            print("canReadData: X")
        if self.testCanDeleteData() == 1:
            tests_passed += 1
            print("canDeleteData: ✓")
        else:
            print("canDeleteData: X")
        if self.testCanPrintRowData() == 1:
            tests_passed += 1
            print("canPrintRowData: ✓")
        else:
            print("canPrintRowData: X")
        if self.testCanPrintAllData() == 1:
            tests_passed += 1
            print("canPrintAllData: ✓")
        else:
            print("canPrintAllData: X")

        print("sheet robot tests passed: " + str(tests_passed))

        # return whether or not all tests passed
        return tests_passed == 5
      
    def testCanAddData(self):
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)
        date = "01.01.2025"
        desc = "example"
        hours = 2
        try:
            robot.fill_in_hours(spreadsheet=spreadsheet, date=date, desc=desc, hours=hours)
            return 1
        except Exception as err:
            print(f"could not fill in data. Reason for Error: {err}")
            return 0
    
    def testCanReadData(self):
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)
        date = "01.01.2025"
        desc = "example"
        hours = "2"
        try:
            row_data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=9)
            if row_data['date'] == date and row_data['desc'] == desc and row_data['hours'] == hours: 
                return 1
            else: 
                print("could not read data or data was incorrect")
                return 0
        except Exception as err:
            print(f"could not read data. Reason for Error: {err}")
            return 0
    
    def testCanDeleteData(self):
        try:
            service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
            spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
            robot = SheetRobot(spreadsheet=spreadsheet)

            row_to_delete = int(robot._current_cell.split("A")[1]) - 1
            robot.delete_hours_log(spreadsheet=spreadsheet, row_number=row_to_delete)
            data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=row_to_delete)

            if self._data_is_from_empty_row(data=data):
                print("Data was successfully deleted.")
                return 1
            else:
                print("Did not delete data.")
                return 0
        except Exception as err:
            print(f"Could not delete data. Reason for Error: {err}")
            return 0
    
    def testCanPrintRowData(self):
        try:
            service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
            spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
            robot = SheetRobot(spreadsheet=spreadsheet)

            data = robot.read_data_on_row(spreadsheet=spreadsheet, row_number=9)
            robot.print_row_data(data=data)
            return 1
        except Exception as err:
            print(f"Could not print row data. Reason for Error: {err}")
            return 0
        
    def testCanPrintAllData(self):
        try:
            service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
            spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
            robot = SheetRobot(spreadsheet=spreadsheet)

            robot.print_all_data(spreadsheet=spreadsheet)
            return 1
        except Exception as err:
            print(f"Could not print row data. Reason for Error: {err}")
            return 0
        
    def _data_is_from_empty_row(self, data: dict):
        empty_date = data["date"] == None or data["date"] == "Empty"
        empty_desc = data["desc"] == None or data["desc"] == "Empty"
        empty_hours = data["hours"] == None or data["hours"] == 0

        print(f'empty_date = {empty_date}')

        if empty_date and empty_desc and empty_hours:
            return True
        else:
            return False