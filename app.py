from flask import Flask, render_template, request
from googleapiclient.discovery import build
from pytube import YouTube
import json
from concurrent.futures import ThreadPoolExecutor

app = Flask(__name__)

API_KEYS = ['AIzaSyDdyejQ0N6LkJ0YIFpBmpzQXwV7x1HYlAw',
            'AIzaSyCUDaCZJRNk9MeQh3XEOW2iP-QlS-Ku6vk',
            'AIzaSyCmhpDQnXw6O8sR1uqcCsq4E94Okntk8ig']

def initYoutubeAPI():
    for api_key in API_KEYS:
        youtube = build('youtube', 'v3', developerKey=api_key)
        if youtube:
            return youtube
    return None

youtube = initYoutubeAPI()

class Song:
    def __init__(self, id, title, artist, thumbnail, songUrl, audioUrl):
        self.id = id
        self.title = title
        self.artist = artist
        self.thumbnail = thumbnail
        self.songUrl = songUrl
        self.audioUrl = audioUrl

def getInfoSong(id, audio_url):
    request = youtube.videos().list(part='snippet', id=id).execute()
    songResponse = request['items'][0]['snippet']
    thumbnail_url = songResponse['thumbnails']['medium']['url']
    songUrl = f'https://www.youtube.com/watch?v={id}'
    songInfo = Song(id, songResponse['title'], songResponse['channelTitle'], thumbnail_url, songUrl, audio_url)
    return songInfo

def getAudioUrl(video_id):
    try:
        video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        best_audio = video.streams.filter(only_audio=True).first()
        audio_url = best_audio.url
        return audio_url
    except Exception as e:
        print(f"Error fetching audio URL for video {video_id}: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    songUrl = request.form['txtSongUrl']
    yt = YouTube(songUrl)
    t = yt.streams.filter(only_audio=True)
    t[0].download()
    return render_template("index.html")

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_response = youtube.search().list(
            q=request.form['query'],
            part='snippet',
            type='video',
            videoCategoryId='10',  
            maxResults=3
        ).execute()

        songs = []
        videoIds = []
        for search_result in search_response.get('items', []):
            videoId = search_result['id']['videoId'] 
            videoIds.append(videoId)

        with ThreadPoolExecutor() as executor:
            audioUrls = executor.map(getAudioUrl, videoIds)

        for video_id, audio_url in zip(videoIds, audioUrls):
            song = getInfoSong(video_id, audio_url)
            songs.append(song)

        songs_json = json.dumps([song.__dict__ for song in songs])
        return render_template('index.html', songs=songs_json)

if __name__ == '__main__':
    app.run(debug=True)
