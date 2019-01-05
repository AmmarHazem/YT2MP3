from django import forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from pytube import YouTube

from .models import YoutubeLink



class DownloadForm(forms.ModelForm):
    class Meta:
        model = YoutubeLink
        fields = ('url',)
        widgets = {'url' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter a Youtube video URL'})}

    def download(self, req):
        yt_link = self.save(commit = False)
        url = yt_link.url
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(only_audio = True).first()
            buffer = stream.stream_to_buffer()
            filename = stream.default_filename.replace("mp4", "mp3")
        except:
            print('\npytube error\n')
            messages.error(req, 'Server error. Please try agian later.')
            return HttpResponseRedirect('/')
        response = HttpResponse(content = buffer.getvalue())
        response['Content-Type'] = 'audio/mpeg'
        response['Content-Disposition'] = f'attachment; filename="{filename}"'
        print(filename)
        response['Content-Length'] = stream.filesize
        yt_link.title = yt.title
        yt_link.save()
        messages.success(req, f'{yt.title}')
        return response
