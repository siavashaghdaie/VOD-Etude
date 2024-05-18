from django.shortcuts import render, redirect
from .models import Slider, Content
from .forms import sliderForm, messageForm, exclusiveContentForm
from django.utils import timezone
import datetime





def home(request):
    slider = Slider.objects.all()
    target_time = datetime.datetime(2024, 12, 31, 23, 59, 59, tzinfo=timezone.utc)

    context = {'slider':slider, 'target_time': target_time}
    return render(request, 'jjii/home.html', context)

def exclusive(request):
    slider = Slider.objects.all()
    form  = exclusiveContentForm()
    type = 'تولیدات ویژه'
    country = 'ایران'
    if request.method == "POST":
        form = exclusiveContentForm(request.POST, request.FILES)
        if form.is_valid():
            # content = form.save(commit=False)
            # content.type = type
            # content.country = country
            # content.save()
            form.save()
            return redirect('exclusive')


    context = {'slider':slider,'form':form}
    return render(request, 'jjii/exclusive.html', context)



def slideUpdate(request):
    form = sliderForm()
    if request.method == "POST":
        form = sliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
    return render (request, 'jjii/slider-form.html', context)

def message(request):
    form = messageForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect ('home')
    context = {'form':form}
    return render (request, 'jjii/message.html', context)
