from pytube import YouTube

def DownloadMP4(link):

    try:
        YTLink = YouTube(link)
        YTLink = YTLink.streams.get_highest_resolution()
        YTLink.download(filename=f"{YTLink.title}.mp4")
    except:
        print("Download Failed")
        return 0
    
    return 1

def DownloadMP3(link):

    try:
        YTLink = YouTube(link)
        audio = YTLink.streams.filter(only_audio=True).first()
        audio.download(filename=f"{YTLink.title}.mp3")
    except:
        print("Download Failed")
        return 0
    
    return 1
