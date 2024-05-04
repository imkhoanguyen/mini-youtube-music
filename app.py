from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build
from pytube import YouTube
import json
import re
from concurrent.futures import ThreadPoolExecutor
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

@app.route('/getAudioUrl', methods=['POST'])
def getAudioUrl():
    try:
        data_received = request.json
        video_id = data_received.get('videoId', None)
        video = YouTube(f'https://www.youtube.com/watch?v={video_id}')
        best_audio = video.streams.filter(only_audio=True).first()
        audio_url = best_audio.url
        return jsonify({'audioUrl': audio_url})
    except Exception as e:
        print(f"Error fetching audio URL for video {video_id}: {e}")
        return jsonify({'audioUrl': f'{audio_url}'})

@app.route('/download', methods=['POST'])
def download():
    songUrl = request.form['txtSongUrl']
    try:
        yt = YouTube(songUrl)
        t = yt.streams.filter(only_audio=True)
        t[0].download(output_path=os.path.expanduser('~/Desktop'))
        filename = t[0].default_filename
        baseName, _ = os.path.splitext(filename)
        newFileName = baseName + ".mp3"
        
        # Check if the new filename already exists
        count = 1
        while os.path.exists(os.path.join(os.path.expanduser('~/Desktop'), newFileName)):
            newFileName = f"{baseName}_{count}.mp3"
            count += 1

        os.rename(os.path.join(os.path.expanduser('~/Desktop'), filename), os.path.join(os.path.expanduser('~/Desktop'), newFileName))
        return jsonify({'message': 'Download Audio Success!'})
    except Exception as e:
        return jsonify({'error': 'Download Audio Fail!'})
    
@app.route('/downloadAll', methods=['POST'])
def downloadAll():
    data = request.json
    songUrls = data.get('songUrls', []) 
    try:
        for songUrl in songUrls:
            yt = YouTube(songUrl)
            t = yt.streams.filter(only_audio=True)
            t[0].download(output_path=os.path.expanduser('~/Desktop'))
            filename = t[0].default_filename
            baseName, _ = os.path.splitext(filename)
            newFileName = baseName + ".mp3"
            
            # Check if the new filename already exists
            count = 1
            while os.path.exists(os.path.join(os.path.expanduser('~/Desktop'), newFileName)):
                newFileName = f"{baseName}_{count}.mp3"
                count += 1

            os.rename(os.path.join(os.path.expanduser('~/Desktop'), filename), os.path.join(os.path.expanduser('~/Desktop'), newFileName))
        return jsonify({'message': 'Download Audio Success!'})
    except Exception as e:
        return jsonify({'error': 'Download Audio Fail!'})

def searchWithSongName(query):
    songs = []
    search_response = youtube.search().list(
                    q=query,
                    part='snippet',
                    type='video',
                    videoCategoryId='10',  
                    maxResults=9
                ).execute()

    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        videoUrl = f"https://www.youtube.com/watch?v={video_id}"
        title = search_result['snippet']['title']
        artist = search_result['snippet'].get('channelTitle', 'Unknown')
        thumbnail = search_result['snippet']['thumbnails']['medium']['url']
        song = Song(video_id, title, artist, thumbnail, videoUrl, "")
        songs.append(song)
    
    return json.dumps([song.__dict__ for song in songs])

def searchWithPlaylistUrl(query, playlistId):
    songs = []
    playlist_response = youtube.playlistItems().list(
        playlistId=playlistId,
        part='snippet',
        maxResults=50,
    ).execute()

    for search_result in playlist_response.get('items', []):
        videoId = search_result['snippet']['resourceId']['videoId']
        videoUrl = f'https://www.youtube.com/watch?v={videoId}'
        title = search_result['snippet']['title']
        artist = search_result['snippet']['channelTitle']
        thum = search_result['snippet']['thumbnails']['medium']['url']
        song = Song(videoId, title, artist, thum, videoUrl, "")
        songs.append(song)

    return json.dumps([song.__dict__ for song in songs])

def searchWithVideoUrl(query, videoId):
    search_result = youtube.videos().list(
        part='snippet',
        id=videoId
    ).execute()
    if len(search_result['items']) > 0:
        videoInfo = search_result['items'][0]['snippet']
        title = videoInfo['title']
        thum = videoInfo['thumbnails']['medium']['url']
        artist = videoInfo['channelTitle']
        videoUrl = f'https://www.youtube.com/watch?v={videoId}'
        song = Song(videoId,title,artist,thum,videoUrl, "")
    
    return json.dumps([song.__dict__])

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        youtube_video_match = re.match(r'^https?://(?:www\.)?youtube\.com/watch\?v=([^\s&]+)', query)
        youtube_video_in_playlist = re.search(r'list=([^\s&]+)', query)
        
        if youtube_video_in_playlist:
            playlistId = youtube_video_in_playlist.group(1)
            songs_json = searchWithPlaylistUrl(query, playlistId)
            return render_template('index.html', songs=songs_json)
        elif youtube_video_match:
            videoId = youtube_video_match.group(1)
            songs_json = searchWithVideoUrl(query, videoId)
            return render_template('index.html', songs=songs_json)
        else:
            songs_json = searchWithSongName(query)
            return render_template('index.html', songs=songs_json)

if __name__ == '__main__':
    app.run(debug=True)
