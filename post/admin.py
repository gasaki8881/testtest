from django.contrib import admin
from .models import Novel,Chapter,Diary_Category,Diary_Contents

# Register your models here.


admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Diary_Category)
admin.site.register(Diary_Contents)

