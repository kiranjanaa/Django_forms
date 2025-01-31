from django import forms
from app.models import *
class ContactForm(forms.Form):
    studentname=forms.CharField()
    age=forms.IntegerField()
    Password=forms.CharField(widget=forms.PasswordInput)
    #couese=forms.ChoiceField(choices=[('Python','PYTHON'),('sql','SQL')])
    gender=forms.ChoiceField(choices=[('male','MALE'),('female','FEMALE')],widget=forms.RadioSelect)
    couese=forms.MultipleChoiceField(choices=[('Python','PYTHON'),('sql','SQL'),('web','WEb')],widget=forms.CheckboxSelectMultiple)

class TopicForm(forms.Form):
    topic_name=forms.CharField()

class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField()
    url=forms.URLField()

class AccessRecordform(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    autor=forms.CharField()
    date=forms.DateField()