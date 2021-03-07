from youtube_transcript_api import YouTubeTranscriptApi

from moviepy.editor import VideoFileClip, concatenate_videoclips

import youtube_dl

YOUTUBE_ID = 'alTRvtmWi7k'
OUTPUT_NAME = 'temp_vid.mp4'
COMPILED_NAME = 'ums.mp4'

ydl_opts = {'outtmpl': OUTPUT_NAME}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v='+YOUTUBE_ID])

srt = YouTubeTranscriptApi.get_transcript(YOUTUBE_ID)

i = 1

vid_files = []
clip = VideoFileClip(OUTPUT_NAME, audio=True)
for sub in srt:
    text = sub.get('text')
    if 'um' in text:
        snippet = clip.subclip(sub['start'], sub['start'] + sub['duration'])
        i += 1
        vid_files.append(snippet)
        print("Processing Snippet:", i)

final = concatenate_videoclips(vid_files)
final.write_videofile(COMPILED_NAME)