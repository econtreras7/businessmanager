from catalog.models import Service
from django.shortcuts import render
# Create your views here.




def index(request):

    service = Service.objects.all().count()



    context={
    'num_services':service,
    }

    return render(request,'index.html',context=context)