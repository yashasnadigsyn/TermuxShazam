pkg install python
pkg install python-numpy
pkg install ffmpeg
pip install -U yt-dlp
pip install shazamio
pkg install termux-api
mkdir ~/bin
touch ~/bin/termux-url-opener
echo "python3 $(pwd)/share_recognize.py \$1" >> ~/bin/termux-url-opener

