""" view.py: User feeds, create and update user profile."""
__author__ = "sunil"
__date__   = "21 Mar 2016"

from django.shortcuts import render,redirect
from datetime import *
from EXAPP.models import *
from EXAPP.forms import *
from django.views.generic import TemplateView, FormView, CreateView, DetailView
from django.http import HttpResponse
from django.core.exceptions import *

''' exceptions handling'''
class PasswordNotMatch(Exception):
    pass

class DisplayHome(DetailView):
    ''' Display Home page. user can also post status'''
    model = UserFeeds
    template_name = "Home.html"

    # def __init__(request):
    #     print request
        # u = request.session.get('logged_user')
        # if u is None:
        #     return redirect('/login')

    def post(self, request):
            PostMess = request.POST.get('postdata')
            usern = request.session['logged_user']
            date = datetime.now() 
            savepost = UserFeeds(username=usern,user_post = PostMess,date=date)
            # save post shared by user
            savepost.save()                                                          
            return redirect('/')
    
    def get_object(self):
        sorex = UserFeeds.objects.order_by('-date')  
        #Display all users feeds

        # sorex.delete()                                                             
        return sorex


class FeedCreate(CreateView):                             
    '''Create new profile page'''

    model = UserProfile
    template_name = "Profile.html"
    
    def post(self, request):
        NewUserName = request.POST.get('UserName')
        ProfileName = request.POST.get('Name')
        Followers = request.POST.get('user_followers')
        updateUserProfile = UserProfile(UserName = NewUserName,Name = ProfileName,user_followers = Followers)
        SUC = updateUserProfile.save()                                         #Save new profile
        request.session['logged_user'] = NewUserName                           #Create session for logged in user
        return redirect('/')
  

class LoginPage(CreateView):
    '''Login page'''

    model = UserProfile
    fields = ['UserName']
    template_name = "login.html"
    
    def post(self, request):
        LoggedUser = request.POST.get('UserName')
        Found = self.ValidateUser(LoggedUser)
        if Found:
            request.session['logged_user'] = LoggedUser                           # If user found, create session
            return redirect('/')
        else:
            return redirect('/profile')                                           # else redirect to create profile page

    def ValidateUser(self,LoggedUser):
        FoundUser = True
        try:
            UserProfile.objects.get(UserName=LoggedUser) 
        except :
            FoundUser = False
        return FoundUser
        
   










        



