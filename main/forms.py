from django import forms


class Bajaderka(forms.Form):
    nazwa_lokalu = forms.CharField(max_length=150, required=True)
    ocena = forms.FloatField(max_value=10, required=True)
    adres = forms.URLField(required=False)


    
    
