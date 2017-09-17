from __future__ import unicode_literals
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
import os
import youtube_dl

ytd_command = Subcommand('youtube', help='Auto download from a specified youtube link')

def youtubedl(lib, opts, args):
    #print(args)
    ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '~/audio.webm',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(args)
    os.system( 'beet import -m ~/audio.mp3' )
ytd_command.func = youtubedl

class ytd(BeetsPlugin):
    def commands(self):
        return[ytd_command]
