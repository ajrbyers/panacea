from django.shortcuts import render

from journal import models, forms

def submit(request):

	form = forms.SubmissionForm()

	if request.POST:
		form = forms.SubmissionForm(request.POST, request.FILES)

		if form.is_valid():
			form.save(request=request)

	template = 'journal/submit.html'
	context = {
		'form': form,
	}

	return render(request, template, context)
