from django import forms

class inputform(forms.Form):
    time = forms.IntegerField(min_value=1, max_value=100000, label="Enter the expected Time of the loan [In Years]")
    amount = forms.IntegerField(min_value=1, label="Enter the Principal Amount")
    rate=forms.IntegerField(min_value=1,label="Enter the Rate of Intrest")
