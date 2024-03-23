from flask import Flask, render_template, request
from googleapiclient.discovery import build
from pytube import YouTube


app = Flask(__name__)

# Thay đổi 'YOUR_API_KEY' bằng API key của bạn
API_KEY = 'AIzaSyCmhpDQnXw6O8sR1uqcCsq4E94Okntk8ig'

# Khởi tạo YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

class Song:
    def __init__(self, id, title, artist, thumbnail, songUrl, audioUrl):
        self.id = id
        self.title = title
        self.artist = artist
        self.thumbnail = thumbnail
        self.songUrl = songUrl
        self.audioUrl = audioUrl

def getInfoSong(id):
    request = youtube.videos().list(part='snippet', id=id).execute()
    songResponse = request['items'][0]['snippet']
    thumbnail_url = songResponse['thumbnails']['medium']['url']
    songUrl = f'https://www.youtube.com/watch?v={id}'

    video = YouTube(songUrl)
    bestAudio = video.streams.filter(only_audio=True).first()
    audioUrl = bestAudio.url

    songInfo = Song(id, songResponse['title'], songResponse['channelTitle'], thumbnail_url, songUrl, audioUrl)
    return songInfo


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_response = youtube.search().list(
            q=request.form['query'],
            part='snippet',
            type='video',
            # videoCategoryId='10',  
            maxResults=3
        ).execute()

        songs = []
       
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            song = getInfoSong(video_id)
            songs.append(song)
        return render_template('index.html', songs=songs)


if __name__ == '__main__':
    app.run(debug=True)
