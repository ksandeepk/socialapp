from django import forms

class create(forms.Form):
    name=forms.CharField(max_length=50)
    status=forms.ChoiceField(choices=[('job','Job'),('studies','Studies')])
    gender=forms.ChoiceField(choices=[('male','Male'),('female','Female')])
    marital_status=forms.ChoiceField(choices=[('single','Singel'),('in_relation','In_relation')])
    interest_in=forms.ChoiceField(choices=[('male','Male'),('female','Female')])
    email=forms.EmailField(max_length=50)
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=15)
    address=forms.CharField(max_length=200)
    




