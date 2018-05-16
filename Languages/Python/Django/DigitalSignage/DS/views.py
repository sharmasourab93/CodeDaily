from django.shortcuts import render, get_object_or_404
from UI.models import defaultDB	#, MainDB 
# Create your views here.
def index(request):
	"Method to process Image"
	all_images=defaultDB.objects.all()
	return render(request,'DS/display.html',{'all_images':all_images})