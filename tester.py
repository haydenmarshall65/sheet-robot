from tests import test_gspread_factory
from tests import test_sheet_robot

class Tester:

    def run_all_tests(self):
        gspread_tester = test_gspread_factory.GspreadFactoryTester()
        gspread_tests_passed = gspread_tester.run_tests()

        if not gspread_tests_passed:
            print("GspreadFactory tests failed.")
            return

        sheet_robot_tester = test_sheet_robot.SheetRobotTester()
        sheet_robot_tests_passed = sheet_robot_tester.run_tests()

        if not sheet_robot_tests_passed:
            print("Sheet Robot tests failed")
            return
        
        print("All tests passed!")


tester = Tester()
tester.run_all_tests()