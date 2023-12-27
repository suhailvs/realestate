from django.shortcuts import render, redirect
import csv, json
from .models import Property, PropertyGIS
from django.http import JsonResponse
from django.views import View
import json
from django.core.serializers import serialize
# Create your views here.
def home(request):
    """
    latlngs =  [
        {"latlngs": [[10.59, 76.45],[10.5901, 76.4503],[10.5808, 76.4501]], "id": 1},
        {"latlngs": [[10.5903, 76.4502],[10.5901, 76.4504],[10.5808, 76.4501]], "id": 2},
    ];
    """
    latlngs = [{"latlngs": p.latlngs, "id": p.id} for p in Property.objects.all()]
    return render(
        request,
        "map/home.html",
        {"f_latlogs": latlngs, 'propertygis':json.loads(serialize("geojson",PropertyGIS.objects.all()))},
    )


def save_property(request):
    if request.method == "POST":
        Property.objects.create(
            name=request.POST["name"],
            address=request.POST["address"],
            latlngs=json.loads(request.POST["latlngs"]),  # getlist("latlngs[]"),
        )
        return JsonResponse({"success": True})


class PropertyDetail(View):
    """Show Details of a Property"""
    def get(self, request, property):
        property = Property.objects.get(id= property)
        return render(request,'map/property_detail.html',{"property":property})

    def post(self, request, property):
        Property.objects.get(id= property).delete()
        return redirect('/')

