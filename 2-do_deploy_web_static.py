#!/usr/bin/python3
from datetime import datetime
from fabric.api import *
from os import path
'''automatize with fabric
'''

'''env.user = 'localhost'
'''
env.hosts = ['35.231.53.89', '35.190.176.186']


def do_pack():
    '''making a pack on web_static folder
    '''
    now = datetime.now()
    file = 'web_static_' + now.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local("mkdir -p versions")
    check = local("tar -cvzf versions/{} web_static".format(file))
    if check is not None:
        return file
    else:
        return None


def do_deploy(archive_path):
    '''distribute an archive to web servers
    '''
    print(archive_path)
    print(str(path.exists(archive_path)))
    if str(path.exists(archive_path)) is False:
        return False
    oper = []
    file = archive_path.split("/")
    oper.append(put(archive_path, '/tmp'))
    folder = file[1].split('.')
    print(folder[0])
    oper.append(
        run("mkdir -p /data/web_static/releases/{}".format(
            folder[0])))
    oper.append(run(
        "tar -xzf /tmp/{file} -C /data/web_static/releases/{}".format(
            file[1], folder[0])))
    oper.append(run("rm /tmp/{}".format(file[1])))
    oper.append(run("mv /data/web_static/releases/{0}/web_static/* /data/web_static/releases/{0}".format(
        folder[0])))
    oper.append(run(
        "rm -rf /data/web_static/releases/{}/web_static".format(
            folder[0])))
    oper.append(run("rm -rf /data/web_static/current"))
    oper.append(run(
        "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
            folder[0])))
    print(oper)
    for op in oper:
        if op is False:
            return False
    return True
