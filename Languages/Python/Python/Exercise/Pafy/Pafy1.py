#A Kaltura Video Scheduler
import pafy
url="https://play.ericsson.net/media/t/0_yz2e6mjy"
video=pafy.new(url)
streams=video.streams
print(video.title)
print(video.length)
print(video.description)
best=video.getbest()
print(best.url)
#bestaudio=video.getbestaudio()
streams=video.streams
allstreams=video.allstreams
for s in streams:
    print(s)
for l in allstreams:
    print(l.mediatype,l.extension,l.quality)
