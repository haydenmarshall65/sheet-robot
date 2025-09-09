from tests import gspreadFactoryTest
from tests import sheetRobotTest

class Tester:

    def run_all_tests(self):
        gspread_tester = gspreadFactoryTest.GspreadFactoryTester()
        gspread_tests_passed = gspread_tester.run_tests()

        if not gspread_tests_passed:
            print("GspreadFactory tests failed.")
            return

        sheet_robot_tester = sheetRobotTest.SheetRobotTester()
        sheet_robot_tests_passed = sheet_robot_tester.run_tests()

        if not sheet_robot_tests_passed:
            print("Sheet Robot tests failed")
            return
        
        print("All tests passed!")


tester = Tester()
tester.run_all_tests()