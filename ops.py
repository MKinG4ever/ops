import os
import platform
import sys
import string
from random import random as rnd
from time import sleep as dly
from time import time, ctime


def main():
    """
    ops: os, platform, system get system information, to act base on.
    Powered by Python author: NightFox v0.02
    """
    key_guard()  # ask for safety key
    info()  # gathering data


def echo(value):
    """echo, print, write, this function have a lot of names"""
    for line in value.split('\n'):
        char = str()
        for ch in line:
            char += ch
            print(f'\r{char}', end='')
            if not ch == ' ':
                dly(rnd() / 3.14159264)
    if str(value).endswith('\n'):
        print()


def key_guard(keyword: bool = True):
    """Create a safety key to protect your Data/System"""
    if keyword:
        _keys = ['secure', 'sex', '69', 'kiss', 'love']
        if not input('Enter your safety keyword: ') in _keys:
            echo('Access Denied.')
            sys.exit()
        else:
            echo('Initiation ...')
            echo(f'{ctime()}\n')
            dly(0.1)
    else:
        # feature for enable|disable key_guard safety
        # sys.exit()
        echo('You are disabling safety keyword !!!\n')


def info():
    # Gathering data
    _info = {
        # user_info
        'getlogin': os.getlogin(),
        'node': platform.node(),
        'uname': platform.uname(),
        # current_dir
        'getcwd': os.getcwd(),
        'path': sys.path,
        # system_info
        'system': platform.system(),  # Linux|Windows
        'architecture': platform.architecture(),
        'platform': [sys.platform, platform.platform()],
        'version': [platform.python_version(), sys.version],
        # runtime_info
        'pid': os.getpid(),
        'ppid': os.getppid(),
        'argv': sys.argv,
        'time': [ctime(), time()],
        # more info
        'cpu_count': os.cpu_count(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'environ': os.environ,
        'listdir': os.listdir(),
        'scandir': os.scandir(),
        'python_compiler': platform.python_compiler(),
        'win32_edition': platform.win32_edition(),
        'win32_is_iot': platform.win32_is_iot(),
        'win32_ver': platform.win32_ver(),
        'encoding': sys.getdefaultencoding(),
        'cache': sys.path_importer_cache,
    }
    # for 'Windows' os, find and add the HDD Drives
    if _info['system'].lower() == 'windows':
        _info['drivers'] = [f'{i}:\\' for i in string.ascii_uppercase if os.path.isdir(f'{i}:\\')]
    # Presentation
    for key, val in _info.items():
        echo(f'{key:15}: ')
        print(val)
    # return data
    return _info


if __name__ == '__main__':
    main()
