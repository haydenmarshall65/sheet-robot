import gspread
from dotenv import dotenv_values

class SheetRobot:
    # the current spreadsheet to edit with
    _current_spreadsheet = None
    _service_account = None
    _current_cell = "A9"

    # constructor, takes in path to credentials and should login via gspread
    def __init__(self, path_to_credentials):
        self._service_account = gspread.service_account(filename=path_to_credentials)
    
    # use this to modify the values of the class to the current spreadsheet so it can be easily edited
    # using the helper functions below
    @classmethod
    def set_current_spreadsheet(self, spreadsheet_name):
        # get the current spreadsheet and correct sheet
        spreadsheet = self._service_account.open(spreadsheet_name)
        self._current_spreadsheet = spreadsheet.get_worksheet(0)

        # now check for first empty row in case edited before
        self._find_next_empty_row()
    
    # helper function to set self._current_cell to the next empty field
    @classmethod
    def _find_next_empty_row(self):
        found_empty_row = False
        cell_number = self._current_cell
        row = int(cell_number[1])
        
        while found_empty_row == False:
            cell_number = "A" + str(row)

            val = self._current_spreadsheet.acell(row).value

            if val == None or val == "":
                self._current_cell = "A" + str(row)
                found_empty_row = True
            else:
                row += 1

    # fills in the hours on hours log spreadsheets
    @classmethod
    def fill_in_hours(self, date, desc, hours, optional_row_number):
        if optional_row_number:
            row_number = optional_row_number
        else:
            row_number = int(self._current_cell[1])

        # update the date work was done
        self._current_spreadsheet.update("A" + row_number, date)

        # update the desc of work done
        self._current_spreadsheet.update("B" + str(row_number), desc)

        # update the hours done
        self._current_spreadsheet.update("C" + str(row_number), hours)

        # quickly update the next empty row
        self._find_next_empty_row()
    
    # removes data in the given row and sets to active row
    @classmethod
    def delete_hours_log(self, row_number):
        self._current_spreadsheet.update("A" + str(row_number), "")
        self._current_spreadsheet.update("B" + str(row_number), "")
        self._current_spreadsheet.update("C" + str(row_number), 0.0)
        
        self._current_cell = "A" + str(row_number)
    
    # creates a new sheet and share it with the USER_EMAIL provided in .env
    @classmethod
    def create_new_sheet(self, spreadsheet_name, user_email):
        new_sheet = self._service_account.create(title=spreadsheet_name)
        
        new_sheet.share(email_address=user_email, perm_type="user", role="writer")
    
    # creates a new sheet, shares it with USER_EMAIl, and sets it as the current sheet
    @classmethod
    def create_new_sheet_and_set_current(self, spreadsheet_name, user_email):
        self.create_new_sheet(spreadsheet_name=spreadsheet_name, user_email=user_email)
        self.set_current_spreadsheet(spreadsheet_name=spreadsheet_name)
