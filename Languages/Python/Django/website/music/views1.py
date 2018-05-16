from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from . models import Album,Song
#from django.template import loader

# Create your views here.
def index(request):
	all_albums=Album.objects.all()
	html=''
	#template=loader.get_template('music/index.html')
	context={
		'all_albums':all_albums,
	}
	#return HttpResponse(template.render(context,request))
	return render(request,'music/index.html',context)

def detail(request,album_id):
	#return HttpResponse("<h2>Details for the Album id"+ str(album_id) + "</h2>")
	'''try:
		album=Album.objects.get(pk=album_id)
		return render(request,'music/details.html',{'all_albums':Album.objects.all()})
	except Album.DoesNotExist:
		raise Http404("Album DoesNotExist",{'all_albums':Album.objects.all()})'''
	album=get_object_or_404(Album,pk=album_id)
	return render(request,'music/details.html',{'album':album})

def favorite(request,album_id):
	album=get_object_or_404(Album,pk=album_id)
	try:
		selected_song=album.song_set.get(pk=request.POST['song'])
	except (KeyError,Song.DoesNotExist):
		return render(request,'music/details.html',{'album':album,
			'error_message':"You did not select a valid song",
			})
	else:
		selected_song.is_favorite=True
		selected_song.save()
		return render(request,'music/details.html',{'album':album})

