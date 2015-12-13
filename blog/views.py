# -*- coding:utf8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
	text = """<h1>Bienvenue sur mon blog !</h1>
				<p>Home and cakes, cours de pâtisserie à domicile :)</p>"""
	return HttpResponse(text)