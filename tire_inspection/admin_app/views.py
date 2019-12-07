from django.shortcuts import render

# Create your views here.
def tire_test_view(request):
    return render(request,"index.html",context={})