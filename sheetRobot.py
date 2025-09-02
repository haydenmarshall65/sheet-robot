import gspread
from gspread import Spreadsheet

class SheetRobot:
    # the current spreadsheet to edit with
    _current_cell = "A9"

    def __init__(self, spreadsheet: Spreadsheet):
        if spreadsheet == None:
            return
        print("(SR) [#] New Sheet Robot initialized!")
        self._find_next_empty_row(spreadsheet=spreadsheet)

    # helper function to set self._current_cell to the next empty field
    @classmethod
    def _find_next_empty_row(self, spreadsheet: Spreadsheet):
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
    def fill_in_hours(self, spreadsheet: Spreadsheet, date: str, desc: str, hours: float, optional_row_number:int=None):
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
    def delete_hours_log(self, spreadsheet: Spreadsheet, row_number:int):
        spreadsheet.update_acell("A" + str(row_number), "")
        spreadsheet.update_acell("B" + str(row_number), "")
        spreadsheet.update_acell("C" + str(row_number), 0.0)
        
        self._current_cell = "A" + str(row_number)
        print("(SR) [#] Deleted row " + str(row_number))
    
    @classmethod
    def read_data_on_row(self, spreadsheet: Spreadsheet, row_number: int) -> dict[str, str | float]:
        date = spreadsheet.acell("A" + str(row_number)).value
        if date == None:
            date = "Empty"

        desc = spreadsheet.acell("B" + str(row_number)).value
        if desc == None:
            desc = "Empty"

        hours = spreadsheet.acell("C" + str(row_number)).value
        if hours == None:
            hours = "Empty"

        return {"date": date, "desc": desc, "hours": hours}

    @classmethod
    def print_row_data(self, data: list, include_header:bool = True):
        padding = 2
        date = data[0]
        desc = data[1]
        hours = data[2]

        dateLength = len(date)
        dateDiff = dateLength - 4 + padding # 4 because "DATE" is 4 characters

        header = "DATE" + (" " * dateDiff)
        text = str(date) + "  "

        descLength = len(desc)
        descDiff = descLength - 5 + padding # 5 because " DESC" is 5 characters
        
        header += "| DESC" + (" " * descDiff)
        text += "| " + str(desc) + " "

        # not worried about header and text difference because this is the end of the line
        header += "| HOURS"
        text += "| " + str(hours) + " "

        if include_header:
            print(header)
        print(text)

    @classmethod
    def print_all_data(self, spreadsheet: Spreadsheet):
        still_has_data = True
        first_row = 9
        last_row = int(self._current_cell.split("A")[1])

        data = spreadsheet.get_all_values()
        
        for i in range(first_row, last_row - 1):
            include_header = (i == first_row)
            self.print_row_data(data=data[i], include_header=include_header)

