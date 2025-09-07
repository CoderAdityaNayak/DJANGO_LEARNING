from django import forms


class NumberListForm(forms.Form):
    numbers=forms.CharField(label="Enter the numbers");       
