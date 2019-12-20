from django.shortcuts import render,HttpResponse

import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
	return render(request, "index.html")

@csrf_exempt
def uploadfile(request):
	if request.method=="POST":
		file=request.FILES.get("myfile",None)
		path='./files'
		if not file:
			return HttpResponse("no files for upload!")
		destination=open(os.path.join(path,file.name),'wb')
		for chunk in file.chunks():
			destination.write(chunk)
		destination.close()
	return HttpResponse("success")
