from django.shortcuts import render
import csv,json
from .models import Property
from django.http import JsonResponse

# Create your views here.
def home(request):
    """
    latlngs =  [
        [[10.59, 76.45],[10.5901, 76.4503],[10.5808, 76.4501]],
        [[10.5903, 76.4502],[10.5901, 76.4504],[10.5808, 76.4501]]
    ];
    """
    return render(request, "map/home.html", {"f_latlogs": [p.latlngs for p in Property.objects.all()]})


def save_property(request):
    if request.method == "POST":        
        Property.objects.create(
            name=request.POST["name"],
            address=request.POST["address"],
            latlngs=json.loads(request.POST['latlngs']), # getlist("latlngs[]"),
        )
        return JsonResponse({"success": True})
