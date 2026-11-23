from django.contrib import admin

# Register your models here.
from .models import Question, Choice


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]})
    ]
    list_display = ["question_text", "pub_date"]
    search_fields = ["question_text"]
    list_filter = ["question_text"]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)