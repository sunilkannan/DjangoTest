from django import forms
 
class PostForm(forms.Form):
    content = forms.CharField(max_length=256)
    created_at = forms.DateTimeField()

class ShareStatus(forms.Form):
	postThought = forms.CharField(max_length = 140)
