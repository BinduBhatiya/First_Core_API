from django.shortcuts import render
from .models import employee
from .serializers import employeeserializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

# Create your views here.
def empdetails(request,id):
    emp = employee.objects.get(id=id)
    serializer = employeeserializer(emp)
    print(serializer)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
def emplist(request):
    emp = employee.objects.all()
    serializer = employeeserializer(emp, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')