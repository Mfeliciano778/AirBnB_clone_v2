#!/usr/bin/python3
'''fabric script'''
from fabric.api import *
from datetime import datetime
import os


env.hosts = ['34.75.248.37', '34.74.75.108']


def do_deploy(archive_path):
    '''do_deploy'''
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp")
            file = archive_path.split("/")
            directory_name = file.split(".")
            run("sudo mkdir -p /data/web_static/releases/{}/".
                format(directory_name[0]))
            run("sudo tar -zxf /tmp/{} -C /data/web_static/releases/{}/".
                format(file[1], directory_name[0]))
            run("sudo rm -rf /tmp/{}".format(file[1]))
            run("sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".
                format(directory_name[0], directory_name[0]))
            run("sudo rm -rf /data/web_static/releases/{}/web_static".
                format(directory_name[0]))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(directory_name[0]))
            return True
        except:
            return False
    print 
    return False
