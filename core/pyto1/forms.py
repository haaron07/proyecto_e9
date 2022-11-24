from django import forms
from .models import Movies,Series,VideoGames

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = '__all__'

class SerieForm(forms.ModelForm):
    class Meta:
        model=Series
        fields = '__all__'

class GameForm(forms.ModelForm):
    class Meta:
        model=VideoGames
        fields = '__all__'
