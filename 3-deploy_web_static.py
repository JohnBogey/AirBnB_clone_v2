#!/usr/bin/python3
''' pack and deploy archive '''

from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy

def deploy():
    '''calls previous functions to do everything'''
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive_path)
