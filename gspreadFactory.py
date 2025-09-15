import gspread

class GspreadFactory:
    def createServiceAccount(path_to_credentials: str) -> gspread.Client:
        return gspread.service_account(filename=path_to_credentials)

    def createNewSpreadSheet(path_to_credentials: str, file_name: str) -> gspread.Worksheet:
        service_account = gspread.service_account(filename=path_to_credentials)
        spreadsheet = service_account.create(file_name)
        return spreadsheet.get_worksheet(0)

    def getWorkSheet(service_account: gspread.Client, spreadsheet_name: str) -> gspread.Worksheet:
        spreadsheet = service_account.open(spreadsheet_name)
        return spreadsheet.get_worksheet(0)