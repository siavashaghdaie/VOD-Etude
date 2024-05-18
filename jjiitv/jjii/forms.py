from django.forms import ModelForm
from .models import Slider, Message, Content

class sliderForm(ModelForm):
    class Meta:
        model = Slider
        fields = '__all__'

class messageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'


class exclusiveContentForm(ModelForm):
    class Meta:
        model = Content
        exclude = ['type', 'country','genre','imdblink','imdbscore','stars','episode']