#!/usr/bin/python3
''' get compressed file of web static '''

from fabric.api import local
from datetime import datetime


def do_pack():
    '''packs webstatic'''
    now = datetime.now().strftime("%Y%m%d%I%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static"
          .format(now))
    return "versions/web_static_{}.tgz".format(now)
