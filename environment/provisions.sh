lschmod 755 /tmp/

chmod +x /tmp/vagrant-shell


#!bin/bash
  # Install python and pip
  sudo apt-get update
  sudo apt-get install python3-venv -y
  sudo apt-get install python3-pip -y
  cd /home/ubuntu/
  sudo python3 -m venv env
  #sudo python3 -m pip install flask
  #sudo python3 -m pip install datetime
  cd /home/ubuntu/app
  sudo python3 -m pip install -r requirements.txt
  sudo apt-get install nginx -y
  sudo systemctl start nginx


# Configuring nginx proxy
  sudo unlink /etc/nginx/sites-enabled/default
  cd /etc/nginx/sites-available
  sudo touch reverse-proxy.conf
  sudo chmod 666 reverse-proxy.conf
  echo "server{
    listen 80;
    location / {
        proxy_pass http://192.168.10.100:5000;
    }
  }" >> reverse-proxy.conf

  sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
  sudo service nginx restart


  export FLASK_APP=app.py
  cd /home/ubuntu/app
  sudo flask run -h 0.0.0.0
