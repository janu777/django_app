from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):	
	projects = Project.objects.all() # a query which is a command that
	#allows you to create, retrieve, update, or delete objects in your database. 
	#Here all objects in the projects table are being retrieved
	context = {
	'projects': projects
	}
	return render(request,'project_index.html',context)

def project_detail(request,pk):
	projects = Project.objects.get(pk=pk)#this query 
	#retrieves the project with primary key pk
	# equal to that in the function
	context = {
	'Project': projects
	}
	return render(request, 'project_detail.html',context)
