from django.contrib import admin
from quiz_app.models import Feedback, Participant, Answer, Question, Quiz, Tag, Category

# Register your models here.

admin.site.register(Feedback)
admin.site.register(Participant)
admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Tag)
admin.site.register(Category)
