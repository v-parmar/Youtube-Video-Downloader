
import logging
import sys
from flask import Flask, request, send_file
from flask.templating import render_template
from pytube import YouTube
from werkzeug.utils import redirect
 
"""
Flask YouTube Video Downloader - Python Marketer
https://pythonmarketer.com/2020/10/07/making-a-yout
ube-video-downloader-with-pythons-flask-and-pytube3-libraries/
"""
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
app = Flask(__name__)
 
@app.route('/')
def youtube_downloader():
    return render_template("main.html")
 
@app.route('/download', methods=['GET','POST'])
def download_video():
    """
    First pytube downloads the file locally in pythonanywhere:
    /home/your_username/video_name.mp4
 
    Then use Flask's send_file() to download the video 
    to the user's Downloads folder. 
    """
    try:
        youtube_url = request.form['link']
        download_path = YouTube(youtube_url).streams.get_by_itag(22).download()
        fname = download_path.split('//')[-1]
        return send_file(fname, as_attachment=True)
       
    except:
        logging.exception('Failed download')
        return 'Video download failed!'