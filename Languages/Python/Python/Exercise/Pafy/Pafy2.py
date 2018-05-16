import pafy 

url=['https://www.youtube.com/watch?v=WS4Mev_vRAc']
for i in range(len(url)):
    video=pafy.new(url[i])
    s=video.getbestaudio()
    print("\nDownloading "+str(video.title))
    #song=s.download("C:\\Users\\ESOUSSH\\Downloads\\Personal\Github\Practices\\Languages\\Python\\RoughWork\\Pafy\\"+str(i)+".webm",quiet=True)
    song=s.download(quiet=True)
    print(str(video.title)+" downloaded.")
