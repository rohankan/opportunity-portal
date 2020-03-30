import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from config import SPREADSHEET_ID, SHEET_NAME
from exceptions import NoDataFoundError


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
RANGE_QUERY = f'{SHEET_NAME}!A2:E'


def credentials():
	creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return creds


def sheet():
    service = build('sheets', 'v4', credentials=crendentials())
    sheet = service.spreadsheets()


def form_responses():
	sheet = sheet()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])


    if not values:
    	raise NoDataFoundError()
    else:
    	return values


