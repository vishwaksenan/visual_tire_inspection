from django.shortcuts import render
from my_tire_tests import tire_tests


# Create your views here.
def tire_test_view(request):
    return render(request,"index.html",context={})

def ink_test_view(request):
	if(request.method == 'POST' and request.FILES['test_file']):
		test_file = request.FILES['test_file']
		name = request.POST['sample']

	return render(request,"result.html",context={'test_file_name' : test_file,'sample_value':name})