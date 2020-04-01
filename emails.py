from sheets import get_form_responses
from html_builder import render_template


def generate_email():
	responses = get_form_responses()

	opportunities = [
		{
			'title': response.title,
			'description': response.description,
			'image_base64': response.images.to_base64()
		}
		for response in responses
	]

	print(f'Total of {len(responses)} responses:')
	for response in responses:
		print('- ', response.title)

	html = render_template(
		title='DYLN Opportunity Portal:', 
		subtitle='2020 Test Email',
		opportunities=opportunities
	)

	with open('output.html', 'w') as f:
		f.write(html)

	print('Succesfully generated email from Google Forms data!')


if __name__ == '__main__':
	generate_email()
