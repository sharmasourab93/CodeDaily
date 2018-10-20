#A Video Scheduler
import pafy
url="https://www.youtube.com/watch?v=DelhLppPSxY"
video=pafy.new(url)
"""streams=video.streams
print(video.title)
print(video.length)
#print(video.description)
best=video.getbest()
print(best.resolution)
bestaudio=video.getbestaudio()
print("Best Audio Stream",bestaudio)
streams=video.streams
allstreams=video.allstreams
for s in streams:
    print(s)
for l in allstreams:
    print(l.mediatype,l.extension,l.quality)"""

vstreams=video.streams
print(video.title,video.length,video.author,video.category,video.)
astreams=video.audiostreams
for i in vstreams:
    print(i)
print(astreams)
print(vstreams)
