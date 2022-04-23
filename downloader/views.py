from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from downloader.youtube_dl_org import youtube_dl


#class PlayMusic(viewjkkk)
def use_youtube_dl(request):
    #template_name = 'get_url.html'
    #youtube_dl.main(['-x', '--audio-format', 'mp3', '-o', 'tmp.mp3', 'https://www.youtube.com/watch?v=eKoD2CRr_KA'])
    #print(url)

    #return HttpResponse("hello, world")
    return render(request, 'get_url.html')
