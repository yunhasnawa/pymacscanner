sudo cp pymacscanner.service /etc/systemd/system/pymacscanner.service
sudo systemctl daemon-reload
sudo systemctl enable my_python_script.service
sudo systemctl start my_python_script.service