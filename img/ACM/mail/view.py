import re
from abc import abstractclassmethod
from django.http import request
from django.http.request import HttpHeaders
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect
from club_app.models import Payment, Registered_User,Manager,Reservation,feedback,events,Room,Message
from django.core.mail import send_mail
import datetime 
from datetime import date
import string  
from werkzeug.security import check_password_hash, generate_password_hash
from socket import gaierror
from dateutil.relativedelta import relativedelta
from validate_email_address import validate_email
from django.http import HttpResponse, JsonResponse

from datetime import datetime

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
import random

def snd_mail():
    global rand
    global email
    global mg
    rand= str(random.randint(1000,9999))
    try:
        if mg==1:
            try:
                result = ''.join((random.choice(string.ascii_lowercase) for x in range(6)))
                # result="abcd"
                send_mail(
                    "Room Code",
                    "Your Room Code is Please join with the following roon no :"+ result ,
                    "uetupdates@gmail.com",
                    [email],
                    fail_silently=False

                )
                send_mail(
                    "Live Chat Update",
                    "Following User wants to contact with you "+email +"  Please contact with him with the following Room Code :"+ result ,
                    "uetupdates@gmail.com",
                    ["2019ce21@student.uet.edu.pk"],
                    fail_silently=False

                )
            except :
                return HttpResponse ("Please Login First")
              
    except:
                    send_mail(
                "Email Verification",
                "Your Email Verification Code is :"+ rand ,
                "uetupdates@gmail.com",
                [email],
                fail_silently=False)
