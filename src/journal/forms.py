from django import forms

from django_summernote.widgets import SummernoteWidget

from journal import models

class SubmissionForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(SubmissionForm, self).__init__(*args, **kwargs)
		self.fields['subtitle'].required = False
		self.fields['manuscript_file'].required = False

	def save(self, commit=True, request=None):
		article = super(SubmissionForm, self).save(commit=False)
		article.owner = request.user

		if commit:
			article.save()

		return article


	class Meta:
		model = models.Article
		exclude = ('owner', 'authors', 'date_submitted', 'date_published', 'open_for_comments', 'doi')
		widgets = {
			'abstract': SummernoteWidget(),
		}


