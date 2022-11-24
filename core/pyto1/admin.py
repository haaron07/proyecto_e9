from django.contrib import admin
from .models import VideoGames,Movies,Series
# Register your models here.
admin.site.register(VideoGames)
admin.site.register(Movies)
admin.site.register(Series)