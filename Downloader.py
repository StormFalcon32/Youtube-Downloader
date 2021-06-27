import pytube
from time import sleep

playlist = pytube.Playlist('https://www.youtube.com/watch?v=bfw5f4cnRcc&list=PLFITtxHy9Gk4gsWyU7uCVHK2Xp6W4pW35')
ind = 0
start_ind = 0
for video in playlist.videos:
    ind += 1
    if ind >= start_ind:
        print('Downloading {} {} / {}'.format(video.title, ind, len(playlist.videos)))
        video.streams.first().download('C:/Data/Python/Youtube-Downloader/Downloads/')
        sleep(1)