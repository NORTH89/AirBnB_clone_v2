#!/usr/bin/python3
""" deploy """
from fabric.api import *


env.hosts = ["54.197.97.2", "34.229.186.37"]
env.user = "ubuntu"


def do_clean(number=0):
    """clean"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(path, number))
