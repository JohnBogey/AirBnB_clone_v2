#!/usr/bin/python3
''' pack and deploy archive '''

from fabric.api import put, run, env, local
import os
from datetime import datetime

env.hosts = ['35.237.13.104', '34.75.145.253']


def do_pack():
    '''packs webstatic'''
    now = datetime.now().strftime("%Y%m%d%I%M%S")
    local("mkdir -p versions")
    local("tar -cvzf versions/web_static_{}.tgz web_static"
          .format(now))
    return "versions/web_static_{}.tgz".format(now)


def do_deploy(archive_path):
    ''' deploys webstatic '''
    if not os.path.exists(archive_path):
        return False
    try:
        name_ex = archive_path.split('/')[-1]
        name = name_ex.split('.')[0]
        put(archive_path, "/tmp/{}".format(name_ex))
        run("mkdir -p /data/web_static/releases/{}/".format(name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(name_ex, name))
        run("rm /tmp/{}".format(name_ex))
        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except Exception as e:
        return False


def deploy():
    '''calls previous functions to do everything'''
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive_path)
