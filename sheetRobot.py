import gspread

class SheetRobot:
    # the current spreadsheet to edit with
    _current_cell = "A9"

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
    def fill_in_hours(self, spreadsheet, date, desc, hours, optional_row_number=None):
        if optional_row_number:
            row_number = optional_row_number
        else:
            row_number = int(self._current_cell[1])

        # update the date work was done
        spreadsheet.update("A" + str(row_number), date)

        # update the desc of work done
        spreadsheet.update("B" + str(row_number), desc)

        # update the hours done
        spreadsheet.update("C" + str(row_number), hours)
    
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
