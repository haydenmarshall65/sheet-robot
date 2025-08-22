from dotenv import dotenv_values
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

# now we can import the module in the directory.
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory

class SheetRobotTester:
    _env_vars = None

    def run_tests(self):
        self._env_vars = dotenv_values(parent + '/.env')

        testsPassed = 0
        if self.testCanAuthenticate() == 1:
            testsPassed += 1
            print("canAuthenticate: ✓")
        else:
            print("canAuthenticate: X")
        if self.testCanGetWorksheet() == 1:
            testsPassed += 1
            print("canGetWorksheet: ✓")
        else:
            print("canGetWorksheet: X")
        if self.testCanAddData() == 1:
            testsPassed += 1
            print("canAddData: ✓")
        else:
            print("canAddData: X")
        if self.testCanReadData() == 1:
            testsPassed += 1
            print("canReadData: ✓")
        else:
            print("canReadData: X")
        print("tests passed: " + str(testsPassed))
      
    def testCanAuthenticate(self):
        try: 
            GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
            return 1
        except Exception as err:
            print(f"Could not authenticate. Reason for Error: {err}")
            return 0
    
    def testCanGetWorksheet(self):
        try: 
            service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
            GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
            return 1
        except Exception as err:
            print(f"Could not get a spreadsheet. Reason for Error: {err}")
            return 0
    
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
        

test = SheetRobotTester()
test.run_tests()