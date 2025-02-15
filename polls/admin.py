from django.contrib import admin
from .models import Choice, Question

# Inline model for Choice inside Question
class ChoiceInline(admin.TabularInline):  # TabularInline gives a table-like layout
    model = Choice
    extra = 3  # Allows adding 3 extra choice fields

# Customizing the Question model in the Admin panel
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]  # Adds choices inside question form
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

# Registering Question with the customized admin
admin.site.register(Question, QuestionAdmin)
