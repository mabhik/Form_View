from django.shortcuts import render
from django.views.generic import FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class studentform(FormView):
    template_name='studentform.html'
    form_class=student

    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))

class college_data(FormView):
    template_name='college_data'
    form_class=data

    def form_valid(self, form):
        form.save()
        return HttpResponse('college data inserted successfully')