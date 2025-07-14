from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Home, About, Skill, Project
from .forms import ContactForm

def home_view(request):
    home = Home.objects.first()
    about_list = About.objects.all()
    skills = Skill.objects.all()
    return render(request, 'home.html', {
        'home': home,
        'about_list': about_list,
        'skills': skills,
    })

def projects_view(request):
    projects = Project.objects.all()
    return render(request, 'projects.html', {'projects': projects})

def contact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправлено!')
            return redirect('contact')
    return render(request, 'contact.html', {'form': form})
