from flask import Flask, render_template, request
from googleapiclient.discovery import build

app = Flask(__name__)

# Thay đổi 'YOUR_API_KEY' bằng API key của bạn
API_KEY = 'AIzaSyCUDaCZJRNk9MeQh3XEOW2iP-QlS-Ku6vk'

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

if __name__ == '__main__':
    app.run(debug=True)
