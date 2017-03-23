from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
import textwrap

# Create your views here.
class HomePageView(View):
    def dispatch(self, request, *args, **kwargs):
        response_text = textwrap.dedent('''\
        <html>
        <head>
            <title>Greetings to the world</title>
        </head>
        <body>
            <h1>Greetings to the world</h1>
            <p>Hello World</p>
        </body>
        </html>
        ''')
        return HttpResponse(response_text)