from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from downloader.youtube_dl_org import youtube_dl


class PlayMusic(View):
    def get(self, request):
        context = {
                'message': "backgroundで再生したいyoutubeのurlを入力"
        }
        return render(request, 'get_url.html', context)
    def post(self, request):
        context = {
                'message': "Downloading ..."
        }
        print(request.POST['url'])
        return render(request, 'get_url.html', context)
        #url = request.POST['url']
        #print(url)
        #youtube_dl.main(['-x', '--audio-format', 'mp3', '-o', 'tmp.mp3', url])
#def use_youtube_dl(request):
    #template_name = 'get_url.html'
    #print(url)

    #return HttpResponse("hello, world")
