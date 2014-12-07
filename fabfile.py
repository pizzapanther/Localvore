import os
import sys

from fabric.api import (
  env,
  run,
  sudo,
  cd,
  hosts,
  settings as fabric_settings
)
from fabric.operations import get, prompt, local
from fabric.contrib.project import rsync_project

env.use_ssh_config = True

WEB_USER = "www"
WEB_HOST = 'dev.localvore.guide'

@hosts(WEB_HOST)
def deploy():
  with cd('/home/www/Localvore/'):
    sudo('git pull', user=WEB_USER)
    
  with cd('/home/www/Private-Settings/'):
    sudo('git pull', user=WEB_USER)
    
  with cd('/home/www/Localvore/django-app/'):
    sudo('git rev-parse --short HEAD > release.txt', user=WEB_USER)
    sudo('su -c "pip install -r requirements.txt --user" {}'.format(WEB_USER))
    sudo('su -c "./manage.py migrate" {}'.format(WEB_USER))
    sudo('su -c "./manage.py collectstatic --noinput" {}'.format(WEB_USER))
    
  sudo('supervisorctl restart localvore')
  
@hosts(WEB_HOST)
def upgrade ():
  sudo('apt-get update')
  sudo('apt-get upgrade -y')
  sudo('reboot')
  