from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ["question_text", "pub_date"]


admin.site.register(Question, QuestionAdmin)
