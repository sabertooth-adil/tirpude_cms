from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import random
from django.conf import settings
from django.core.mail import EmailMessage
import base64
import datetime
import traceback
# Create your views here.
