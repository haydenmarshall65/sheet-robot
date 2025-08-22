import gspread

class SheetRobot:
    # the current spreadsheet to edit with
    _current_cell = "A9"

    def __init__(self, spreadsheet):
        if spreadsheet == None:
            return
        self._find_next_empty_row(spreadsheet=spreadsheet)

    # helper function to set self._current_cell to the next empty field
    @classmethod
    def _find_next_empty_row(self, spreadsheet):
        found_empty_row = False
        cell_number = self._current_cell
        row = int(cell_number.split("A")[1])
        
        while found_empty_row == False:
            cell_number = "A" + str(row)

            val = spreadsheet.acell(cell_number).value

            if val == None or val == "":
                self._current_cell = "A" + str(row)
                found_empty_row = True
            else:
                row += 1
        
        print("(SR) [#] New current cell: " + self._current_cell)

    # fills in the hours on hours log spreadsheets
    @classmethod
    def fill_in_hours(self, spreadsheet, date, desc, hours, optional_row_number=None):
        if optional_row_number != None:
            row_number = optional_row_number
        else:
            row_number = self._current_cell.split("A")[1]

        # update the date work was done
        spreadsheet.update_acell("A" + str(row_number), date)

        # update the desc of work done
        spreadsheet.update_acell("B" + str(row_number), desc)

        # update the hours done
        spreadsheet.update_acell("C" + str(row_number), hours)

        print("(SR) [#] Updated row " + str(row_number) + "!")
        self._find_next_empty_row(spreadsheet=spreadsheet)
    
    # removes data in the given row and sets to active row
    @classmethod
    def delete_hours_log(self, spreadsheet, row_number):
        spreadsheet.update_acell("A" + str(row_number), "")
        spreadsheet.update_acell("B" + str(row_number), "")
        spreadsheet.update_acell("C" + str(row_number), 0.0)
        
        self._current_cell = "A" + str(row_number)
        print("(SR) [#] Deleted row " + str(row_number))
    
    @classmethod
    def read_data_on_row(self, spreadsheet, row_number):
        date = spreadsheet.acell("A" + str(row_number)).value
        desc = spreadsheet.acell("B" + str(row_number)).value
        hours = spreadsheet.acell("C" + str(row_number)).value

        return {"date": date, "desc": desc, "hours": hours}
