from django import forms

class ItemForm(forms.Form):
    id=forms.IntegerField()
    item_name = forms.CharField(max_length=60)
    item_price = forms.FloatField()
    unit_per_item = forms.FloatField()
    description = forms.CharField(widget=forms.Textarea())

class itemId(forms.Form):
    question_id=forms.IntegerField()