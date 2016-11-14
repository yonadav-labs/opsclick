import os
import hashlib
import base64
import mimetypes

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
from django.views.decorators.csrf import csrf_exempt

from sign_up.models import *


genre_key_code = {
    'webinar': '@3$',
    'reference': '%7!',
    'resume': '6^&'
}

def platform(request):
    return render(request, 'platform.html')


@csrf_exempt
def webinar_sign_up(request):
    """
    view for webinar, reference, resume
    """
    first_name, last_name, email, genre = parse_request(request)
    user = OpsUser.objects.filter(email=email, genre=genre).first()
    if user:
        if user.first_name == first_name and user.last_name == last_name:
            return HttpResponse('You are already registered!', 200)        
        return HttpResponse('The email is already used!', status=405)
    else:
        # verification key
        key = base64.b64encode(hashlib.new('md5').digest())
        # set genre in the key
        key = "{}{}{}".format(key[:5], genre_key_code[genre], key[5:])

        user = OpsUser.objects.create(first_name=first_name, last_name=last_name, 
                               genre=genre, email=email, vkey=key)

        if genre == 'resume':
            user.experience = request.POST.get('experience')
            user.zipcode = request.POST.get('zipcode')
            user.phone = request.POST.get('phone')
            user.resume = request.FILES.get('resume')
            user.save()

        # send verification email
        email_subject = 'Please Confirm Your E-mail Address'

        email_body = 'Dear Customer.\n\nYou are receiving this e-mail because '+\
                     'user {} at www.opsclick.com has given yours as '+\
                     'an e-mail address to connect their account.\n'+\
                     'To confirm this is correct, go to http://localhost:8000/verify/{}/\n\n'+\
                     'Thank you!\n'+\
                     'www.opsclick.com'
        email_body = email_body.format(first_name+' '+last_name, key)

        send_mail(email_subject, email_body, settings.DEFAULT_FROM_EMAIL, [email], 
                  fail_silently=False)        

        return HttpResponse('We have sent an e-mail to you for verification. ' + 
                            'Follow the link provided to finalize the signup ' +
                            'process. Please contact us if you do not receive ' +
                            'it within a few minutes.', 201)


def verify_webinar(request, key):
    """
    email verification for webinar, reference, resume
    """
    user = OpsUser.objects.filter(vkey=key).first()
    if user:        
        user.verified = True
        user.save()

        if key[5:8] in [genre_key_code['webinar'], genre_key_code['resume']]: # webinar
            return HttpResponse('You are successfully signed up!\n Thank you.')
        else:            
            path = smart_str(settings.PROJECT_ROOT+'/OpsClick_QuickReferenceGuide.pdf')
            wrapper = FileWrapper( open( path, "r" ) )
            content_type = mimetypes.guess_type( path )[0]

            response = HttpResponse(wrapper, content_type = content_type)
            response['Content-Length'] = os.path.getsize( path ) # not FileField instance
            response['Content-Disposition'] = 'attachment; filename=%s/' % smart_str( os.path.basename( path ) ) # same here

            return response
    return HttpResponse('Wrong verification key!')


def parse_request(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    genre = request.POST.get('genre')
    return first_name, last_name, email, genre


def submit_resume(request):
    if request.method == 'GET':
        return render(request, 'submit_resume.html')
