from googleapiclient.discovery import build
import requests
url = "https://www.youtube.com/channel/UCrcZf8dGWj-7SbHu2ZD5i7g/videos?pbjreload=10"
page = requests.get(url).content
#print(page)
data = str(page).split(' ')
item = 'href="/watch?'
ti='title='
vids = [line.replace('href="', 'youtube.com') for line in data if item in line]
#print(vids[0])

api_key = "AIzaSyBRFRVG_Y6Ed6TmQqPxWI70k7VgME1wMVk"

youtube = build('youtube', 'v3', developerKey=api_key,cache_discovery=False)
req = youtube.search().list(part='contents',
                            q='Bodhi AI',
                            type='video',
                            maxResults=50)
# res = req.execute()
# print(len(res['items']))
# for item in res['items']:
#     print(item['snippet']['title'])
#     print(item['snippet']['thumbnails']['default'])
#     print(item['snippet'])


def get_channel_videos(channel_id):
    # get Uploads playlist id
    res = youtube.channels().list(id=channel_id,
                                  part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    videos = []
    next_page_token = None

    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id,
                                           part='snippet',
                                           maxResults=50,
                                           pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')

        if next_page_token is None:
            break

    return videos
videos = get_channel_videos('UCrcZf8dGWj-7SbHu2ZD5i7g')
print(len(videos))
published_list=[]
title_list=[]
thumbnail_list=[]
video_id=[]
for video in videos:
    #print(video['snippet'])
    publishedA_time=video['snippet']['publishedAt']
    published_list.append(publishedA_time)
    #print(video['snippet']['title'])
    title=video['snippet']['title']
    title_list.append(title)
    #print(video['snippet']['thumbnails']['default']['url'])
    thumbnail_link=video['snippet']['thumbnails']['default']['url']
    thumbnail_list.append(thumbnail_link)
    id = video['snippet']['resourceId']['videoId']
    #print(id)
    video_id.append(id)
video_url=[]
for i in video_id:
    v="https://www.youtube.com/embed/" +i
    video_url.append(v)
    #print(v)
video_content=list(zip(title_list,video_url,thumbnail_list,published_list))
# print(title_list[0])
# print(video_url[0])
for content in video_content:
    print(content[0])
    print(content[1])
