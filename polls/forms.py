from django.forms import ModelForm

from .models import Poll

class CreatePollForm(ModelForm):
    class Meta:
        model=Poll
        fields=['question','option_1','option_2','option_3','option_4']