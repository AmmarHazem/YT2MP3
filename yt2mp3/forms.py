from django import forms
from django.http import HttpResponse

from mimetypes import guess_type
from pytube import YouTube

from youtubelinks.models import YoutubeLink



class DownloadForm(forms.ModelForm):
    class Meta:
        model = YoutubeLink
        fields = ('url',)
        widgets = {'url' : forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter a Youtube video URL'})}

    def download(self):
        print(self.cleaned_data.get('url'))
        yt = YouTube(self.cleaned_data.get('url'))
        stream = yt.streams.filter(only_audio = True).first()
        buffer = stream.stream_to_buffer()
        response = HttpResponse(content = buffer.getvalue(), content_type = f'{guess_type(stream.default_filename.replace("mp4", "mp3"))}')
        print(stream.default_filename.replace("mp4", "mp3"))
        response['Content-Disposition'] = f'attachment; filename="{stream.default_filename.replace("mp4", "mp3")}"'
        response['Content-Length'] = stream.filesize
        return response
