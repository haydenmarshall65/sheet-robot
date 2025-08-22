import gspread

class GspreadFactory:
    def createServiceAccount(path_to_credentials):
        return gspread.service_account(filename=path_to_credentials)

    def getWorkSheet(service_account, spreadsheet_name):
        spreadsheet = service_account.open(spreadsheet_name)
        return spreadsheet.get_worksheet(0)