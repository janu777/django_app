from django.shortcuts import render

# Create your views here.

# The view function takes one argument, request. This object is an HttpRequestObject that 
# is created whenever a page is loaded. 
# It contains information about the request, such as the method, 
# which can take several values including GET and POST.

def hello_world(request):
	return render(request,'hello_world.html',{})
