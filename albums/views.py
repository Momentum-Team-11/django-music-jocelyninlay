from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm

# Create your views here.
def list_albums(request):
    album = Album.objects.all()
    return render(request, "albums/list_albums.html", {"album": album})

def album_detail(reuqest, pk):
    album = get_object_or_404(Album, pk=pk)
    form = AlbumForm()
    return render (
        request,
        "albums/album_detail.html",
        {"album": album, "pk":pk, "form": form},
    )

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums")
    return render(request, "albums/add_album.html", {"form": form})

def edit_album(request, contact_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == "GET":
        form = AlbumForm(instance=album)
    else:
        form = AlbumForm(data=request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect(to="list_albums")
    return render(request, "album/edit_album.html", {"form": form, "album": album})

def delete_album(request, pk):
    album = get_objects_or_404(Album, pk=album_pk)
    if request.method == "POST":
        album.delete()
        return redirect(to="list_albums")

    return render(request, "albums/delete_album.html",{"album": album})