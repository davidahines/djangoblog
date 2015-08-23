from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class ContactForm(forms.Form):
        contact_name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class':'basic_input'}))
        contact_email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(attrs={'class':'basic_input'}))
        contact_subject = forms.CharField(label='Subject', max_length=100, widget=forms.TextInput(attrs={'class':'basic_input'}))
        contact_message = forms.CharField(label='Message', max_length=5000, widget=forms.Textarea(attrs={'class':'basic_input'}))
