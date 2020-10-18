from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import Context, loader
from models import Student, Quiz, Question, Options
from django.shortcuts import render_to_response
import os

# Create your views here.
def saveRollno(rolln):
   data=Student()
   data.rollno=rolln
   data.save()


def login(request):
    path = ".\quizapplication\html\Login.html"
    pass

def getQuizlist(request):
    results=[]
    for i in  Quiz.objects.all():
       results.append(translateQuiz(i))
    return JsonResponse({"result": results})


def translateQuiz(quize):
    print "quize: " + str(quize)
    ques = Question.objects.filter(Quiz=quize.id)
    print "ques: "+str(ques)
    return{"quize": quize.text, "ques": translateQues(ques)}

def translateQues(ques):
    results=[]
    for q in ques:
        options = Options.objects.filter(question=q.id)
        results.append({'id':q.id,'text':q.text,'Options':translateOptions(options)})
    return results

def translateOptions(options):
    results=[]
    for op in options:
        results.append({'text':op.text,'isCorrect':op.isCorrect})
    return results