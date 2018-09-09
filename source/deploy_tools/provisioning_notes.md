Provisioning a new site
=======================

* nginx
* Python 2.7
* Git
* pip
* virtualenv

e.g.,, on Ubuntu:

    sudo apt-get install nginx git
    sudo pip install virtualenv

## Nginx 虛擬主機設定

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Upstart 工作

* see gunicorn-upstart.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## 資料夾結構
Assume we have a user account at /home/username

/home/username
|___site
    |___SITENAME
        |___database
        |___source
        |___static
        |___virtualenv