#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack.
"""
from datetime import datetime
from fabric.api import *
import os
def do_pack():
    """
    creates a directory to store archive file and archives web_static files
    """
    try:
        archive_path = "versions/web_static_{}.tgz".format(
            datetime.now().strftime("%Y%m%d%H%M%S"))
        local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_path))
        print("web_static packed: {} -> {}Bytes".format(
            archive_path, os.path.getsize(archive_path)))
        return archive_path
    except Exception:
        return None

