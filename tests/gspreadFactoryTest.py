from dotenv import dotenv_values
import os

current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)

# now we can import the module in the directory.
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory

class GspreadFactoryTester:

    _env_vars = None
    total_tests = 2

    def run_tests(self) -> bool :
        self._env_vars = dotenv_values(parent + '/.env')
        
        tests_passed = 0

        if self.testCanAuthenticate() == 1:
            tests_passed += 1
            print("canAuthenticate: ✓")
        else:
            print("canAuthenticate: X")

        if self.testCanGetWorksheet() == 1:
            tests_passed += 1
            print("canGetWorksheet: ✓")
        else:
            print("canGetWorksheet: X")

        print(f"gspread factory tests passed: {tests_passed}")
        # return if all tests passed or not
        return tests_passed == 2


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