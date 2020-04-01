from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import uuid


CREDENTIALS_FILE = 'drive_credentials.txt'


def drive_instance():
	gauth = GoogleAuth()

	gauth.LoadCredentialsFile(CREDENTIALS_FILE)

	if gauth.credentials is None:
		gauth.LocalWebserverAuth()
	elif gauth.access_token_expired:
	    gauth.Refresh()
	else:
	    gauth.Authorize()

	gauth.SaveCredentialsFile(CREDENTIALS_FILE)

	return GoogleDrive(gauth)


def download_file(drive_id: str,
				  save_name: str):
	drive = drive_instance()
	file_obj = drive.CreateFile({'id': drive_id})
	file_obj.GetContentFile(save_name)

	return file_obj


# Run this command when you need to authenticate locally.
# authenticate()
