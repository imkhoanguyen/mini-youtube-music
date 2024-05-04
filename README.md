# mini-youtube-music
![image](https://github.com/imkhoanguyen/mini-youtube-music/assets/142555542/9f0e86d2-78a9-455b-bf06-1de10fd0652d)

### This project is a mini-youtube-music web application built using the Flask framework. It allows users to input a YouTube video URL, keyword song, YouTube Playlist URL to play song and download the song with mp3 format.

#### This README.md file provides an overview of the project, installation instructions, usage guide.
## 🚀 Features 

🎉 Play Song

📺 Search song from Youtube video URL, keyword song, Youtube Playlist URL

⬇️ Download and Download All Song

## ⚙️ Installation 

```bash
$ git clone https://github.com/imkhoanguyen/mini-youtube-music.git
$ cd mini-youtube-music
$ pip install -r requirements.txt
$ python app.py
$ Open a web browser to http:127.0.0.1:5000 to access the application.
```

## 📝 Usage 

1. Enter a Youtube video URL, keyword song, Youtube Playlist URL.
2. Select the song you want to Play.
3. Click the icon "Download" and "Download All" button and wait for the audio to downlaod.
4. The file will be downloaded to your Desktop.

```bash
{
  "kind": "youtube#searchListResponse",
  "etag": "QChZWiObheg343U7hzTgY9J_nPI",
  "nextPageToken": "CAkQAA",
  "regionCode": "VN",
  "pageInfo": {
    "totalResults": 697129,
    "resultsPerPage": 9
  },
  "items": [
    {
      "kind": "youtube#searchResult",
      "etag": "bVohMEbLbB0XefXJ6kUuuBOhxLA",
      "id": {
        "kind": "youtube#video",
        "videoId": "zoEtcR5EW08"
      },
      "snippet": {
        "publishedAt": "2024-03-07T17:00:50Z",
        "channelId": "UClyA28-01x4z60eWQ2kiNbA",
        "title": "SƠN TÙNG M-TP | CHÚNG TA CỦA TƯƠNG LAI | OFFICIAL MUSIC VIDEO",
        "description": "Hãy thưởng thức ca khúc CHÚNG TA CỦA TƯƠNG LAI ngay tại đây: https://MTP.bfan.link/chung-ta-cua-tuong-lai ...",
        "thumbnails": {
          "default": {
            "url": "https://i.ytimg.com/vi/zoEtcR5EW08/default.jpg",
            "width": 120,
            "height": 90
          },
          "medium": {
            "url": "https://i.ytimg.com/vi/zoEtcR5EW08/mqdefault.jpg",
            "width": 320,
            "height": 180
          },
          "high": {
            "url": "https://i.ytimg.com/vi/zoEtcR5EW08/hqdefault.jpg",
            "width": 480,
            "height": 360
          }
        },
        "channelTitle": "Sơn Tùng M-TP Official",
        "liveBroadcastContent": "none",
        "publishTime": "2024-03-07T17:00:50Z"
      }
    },
  ]
}
```

