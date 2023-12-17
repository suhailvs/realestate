from django.shortcuts import render, redirect
from django.views import View


from map.models import Property
# Create your views here.
class PropertyDetail(View):
    """Show Details of a Student"""
    def get(self, request, property):
        property = Property.objects.get(id= property)
        return render(request,'property/property_detail.html',{"property":property})

    def post(self, request, property):
        Property.objects.get(id= property).delete()
        return redirect('/')