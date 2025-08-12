# Sheet Robot

## How to Run this Project

To begin, you need a Google API service account with credentials in order to edit and create google sheets. Begin by going to Google Cloud Console and enabling the Google Drive APIs and Google Sheet APIs. After that, create a service account and name it `sheet-robot`. Give it the permissions "Editor" and "Service Account Token Creator". Then, go to the Service Account's page and go to the "Keys" tab and select "Create New Key". When prompted, select "JSON", and it will download the JSON file. Move it to this project directory and add the name of the file under the .env variable "CREDENTIALS_JSON_FILE"

After this is done, set up your python virtual environment with
```bash
python3 -m venv <venv name>
```
and run
```bash
pip install -r requirements.txt
```