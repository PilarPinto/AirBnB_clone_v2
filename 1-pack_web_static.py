#!/usr/bin/python3
"""
Script that generates a .tgz archive from the contents of the web_static
"""
import os
from fabric.api import local
import datetime

def do_pack():
    timeof = datetime.datetime.now()
    timeFor = timeof.strftime("%Y%m%d%H%M%S")
    namef = "versions/web_static{}.tgz".format(timeFor)

    try:
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(namef))
        return namef
    except:
        return None
