import os
import re
from django.shortcuts import render
#from django.urls import reverse_lazy
from django.views import View
from pydub import AudioSegment
from pydub.playback import play
from downloader.youtube_dl_org import youtube_dl


class MusicDl(View):
    def get(self, request):
        context = {
                'message': "input url"
        }
        return render(request, 'get_url.html', context)

    def post(self, request):
        url = request.POST['url']
        message = "Ready to play!"
        context = {
            'message': message
        }
        try:
            youtube_dl.main(['-x', '--audio-format', 'mp3', '-o', 'tmp.mp3', url])
            self._rename_music()
            self._play_music()
        except:
            message = "Unused url."
        return render(request, 'get_url.html', context)

    def _play_music(self):
        tmp = AudioSegment.from_file("/home/tomita/youtube_bg/tmp.mp3")
        play(tmp)
        os.remove("../tmp.mp3")

    def _rename_music(self):
        file_list = os.listdir("../")
        for file_ in file_list:
            if "mp3" in file_:
                os.rename(file_, "tmp.mp3")

