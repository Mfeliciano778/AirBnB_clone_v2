#!/usr/bin/python3
'''fabric script'''
from fabric.api import local
import os
from datetime import datetime


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
