from sheets import get_form_responses


def generate_email():
	responses = get_form_responses()

	print(responses)


generate_email()
