# Sheet Robot

## How to Run this Project

To begin, you need a Google API service account with credentials in order to edit and create google sheets. Begin by going to Google Cloud Console and enabling the Google Drive APIs and Google Sheet APIs. After that, create a service account and name it `sheet-robot`. Give it the permissions "Editor" and "Service Account Token Creator". Then, go to the Service Account's page and go to the "Keys" tab and select "Create New Key". When prompted, select "JSON", and it will download the JSON file. Move it to this project directory and add the name of the file under the .env variable "CREDENTIALS_JSON_FILE"

After this is done, set up your python virtual environment with
```bash
python3 -m venv <venv-name>
```
and run
```bash
pip install -r requirements.txt
```

## To install as a single executable:

Enable your python virtual env by using:

```bash
source <venv-name>/bin/activate
# if on windows
<venv-name>/bin/activate
```

Then, run the build command:
```bash
./build.sh
```

If all works, you should be able to just run:
```bash
./bin/sheet-robot
```

If you want, you can also add the sheet-robot to your path by adding the following line to your .bashrc:
```bashrc
export PATH=$PATH:$HOME/projects/sheet-robot/bin