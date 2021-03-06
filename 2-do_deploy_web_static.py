#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of the web_static
"""
import os
from fabric.api import env, run, put
import datetime

env.hosts = ['54.237.196.98', '104.196.27.193']
env.user = 'ubuntu'


def do_deploy(archive_path):
    if not os.path.exists(archive_path):
        return False

    file_name = archive_path.split('/')
    new_name = file_name[1]
    new_var = new_name.split('.')
    path_tar = "/data/web_static/releases/{}/".format(new_var[0])
    link_cur = "/data/web_static/current"
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(path_tar))
        run("tar -xzf /tmp/{} -C {}".format(new_name, path_tar))
        run("rm /tmp/{}".format(new_name))
        run("mv {}web_static/* {}".format(path_tar, path_tar))
        run("rm -rf {}".format(link_cur))
        run("ln -s {} {}".format(path_tar, link_cur))
        return True
    except:
        return False
