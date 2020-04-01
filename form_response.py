from datetime import datetime 
from typing import NamedTuple
from drive import download_file
import base64
import uuid


class Image:
	RESOLUTION = ()
	def __init__(self, 
				 link: str):
		self.link = link 
		self.drive_id = link.split('id=')[1] 
		self.file_name = f'{uuid.uuid1()}.png'
		self.downloaded = False

	@property
	def local_path(self):
		return f'./images/{self.file_name}'
	
	def download_from_drive(self):
		file = download_file(self.drive_id, save_name=self.local_path)
		self.downloaded = True

		return file

	def to_base64(self):
		if not self.downloaded:
			self.download_from_drive()

		with open(self.local_path, 'rb') as image_file:
			# im = Image.open(image_file)
			# im.save("test-600.png", dpi=(600,600))
		    data = base64.b64encode(image_file.read())

		return data.decode('ascii')  # Converting from 'binary string' to regular ascii string.


class FormResponse:
	@staticmethod
	def from_row(row):
		return FormResponse(date=row[0], email=row[1], title=row[2], description=row[3], images=row[4])

	def __init__(self,
				 date: str,
				 email: str,
				 title: str,
				 description: str,
				 images: str):
		self.date = datetime.strptime(date, '%m/%d/%Y %H:%M:%S')
		self.email = email 
		self.title = title 
		self.description = description
		self.images = Image(images)

	def __repr__(self):
		attrs = '\n\t'.join(f'{attr}={value}' for attr, value in self.__dict__.items())
		return f"<{self.__class__.__name__}\n\t{attrs}>"

