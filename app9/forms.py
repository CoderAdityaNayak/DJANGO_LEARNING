from django import forms 
class toolkit(forms.Form):
    num1=forms.IntegerField(min_value=1,max_value=10,label="PLEASE ENTER THE 1ST NUMBER")
    num2=forms.IntegerField(min_value=1,max_value=10,label="PLEASE ENTER THE 2ND NUMBER")