script (based on the file 2-do_deploy_web_static.py)
that creates and distributes an
archive to your web servers, using the function deploy:
"""
from fabric.api import *
import os
env.hosts = ['54.209.136.208', '54.146.59.67']
@runs_once
def do_pack():
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
def do_deploy(archive_path):
    """
    distributes an archive to your web servers, using the function do_deploy:
    """
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        parent_path, arch_file = os.path.split(archive_path)
        arch_file_no_ext = arch_file.split(".tgz")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(arch_file_no_ext))
        run("tar -xzvf /tmp/{} -C /data/web_static/releases/{}/".format(
            arch_file, arch_file_no_ext))
        # decompresed files will begin with foldername/filename,
        # but we want to keep only the file name
        run("mv /data/web_static/releases/{}/web_static/*\
                /data/web_static/releases/{}/".format(arch_file_no_ext,
                                                      arch_file_no_ext))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            arch_file_no_ext))
        run("rm -r /tmp/{}".format(arch_file))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(arch_file_no_ext))
        print('New version deployed!')
    except Exception as e:
        print("Erros occured: ", e)
        return False
    return True
def deploy():
    """
    assists in creating and distributing archive files to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)

