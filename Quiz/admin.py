from django.contrib import admin
from .models import Quiz, Score, Profile

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.admin import UserAdmin






admin.site.register(Quiz)
admin.site.register(Profile)

