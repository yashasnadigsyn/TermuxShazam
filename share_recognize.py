import asyncio
from shazamio import Shazam
import os
import sys,json

url = sys.argv[1]

print(url)

try:
    os.system("mkdir recognize")
except:
    pass

os.system("rm -rf recognize/*")

ans = os.popen(' termux-dialog radio -v "yes,no" -t "Do you want to identify this song within a timestamp?" ').read()
ans = json.loads(ans)["index"]
if ans == 0:
    start = json.loads(os.popen('termux-dialog text -i "hh:mm:ss" -t "Set start time"').read())["text"].strip()
    stop = json.loads(os.popen('termux-dialog text -i "hh:mm:ss" -t "Set end time"').read())["text"].strip()
    timestamp_code = f'--external-downloader ffmpeg --external-downloader-args "ffmpeg_i:-ss {start} -to {stop}" '
    os.system(""" yt-dlp -f "(bestaudio/best)" """+ timestamp_code + '"' + str(url) + '"' + """ -o "recognize/%(title)s.%(ext)s" """)
if ans == 1:
    os.system('yt-dlp -f "(bestaudio/best)" '+ '"' + url +'"'+ ' -o "recognize/%(title)s.%(ext)s"')

filenames = next(os.walk("recognize"), (None, None, []))[2]
song_audio = open('recognize/'+filenames[0], 'rb').read()

async def main():
  shazam = Shazam()
  out = await shazam.recognize_song('recognize/'+filenames[0])
  try:
    print(out)
    song_url = out['track']['hub']['actions'][1]['uri']
    song_name = out['track']['title']
    id = out['matches'][0]['id']
    return [song_name,song_url,id]
  except:
    print("Cannot find the song")
    os.system("termux-notification -c 'Cannot find the song'")
    os.system("rm -rf recognize/*")
    exit()

loop = asyncio.get_event_loop()
song_name = loop.run_until_complete(asyncio.gather(main()))


os.system(f"termux-notification -c '{song_name[0][0]}' --button1 'open track' --button1-action 'termux-open-url https://www.shazam.com/track/{song_name[0][2]}' --button2 'play song' --button2-action 'termux-open-url {song_name[0][1]}' ")
os.system("rm -rf recognize/*")

