from django.shortcuts import render
from MONGOAPP.models import * 

''' exceptions handling'''
class PasswordNotMatch(Exception):
	pass

class MongoLogin(CreateView):
    '''Login page'''

    model = user
    fields = ['UserName','Password']
    template_name = "login.html"
    
    def post(self, request):
        LoggedUser = request.POST.get('username')
        password = request.POST.get('Password')
        ValRes = self.ValidateUser(LoggedUser,password)

        if list(ValRes.keys)  == 0:
            request.session['logged_user'] = LoggedUser                              # If user found, create session
            return redirect('/')
        else:
            return HttpResponse(ValRes)                                              # else redirect to create profile page

    def ValidateUser(self,LoggedUser,password):
    	''' Validate user and returns status code and  msg.
    	    101 - Password did not match
    	    100 - user not found
    	    0   - login success '''
        ValidList = {}  
                                                                     # Dictionary contains error code and error message
        try:
            UserProfile.objects.get(UserName=LoggedUser) 
            DbUser = user.objects.get(username = LoggedUser)
            if DBUser.password = password:
            	raise PasswordNotMatch
        except PasswordNotMatch:
            ValidList['101'] = 'Password dint not match'
        except ObjectDoesNotExist: 
            ValidList['100']= 'User not found'
        else:
        	ValidList['0'] = 'Login success'
        finally:
        return ValidList
 
class CreateUserProfile(CreateView):
	model = user 


	
