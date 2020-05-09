# Online Image Filter
Median or Mean image filter using python. The goal of this project is to offer a online median/mean filter. The project would read a PPM file, apply the filter per pixel, write the buffer to a new file. The new file is sent back by the server. 

The site showcasing this project is available at:
https://spatialfilter.com

## Setup Environment
```
apt-get install python3.5 nginx imagemagick
pip3 install flask gunicorn
```

## How to setup for debugging
```
//Python3.5+ required
cd app
/usr/local/bin/gunicorn -t9999 --workers 3 --bind 0.0.0.0:5000 -g www-data -m 007 wsgi:app
//Visit localhost:50000
```

## How to Deploy
```
//Install Systemd service
cp spatialFilter.service /etc/systemd/system/
systemctl enable spatialFilter
systemctl start spatialFilter

//Deplay Nginx (requires new certs)
cp nginxFilterConf /etc/nginx/sites-available/
ln -sf /etc/nginx/sites-available/nginxFilterConf /etc/nginx/sites-enabled/
systemctl reload nginx
```
