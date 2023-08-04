pkg update
pkg upgrade -y
pkg install -y python \
               python-numpy \
               ffmpeg \
               termux-api
pip install -U yt-dlp shazamio
mkdir -p ~/bin
echo "python3 $(pwd)/share_recognize.py \$1" > ~/bin/termux-url-opener
