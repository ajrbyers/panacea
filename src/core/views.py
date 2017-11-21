from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages

from core import orcid, logic

def login(request):
	"""
	Presents user with login link to ORCiD.
	"""

	template = 'core/login.html'
	context = {
		'orcid_url': settings.ORCID_URL,
		'orcid_client_id': settings.ORCID_CLIENT_ID,
	}

	return render(request, template, context)


def orcid_login(request):
	"""
	Allows user to login with ORCiD
	"""
	orcid_code = request.GET.get('code', None)

	if orcid_code:
		auth = orcid.retrieve_tokens(orcid_code, request.base_url)
		orcid_id = auth.get('orcid', None)

		if orcid_id:
			user = logic.find_orcid_user(orcid_id)

			if not user:
				user = logic.create_user_account(auth, orcid_id)


			logic.log_user_in(request, user)

		else:
			messages.add_message(request, messages.WARNING, 'An erorr occured during login.')

		return redirect(reverse('login'))

