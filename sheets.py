import pickle
import os.path
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from config import SPREADSHEET_ID, SHEET_NAME, SHEET_RANGE
from form_response import FormResponse
from exceptions import NoDataFoundError


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
RANGE_QUERY = f'{SHEET_NAME}!{SHEET_RANGE}'


def get_credentials():
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


def get_sheet():
	service = build('sheets', 'v4', credentials=get_credentials())
	sheet = service.spreadsheets()

	return sheet


def get_form_responses():
	sheet = get_sheet()
	result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_QUERY).execute()
	rows = result.get('values', [])

	if not rows:
		raise NoDataFoundError()

	return [FormResponse.from_row(x) for x in rows]

