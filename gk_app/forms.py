from django import forms
from gk_app.models import DateWiseGK,CategoryWiseGK

class DateWiseGKForm(forms.ModelForm):
    class Meta:
        model = DateWiseGK
        fields = "__all__"
class CategoryWiseGKForm(forms.ModelForm):
    class Meta:
        model =CategoryWiseGK
        fields = "__all__"