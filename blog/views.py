# -*- coding:utf8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def home(request):
	text = """<h1>Bienvenue sur mon blog !</h1>
				<p>(vue directe sans template) Home and cakes, cours de pâtisserie à domicile :)</p>"""
	return HttpResponse(text)

def tpl(request):
	return render(request, 'blog/tpl.html', {'current_date' : datetime.now()})