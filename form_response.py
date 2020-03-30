
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
		self.date = datetime.strptime(date, '%m/%d/%y %H:%M:%S')
		self.email = email 
		self.title = title 
		self.description = description
		self.images = images
