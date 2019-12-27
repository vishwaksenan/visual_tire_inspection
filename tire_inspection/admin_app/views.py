"""Myview"""
from django.shortcuts import render
from admin_app.auto_tire_test import tire_testing
from django.core.files.storage import FileSystemStorage

# Create your views here.
def tire_test_view(request):
	"""
	hello
	"""
	return render(request,"index.html",context={})


def ink_test_view(request):
	"""
	Ink test
	"""
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		fss = FileSystemStorage()
		name = fss.save(test_file.name,test_file)
		test = tire_testing()
		result_of_ink_test = test.ink_test(fss.path(name))
		data = {}
		data['result'] = result_of_ink_test
	return render(request,"result.html",context=data)

def scorch_test_view(request):
	"""
	Scorch test
	"""
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		fss = FileSystemStorage()
		name = fss.save(test_file.name,test_file)
		test = tire_testing()
		result_of_ink_test = test.scorch_test(fss.path(name))
		data = {}
		data['result'] = result_of_ink_test
	return render(request,"result.html",context=data)
