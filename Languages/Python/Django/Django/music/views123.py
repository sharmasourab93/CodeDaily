from django.http import Http404
#from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from .models import Album
# Create your views here.
def index(request):
	all_albums=Album.objects.all()
	#template=loader.get_template('music/index.html')
	context = {
		'all_albums': all_albums
	}
	return render(request,'music/index.html', context)
	#html=''
	#for album in all_albums:
	#	url='/music/'+ str(album.id)+'/'
	#	html+='<a href="'+ url +'">'+album.album_title+'</a><br>'
	#return HttpResponse(template.render(context, request))

def detail(request, album_id):
	album=get_object_or_404(Album, pk=album_id)
	#try:
	#	album=Album.objects.get(pk=album_id)
	#except Album.DoesNotExist:
	#	raise Http404("This Page isn't available at this point")
	#return HttpResponse("<h2>Details for Album id:"+str(album_id)+" </h2>")
	return render(request,'music/details.html', {'album': album})
