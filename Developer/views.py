from django.shortcuts import render
from Skill.models import Skill
from Developer.models import Developer
# Create your views here.

def home(request):
    skills =  Skill.objects.all()
    developer =  Developer.objects.all()
    
    return render(request, 'base.html'
                  ,
                  {'skills': skills,
                   "developer":developer,                 
                    
                   })

