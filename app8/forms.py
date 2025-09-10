from django import forms

class inputform(forms.Form):
    name=forms.CharField(max_length=40,label="Enter your name")
    p=forms.IntegerField(min_value=1000,max_value=100000,label="Enter Principal in Rs")
    t=forms.IntegerField(min_value=1,max_value=5,label="Enter time in years")
    r=forms.IntegerField(min_value=4,max_value=12,label="Enter rate of interest in %")
