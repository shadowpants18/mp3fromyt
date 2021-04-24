import pytube
import moviepy
from moviepy import editor
import os
import sys

link = sys.argv[1] if sys.argv[1] else "https://www.youtube.com/playlist?list=PLaP23oJapSUmi1AYLTIlq8L_AigHIie9F"
p = pytube.Playlist(link)
print(f'downloading : {p.title}')
for i, video_url in enumerate(p.video_urls):
  try:
    video = pytube.YouTube(video_url)
  except pytube.exceptions.VideoUnavailable:
    pass
  else:       
    try:
      print(video.title)
      videoTitle = video.title.replace("/", "-")
      if f"{videoTitle}.mp3" not in os.listdir('audio') and f"{videoTitle}.mp3" not in os.listdir('newAudio'):
        video.streams.first().download(output_path = 'songs', filename = f'{i}')
        videoFile = editor.VideoFileClip(f'songs/{i}.mp4')
        audioClip = videoFile.audio
        audioClip.write_audiofile(f'newAudio/{videoTitle}.mp3')
        audioClip.close()
        videoFile.close()
        os.remove(f'songs/{i}.mp4')
    except:
      pass
print("Done!")