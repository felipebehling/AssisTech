from django.forms import ModelForm
from .models import Relato

class RelatoForm(ModelForm):
    class Meta:
        model = Relato
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RelatoForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})