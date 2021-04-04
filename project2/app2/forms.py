from django import forms


class EmailForm(forms.Form):

	name = forms.CharField()
	email = forms.EmailField()
	to = forms.CharField()
	comments = forms.CharField(required=False,widget=forms.Textarea)
