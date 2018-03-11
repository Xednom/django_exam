# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView
from .forms import EdiWowForm


# class IndexView(TemplateView):
#    template_name = 'exam/ediwow.html'
#    form_class = EdiWowForm

def post(request):
    a = ['edi', 'wow', 'edi wow']
    for n, i in enumerate(range(17)):
        if i % 3 == 0 and i % 5 == 0:
            print a[2]
        elif i % 3 == 0:
            print a[0]
        elif i % 1 == 0:
            print n
        elif i % 5 == 0:
            print n, a[1]
    return render(request, 'exam/ediwow.html', {'a': a})


def fibo(request, n):
    n = int(n)
    result = fib(n)
    return render_to_response('exam/fibonacci.html', {'n': n, 'r': result})


def fib(n):
    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fib(n-1) + fib(n-2)
