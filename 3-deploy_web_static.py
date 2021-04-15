#!/usr/bin/python3
'''fabric script'''
from fabric.api import *
import os
from datetime import datetime


env.hosts = ['34.75.248.37', '34.74.75.108']


def do_pack():
    '''do_pack - generates a tgz archive'''
    time_now = datetime.now()
    date_time = time_now.strftime("%Y%m%d%H%M%S")
    file = "versions/web_static_{}.tgz".format(date_time)

    if not os.path.exists("versions"):
        local("mkdir versions")
    local("tar -czvf " + file + " web_static")
    if os.path.exists(file):
        return file
    return None


def do_deploy(archive_path):
    '''do_deploy'''
    if os.path.exists(archive_path):
        try:
            put(archive_path, "/tmp/")
            file = archive_path.split("/")
            directory_name = file[1].split(".")
            run("sudo mkdir -p /data/web_static/releases/{}/".
                format(directory_name[0]))
            run("sudo tar -zxf /tmp/{} -C /data/web_static/releases/{}/".
                format(file[1], directory_name[0]))
            run("sudo rm /tmp/{}".format(file[1]))
            run("sudo mv /data/web_static/releases/{}/web_static/* \
                /data/web_static/releases/{}/".
                format(directory_name[0], directory_name[0]))
            run("sudo rm -rf /data/web_static/releases/{}/web_static".
                format(directory_name[0]))
            run("sudo rm -rf /data/web_static/current")
            run("sudo ln -s /data/web_static/releases/{}/ \
                /data/web_static/current".format(directory_name[0]))
            return True
        except Exception as e:
            return False
    return False


def deploy():
    '''deploy'''
    pack = do_pack()
    if pack is None:
        return False
    return do_deploy(pack)
