from django.contrib import admin

# Register your models here.
from .models import Quiz,Student,Question,Options
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy
class QuizAdmin(admin.ModelAdmin):
    list_display=('id','text')


class QuestionAdmin(admin.ModelAdmin):
    list_display =('id','text','Quiz',)


class OptionsAdmin(admin.ModelAdmin):
    list_display=('text','isCorrect','question',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('rollno',)


admin.site.site_header = 'Test Press'

admin.site.register(Quiz,QuizAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Options,OptionsAdmin)

