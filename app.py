from flask import Flask, render_template, request
from googleapiclient.discovery import build
from pytube import YouTube
import pafy
import vlc
from flask import Flask, render_template, request, Response


app = Flask(__name__)

# Thay đổi 'YOUR_API_KEY' bằng API key của bạn
API_KEY = 'AIzaSyCmhpDQnXw6O8sR1uqcCsq4E94Okntk8ig'

# Khởi tạo YouTube API
youtube = build('youtube', 'v3', developerKey=API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        # Thêm videoCategoryId vào yêu cầu tìm kiếm
        search_response = youtube.search().list(
            q=query,
            part='snippet',
            type='video',
            videoCategoryId='10',  # Thay '10' bằng ID của danh mục video mong muốn
            maxResults=10
        ).execute()
        videos = []
       
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video_response = youtube.videos().list(
                part='snippet',
                id=video_id
            ).execute()
            video_info = video_response['items'][0]['snippet']
            # Chọn hình ảnh thumbnail với kích thước "medium" (trung bình)
            thumbnail_url = video_info['thumbnails']['medium']['url']
            videos.append({
                'title': search_result['snippet']['title'],
                'video_id': search_result['id']['videoId'],
                'thumbnail': thumbnail_url,
                'channel_title': video_info['channelTitle']
            })
        return render_template('index.html', videos=videos)
    
@app.route('/play', methods=['POST'])
def play():
    video_url = request.form['video_url']
    audio_title = request.form['video_title']
    audio_thumb = request.form['video_thumb']
    audio_channel = request.form['video_channel']
    video = YouTube(video_url)
    best_audio = video.streams.filter(only_audio=True).first()
    audio_url = best_audio.url

    search_response = youtube.search().list(
        q=audio_channel,
        part='snippet',
        type='video',
        videoCategoryId='10',  # Thay '10' bằng ID của danh mục video mong muốn
        maxResults=15
    ).execute()
    videos = []
    
    for search_result in search_response.get('items', []):
        video_id = search_result['id']['videoId']
        video_response = youtube.videos().list(
            part='snippet',
            id=video_id
        ).execute()
        video_info = video_response['items'][0]['snippet']
        # Chọn hình ảnh thumbnail với kích thước "medium" (trung bình)
        thumbnail_url = video_info['thumbnails']['medium']['url']
        videos.append({
            'title': search_result['snippet']['title'],
            'video_id': search_result['id']['videoId'],
            'thumbnail': thumbnail_url,
            'channel_title': video_info['channelTitle']
        })

    return render_template('play.html', audio_url=audio_url, audio_title=audio_title, audio_thumb=audio_thumb, audio_channel=audio_channel, videos=videos)

@app.route('/stream_audio')
def stream_audio():
    audio_url = request.args.get('audio_url', '')
    audio_title = request.args.get('audio_title', '')
    audio_thumb = request.args.get('audio_thumb', '')
    videos = request.args.getlist('videos', '')
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')
    player = instance.media_player_new()
    media = instance.media_new(audio_url)
    player.set_media(media)
    player.play()
    return Response(status=200)

if __name__ == '__main__':
    app.run(debug=True)
