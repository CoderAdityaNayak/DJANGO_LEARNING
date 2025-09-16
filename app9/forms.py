from django import forms 
class toolkit(forms.Form):
    num1=forms.IntegerField(min_value=1,max_value=10,label="PLEASE ENTER 1ST NUMBER")
    num2=forms.IntegerField(min_value=1,max_value=10,label="PLEASE ENTER 2ND NUMBER")