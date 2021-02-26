from django import forms
branch_list=(('Cse','Cse'),('Ece','Ece'),('Mech','Mech'),('Eee','Eee'),('Civil','Civil'))
class Toorder(forms.Form):
    clgid= forms.CharField(max_length=100)
    bookid = forms.CharField(max_length=100)
    branch = forms.ChoiceField(choices=branch_list)

