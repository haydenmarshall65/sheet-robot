import gspread
from gspread import Client
from gspread import Worksheet

class GspreadFactory:
    def createServiceAccount(path_to_credentials: str) -> Client:
        return gspread.service_account(filename=path_to_credentials)

    def getWorkSheet(service_account: Client, spreadsheet_name: str) -> Worksheet:
        spreadsheet = service_account.open(spreadsheet_name)
        return spreadsheet.get_worksheet(0)