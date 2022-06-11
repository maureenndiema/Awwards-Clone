from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.http import HttpResponseRedirect
from .email import send_welcome_email



# Create your views here.

def signup_view(request):
   if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            name=form.cleaned_data['username']
            email=form.cleaned_data['email']
            
            send_welcome_email(name,email)
            user = authenticate(username=username, password=password)

            login(request, user)


            return redirect('welcome')
        
   else:
        form = SignUpForm()
   return render(request, 'registration/signup.html', {'form': form})

def welcome(request):
   users = User.objects.exclude(id=request.user.id)
   profiles=Profile.objects.all()
   projects=Project.objects.all()
   project_average=Rate.objects.order_by('-score').first()
   ratings=Rate.objects.all()

   params={
       'users':users,
       'profiles':profiles,
       'projects':projects,
       'project_average':project_average,
       'ratings':ratings,
    }
   return render(request,'awwards/index.html',params)

@login_required
def upload_project(request):
      if request.method=='POST':
         form=UploadProjectForm(request.POST, request.FILES)
         if form.is_valid():
            project=form.save(commit=False)
            project.user=request.user
            project.save()
            return redirect('welcome')
      else:
         form=UploadProjectForm()
      return render(request,'awwards/project.html',{'form':form})
 

   
    