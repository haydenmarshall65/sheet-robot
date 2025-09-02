import gspread
from gspread import Client
from gspread import Spreadsheet

class GspreadFactory:
    def createServiceAccount(path_to_credentials: str) -> Client:
        return gspread.service_account(filename=path_to_credentials)

    def getWorkSheet(service_account: Client, spreadsheet_name: str) -> Spreadsheet:
        spreadsheet = service_account.open(spreadsheet_name)
        return spreadsheet.get_worksheet(0)