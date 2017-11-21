from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages


def find_orcid_user(orcid_id):
	try:
		return User.objects.get(username=orcid_id)
	except User.DoesNotExist:
		return None


def create_user_account(auth, orcid_id):
	
	name_split = auth.get('name').split(' ')

	first_name = name_split[0]
	last_name = name_split[-1]

	new_user = User.objects.create(username=orcid_id, first_name=first_name, last_name=last_name)

	return new_user


def log_user_in(request, user):
	user.backend = 'django.contrib.auth.backends.ModelBackend'
	login(request, user)

	if request.user and request.user.is_authenticated:
		messages.add_message(request, messages.INFO, 'Login successful')
