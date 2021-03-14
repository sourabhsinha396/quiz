from django.contrib import admin

# Register your models here.
from .models import User, Subject, Quiz, Question, Answer, Student, TakenQuiz

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Quiz)

admin.site.register(Answer)
admin.site.register(Student)
admin.site.register(TakenQuiz)


class Answer(admin.TabularInline):
    model = Answer
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
	raw_id_fields = ['quiz']
	inlines       = [Answer]
	# made it raw_id_field because when number of quiz inc.
	#it becomes difficult to find a quiz

admin.site.register(Question,QuestionAdmin)