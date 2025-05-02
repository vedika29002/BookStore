from django.contrib import admin
from .models import Books
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display=[
        "userid","bookid","title","author","category","price","qut","dop","photo",
    ]
admin.site.register(Books)