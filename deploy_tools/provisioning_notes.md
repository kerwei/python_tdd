Provisioning a new site
=======================

## Required packages:
  * nginx
  * Python 3.6
  * virtualenv + pip
  * Git

eg. on Ubuntu:

    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install nginx git python36 python3.6-venv


## Nginx Virtual Host config
  * see nginx.template.conf
  * replace DOMAIN with e.g. staging.my-domain.com
  * add to /etc/nginx/sites-available
  * crete a symlink at /etc/nginx/sites-enabled to /etc/nginx/sites-available


## Systemd service
  * see gunicorn-systemd.template.service
  * replace DOMAIN with e.g. staging.my-domain.com
  * add /etc/systemd/system/gunicorn-my-domain.service
  * reload systemctl daemon and nginx
  * enable guniconr-my-domain service and start



## Folder structure:

/home/kerwei
|
|--sites
    |
    |-- DOMAIN1
    |     |
    |     |-- .env
    |     |-- db.sqlite3
    |     |-- manage.py etc
    |     |-- static
    |     |-- virtualenv
    |
    |-- DOMAIN2
        |
        |-- .env
        |-- db.sqlite3
        |-- etc
