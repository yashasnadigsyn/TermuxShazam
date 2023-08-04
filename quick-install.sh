pkg update
pkg install -y git
rm TermuxShazam -rf
git clone https://github.com/yashasnadigsyn/TermuxShazam.git --depth=1
cd TermuxShazam
sh ./install.sh
cd ..
rm TermuxShazam -rf