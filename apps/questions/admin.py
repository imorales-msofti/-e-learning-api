from django.contrib import admin

from .models import Question, Answer, ChoiseByQuestion

admin.site.register(Question)
admin.site.register(Answer)

