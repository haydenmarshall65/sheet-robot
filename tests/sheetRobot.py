from sheetRobot import SheetRobot
from dotenv import dotenv_values
from gspreadFactory import GspreadFactory

class SheetRobotTester:
    _env_vars

    def run_tests(self):
        self.env_vars = dotenv_values("../.env")

        testsPassed = 0
        if self.testCanAuthenticate() == 1:
            testsPassed += 1
            print("canAuthenticate: TRUE")
        else:
            print("canAuthenticate: FALSE")
      
    def testCanAuthenticate(self):
        try: 
            GspreadFactory.createServiceAccount(path_to_credentials=self.env_vars["CREDENTIALS_JSON_FILE"])
            return 1
        except:
            print("Could not authenticate.")
            return 0
    
    def testCanGetWorksheet(self):
        try: 
            service_account = GspreadFactory.createServiceAccount(path_to_credentials=self.env_vars["CREDENTIALS_JSON_FILE"])
            spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self.env_vars["TEST_SPREADSHEET"])
            return 1
        except:
            print("Could not get a spreadsheet.")
            return 0
    
    def testCanAddData(self):
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self.env_vars["CREDENTIALS_JSON_FILE"])
        spreadsheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self.env_vars["TEST_SPREADSHEET"])
        robot = SheetRobot(spreadsheet=spreadsheet)
        robot.fill_in_hours(spreadsheet=spreadsheet, date="01.01.2025", desc="example", hours=2)
        # TODO add rest of test to see if the data here actually fills in properly and that the next row updates properly

