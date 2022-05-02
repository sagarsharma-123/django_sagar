from webbrowser import get
from django.http import HttpResponse
from django.shortcuts import render
from requests import request
import random

def indexv(request):
    return render(request,"index.html")

def aboutv(request):
    return render(request,"about.html")

def opt1v(request):
    return render(request,"opt1.html")

def opt2v(request):
    return render(request,"opt2.html")

def calculatorv(request):
    a=''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('number1'))
            n2=eval(request.POST.get('number2'))
            opr=request.POST.get('opr')
            
            if opr=="+":
                a=n1+n2
            elif opr=="-":
                a=n1-n2
            elif opr=="*":
                a=n1*n2
            elif opr=="/":
                a=n1/n2
    except:
        pass

    return render(request,"calculator.html",{'a':a})

def NumberGuessingv(request):
    n1=''
    n2=''
    c=''
    try:
        if request.method=="POST":
            n1=int(request.POST.get('N1'))
            n2=random.randint(0,9)
            print(n1)
            print(n2)
        if (n1=='' & n2==''):
            c="you wonnn"
        elif (n1!=n2):
            c="you lose"
        else:
            c="noooo"
    except:
        pass
    return render(request,"NumberGuessing.html",{'p2':n2,'p1':n1,'c':c})