from django import forms  
class inputform(forms.Form):
    input1=forms.IntegerField(min_value=1,max_value=10000,label="ENTER THE FIRST NUMBER:")
    input2=forms.IntegerField(min_value=1,max_value=10000,label="ENTER THE SECOND NUMBER:")
    