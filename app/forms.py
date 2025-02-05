from django import forms
from app.models import *
class ContactForm(forms.Form):
    studentname=forms.CharField()
    age=forms.IntegerField()
    Password=forms.CharField(widget=forms.PasswordInput)
    #couese=forms.ChoiceField(choices=[('Python','PYTHON'),('sql','SQL')])
    gender=forms.ChoiceField(choices=[('male','MALE'),('female','FEMALE')],widget=forms.RadioSelect)
    couese=forms.MultipleChoiceField(choices=[('Python','PYTHON'),('sql','SQL'),('web','WEb')],widget=forms.CheckboxSelectMultiple)

def check(value):
    if value.lower()[0]=='f':
        raise forms.ValidationError('topic name is started in f')

class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[check])





class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()
    email=forms.EmailField()
    remail=forms.EmailField()
    botcatch = forms.CharField(widget=forms.HiddenInput, required=False)
    
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('email is mismatched')
    def clean_botcatch(self):
        bc = self.cleaned_data['botcatch']
        if len(bc) > 0:
            raise forms.ValidationError('bot catched')


class AccessRecordform(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    autor=forms.CharField()
    date=forms.DateField()