// init
const timeline = document.querySelector(".timeline");
const currentTimeSpan = document.getElementById("current-time");
const totalTimeSpan = document.getElementById("total-time");
const audio = document.querySelector("audio");
const volumeControl = document.getElementById("volume-control");
const volumeRange = document.querySelector(".volume-range");
const playButton = document.querySelector(".play-btn");
const nextButton = document.querySelector(".next-btn");
const prevButton = document.querySelector(".prev-btn");
const repeatButton = document.querySelector(".repeat-btn");
const shuffleButton = document.querySelector(".shuffle-btn");
const soundButton = document.querySelector(".sound-btn")

// init icon
const shuffle = `<svg
        xmlns="http://www.w3.org/2000/svg"
        width="20"
        height="20"
        fill="#000000"
        class="bi bi-shuffle"
        viewBox="0 0 16 16"
        >
        <path
            fill-rule="evenodd"
            d="M0 3.5A.5.5 0 0 1 .5 3H1c2.202 0 3.827 1.24 4.874 2.418.49.552.865 1.102 1.126 1.532.26-.43.636-.98 1.126-1.532C9.173 4.24 10.798 3 13 3v1c-1.798 0-3.173 1.01-4.126 2.082A9.6 9.6 0 0 0 7.556 8a9.6 9.6 0 0 0 1.317 1.918C9.828 10.99 11.204 12 13 12v1c-2.202 0-3.827-1.24-4.874-2.418A10.6 10.6 0 0 1 7 9.05c-.26.43-.636.98-1.126 1.532C4.827 11.76 3.202 13 1 13H.5a.5.5 0 0 1 0-1H1c1.798 0 3.173-1.01 4.126-2.082A9.6 9.6 0 0 0 6.444 8a9.6 9.6 0 0 0-1.317-1.918C4.172 5.01 2.796 4 1 4H.5a.5.5 0 0 1-.5-.5"
        />
        <path
            d="M13 5.466V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m0 9v-3.932a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192"
        />
        </svg>`;
const shuffleBlue = `<svg
        xmlns="http://www.w3.org/2000/svg"
        width="20"
        height="20"
        fill="#0000FF"
        class="bi bi-shuffle"
        viewBox="0 0 16 16"
        >
        <path
            fill-rule="evenodd"
            d="M0 3.5A.5.5 0 0 1 .5 3H1c2.202 0 3.827 1.24 4.874 2.418.49.552.865 1.102 1.126 1.532.26-.43.636-.98 1.126-1.532C9.173 4.24 10.798 3 13 3v1c-1.798 0-3.173 1.01-4.126 2.082A9.6 9.6 0 0 0 7.556 8a9.6 9.6 0 0 0 1.317 1.918C9.828 10.99 11.204 12 13 12v1c-2.202 0-3.827-1.24-4.874-2.418A10.6 10.6 0 0 1 7 9.05c-.26.43-.636.98-1.126 1.532C4.827 11.76 3.202 13 1 13H.5a.5.5 0 0 1 0-1H1c1.798 0 3.173-1.01 4.126-2.082A9.6 9.6 0 0 0 6.444 8a9.6 9.6 0 0 0-1.317-1.918C4.172 5.01 2.796 4 1 4H.5a.5.5 0 0 1-.5-.5"
        />
        <path
            d="M13 5.466V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m0 9v-3.932a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192"
        />
        </svg>`;

const repeatBtn = `<svg
        xmlns="http://www.w3.org/2000/svg"
        width="20"
        height="20"
        fill="currentColor"
        class="bi bi-repeat"
        viewBox="0 0 16 16"
        >
        <path
            d="M11 5.466V4H5a4 4 0 0 0-3.584 5.777.5.5 0 1 1-.896.446A5 5 0 0 1 5 3h6V1.534a.25.25 0 0 1 .41-.192l2.36 1.966c.12.1.12.284 0 .384l-2.36 1.966a.25.25 0 0 1-.41-.192m3.81.086a.5.5 0 0 1 .67.225A5 5 0 0 1 11 13H5v1.466a.25.25 0 0 1-.41.192l-2.36-1.966a.25.25 0 0 1 0-.384l2.36-1.966a.25.25 0 0 1 .41.192V12h6a4 4 0 0 0 3.585-5.777.5.5 0 0 1 .225-.67Z"
        />
        </svg>`;

    const repeatBtn1 = `<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-repeat-1" viewBox="0 0 16 16">
    <path d="M11 4v1.466a.25.25 0 0 0 .41.192l2.36-1.966a.25.25 0 0 0 0-.384l-2.36-1.966a.25.25 0 0 0-.41.192V3H5a5 5 0 0 0-4.48 7.223.5.5 0 0 0 .896-.446A4 4 0 0 1 5 4zm4.48 1.777a.5.5 0 0 0-.896.446A4 4 0 0 1 11 12H5.001v-1.466a.25.25 0 0 0-.41-.192l-2.36 1.966a.25.25 0 0 0 0 .384l2.36 1.966a.25.25 0 0 0 .41-.192V13h6a5 5 0 0 0 4.48-7.223Z"/>
    <path d="M9 5.5a.5.5 0 0 0-.854-.354l-1.75 1.75a.5.5 0 1 0 .708.708L8 6.707V10.5a.5.5 0 0 0 1 0z"/>
    </svg>`;      

const playIcon = ` <svg
        xmlns="http://www.w3.org/2000/svg"
        width="30"
        height="30"
        fill="currentColor"
        class="bi bi-play-circle-fill"
        viewBox="0 0 16 16"
    >
        <path
        d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M6.79 5.093A.5.5 0 0 0 6 5.5v5a.5.5 0 0 0 .79.407l3.5-2.5a.5.5 0 0 0 0-.814z"
        />
    </svg>`;

const pauseIcon = ` <svg
    xmlns="http://www.w3.org/2000/svg"
    width="30"
    height="30"
    fill="currentColor"
    class="bi bi-pause-circle-fill"
    viewBox="0 0 16 16"
    >
    <path
        d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M6.25 5C5.56 5 5 5.56 5 6.25v3.5a1.25 1.25 0 1 0 2.5 0v-3.5C7.5 5.56 6.94 5 6.25 5m3.5 0c-.69 0-1.25.56-1.25 1.25v3.5a1.25 1.25 0 1 0 2.5 0v-3.5C11 5.56 10.44 5 9.75 5"
    />
    </svg>`;

const muteIcon = `<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="currentColor" class="bi bi-volume-mute-fill" viewBox="0 0 16 16">
    <path d="M6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06m7.137 2.096a.5.5 0 0 1 0 .708L12.207 8l1.647 1.646a.5.5 0 0 1-.708.708L11.5 8.707l-1.646 1.647a.5.5 0 0 1-.708-.708L10.793 8 9.146 6.354a.5.5 0 1 1 .708-.708L11.5 7.293l1.646-1.647a.5.5 0 0 1 .708 0"/>
</svg>`

const volumnIcon = `<svg
    xmlns="http://www.w3.org/2000/svg"
    width="24"
    height="24"
    fill="currentColor"
    class="bi bi-volume-up-fill"
    viewBox="0 0 16 16"
    >
    <path
        d="M11.536 14.01A8.47 8.47 0 0 0 14.026 8a8.47 8.47 0 0 0-2.49-6.01l-.708.707A7.48 7.48 0 0 1 13.025 8c0 2.071-.84 3.946-2.197 5.303z"
    />
    <path
        d="M10.121 12.596A6.48 6.48 0 0 0 12.025 8a6.48 6.48 0 0 0-1.904-4.596l-.707.707A5.48 5.48 0 0 1 11.025 8a5.48 5.48 0 0 1-1.61 3.89z"
    />
    <path
        d="M8.707 11.182A4.5 4.5 0 0 0 10.025 8a4.5 4.5 0 0 0-1.318-3.182L8 5.525A3.5 3.5 0 0 1 9.025 8 3.5 3.5 0 0 1 8 10.475zM6.717 3.55A.5.5 0 0 1 7 4v8a.5.5 0 0 1-.812.39L3.825 10.5H1.5A.5.5 0 0 1 1 10V6a.5.5 0 0 1 .5-.5h2.325l2.363-1.89a.5.5 0 0 1 .529-.06"
    />
    </svg>`

/* ***************Function***************** */
// dowload 1 file
$(document).ready(function() {
    $("#download-btn").click(function() {
        toastr.info("The download is starting. Please wait a moment");
        const songUrl = $("#txtSongUrl").val(); 
        $.ajax({
            type: "POST",
            url: "/download",
            data: { txtSongUrl: songUrl }, 
            success: function(response) {
                if ('message' in response) {
                    toastr.success(response.message);
                } else if ('error' in response) {
                    toastr.error(response.message);
                }
            }
        });
    });
});

// dowload all file
$(document).ready(function() {
    $("#download-all-btn").click(function() {
        toastr.info("The download is starting. Please wait a moment");
        const songs = JSON.parse(localStorage.getItem('songs'));
        const songUrls = songs.map(song => song.songUrl);
        console.log(songUrls);
        $.ajax({
            type: "POST",
            url: "/downloadAll",
            contentType: "application/json",
            data: JSON.stringify({ songUrls: songUrls }), 
            success: function(response) {
                if ('message' in response) {
                    toastr.success(response.message);
                } else if ('error' in response) {
                    toastr.error(response.message);
                }
            }
        });
    });
});


// play and pause
function toggleAudio() {
    if (audio.paused) {
    audio.play();
    playButton.innerHTML = pauseIcon;
    } else {
    audio.pause();
    playButton.innerHTML = playIcon;
    }
}
// ev play and pasue
playButton.addEventListener('click', toggleAudio);

// mute
function toggleSound () {
    audio.muted = !audio.muted;
    soundButton.innerHTML = audio.muted ? muteIcon : volumnIcon;
}
// ev mute
soundButton.addEventListener('click', toggleSound);

// play song
let indexSong = 0;

function playSong(index) {
    
    indexSong = index;

    song = songsArray[index];
    document.getElementById("audio_player").src = song.audioUrl;
    document.getElementById("audio_player").play();
    document.getElementById("song-title").textContent = song.title;
    document.getElementById("song-channel").textContent = song.artist;
    document.getElementById("song-img").src = song.thumbnail;
    document.getElementById("song-img").alt = song.title;
    playButton.innerHTML = pauseIcon;
    document.getElementById("txtSongUrl").value = song.songUrl;
}

function nextSong() {
    indexSong++;
    if(indexSong > songsArray.length - 1) {
    indexSong = 0;
    }
    playSong(indexSong);
}

function prevSong() {
    indexSong--;
    if(indexSong < 0) {
    indexSong = songsArray.length - 1;
    }
    playSong(indexSong);
}

nextButton.addEventListener('click', nextSong);
prevButton.addEventListener('click', prevSong);

// change input time song
function changeSeek() {
    const time = (timeline.value * audio.duration) / 100;
    audio.currentTime = time;
}
timeline.addEventListener("change", changeSeek);

// update time and timeline
audio.addEventListener("timeupdate", () => {
    const currentTime = formatTime(audio.currentTime);
    const totalTime = formatTime(audio.duration);
    currentTimeSpan.textContent = currentTime;
    totalTimeSpan.textContent = totalTime;

    // Cập nhật giá trị của thanh trượt
    const progress = (audio.currentTime / audio.duration) * 100;
    timeline.value = progress;
});

// Convert s to mm:ss
function formatTime(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = Math.floor(seconds % 60);
    return `${minutes}:${
    remainingSeconds < 10 ? "0" : ""
    }${remainingSeconds}`;
}

// ev change volumn
volumeRange.addEventListener("input", () => {
    audio.volume = volumeRange.value;
});

// load songs
displayHtml = "";
var songsArray = JSON.parse(localStorage.getItem('songs'));
if (songsArray) {
  if(songsArray.length > 0) {
    displayBtnDownload = `
      <h2 class="text-center">Search results<h2>
      <div class="row mb-3">
        <div class="col-9"></div>
        <div class="col-3 text-end">
          <button class="btn btn-primary" id="download-all-btn">
            Download All
          </button>
        </div>  
      </div>
    `
  }
  for (var i = 0; i < songsArray.length; i++) {
    displayHtml += `
    <div class="col mb-4">
      <div
        class="mb-2 song-container"
        onclick="playSong('${i}')">
        <img
          src="${songsArray[i].thumbnail}"
          width="100%"
          alt="${songsArray[i].title}"
          class="rounded-3"
        />
      </div>
      <input type="hidden" name="songId" value="${songsArray[i].id}" />
      <p>${songsArray[i].title}</p>
    </div>
    `;
  }
  document.getElementById('songsList').innerHTML = displayHtml;
  document.querySelector('.con-btn-download').innerHTML = displayBtnDownload;
} 


// 
let isRepeat = false;

function repeatSong() {
  isRepeat = true;
  repeatButton.innerHTML = repeatBtn1;
}

function notRepeatSong() {
  isRepeat = false;
  repeatButton.innerHTML = repeatBtn;
}

repeatButton.addEventListener('click', () => (isRepeat ? notRepeatSong() : repeatSong()));

audio.addEventListener('ended', ()=>(isRepeat ? playSong(indexSong): nextSong()));

// 
function shuffleArray(array) {
  let currentIndex = array.length, temporaryValue, randomIndex;

  while (currentIndex !== 0) {

    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

let isShuffle = false;

function shuffleSong() {
  isShuffle = true;
  shuffleButton.innerHTML = shuffleBlue;
  songsArray = shuffleArray(JSON.parse(localStorage.getItem('songs')));
}

function notShuffleSong() {
  isShuffle = false;
  shuffleButton.innerHTML = shuffle;
  songsArray = JSON.parse(localStorage.getItem('songs'));
}

shuffleButton.addEventListener('click', () => (isShuffle ? notShuffleSong() : shuffleSong()))
