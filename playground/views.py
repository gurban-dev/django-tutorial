from django.shortcuts import render
from django.http import HttpResponse

def calculate():
  x = 1
  y = 2
  return x

# A view function accepts a request as
# a parameter and returns a response.
# It is a request handler.
def say_hello(request):
  # return HttpResponse('Hello World')

  # x = 1
  x = calculate()

  # The "name" key can be accessed inside
  # the hello.html template.
  return render(request, 'hello.html', {'name': 'Dennis'})