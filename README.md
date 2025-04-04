# FB
FB
pkg update && pkg upgrade
pkg install python
pip install selenium requests colorama
pkg install wget

wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver /data/data/com.termux/files/usr/bin/
chmod +x /data/data/com.termux/files/usr/bin/chromedriver
