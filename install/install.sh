sudo cp -r ../../pymacscanner /usr/local/pymacscanner
sudo cp pymacscanner.service /etc/systemd/system/pymacscanner.service
sudo systemctl daemon-reload
sudo systemctl enable pymacscanner.service
sudo systemctl start pymacscanner.service