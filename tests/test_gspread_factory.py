from dotenv import dotenv_values
import os
import pytest

current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)

# now we can import the module in the directory.
from sheetRobot import SheetRobot
from gspreadFactory import GspreadFactory
from gspread import Client, Worksheet

class TestGspreadFactory:

    _env_vars = None
    total_tests = 2

    def test_can_authenticate(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        assert isinstance(service_account, Client)

    def test_can_get_worksheet(self):
        self._env_vars = dotenv_values(".env")
        service_account = GspreadFactory.createServiceAccount(path_to_credentials=self._env_vars["CREDENTIALS_JSON_FILE"])
        worksheet = GspreadFactory.getWorkSheet(service_account=service_account, spreadsheet_name=self._env_vars["TEST_SPREADSHEET"])
        assert isinstance(worksheet, Worksheet)