import os
import platform
import random as rnd
import sys
import time


def main():
    stamp = time.time()
    reg_keys = ['secure', 'sex', '69']

    if len(sys.argv) > 1 and sys.argv[1] in reg_keys:  # in-line
        export()
    elif input('Enter Your Registration key: ') in reg_keys:  # run-time
        export()
    else:
        print('Access Deny!')
        print(f'loop complete in: {time.time() - stamp}')


def info():
    """serious information about target system"""
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
        'time': [time.time(), time.ctime()],
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
    return _info


def dly(sec=None) -> None:
    """delay function for make interrupt"""
    if sec:
        time.sleep(sec)
    else:
        time.sleep(rnd.random() / 3.14156294)


def writeln(value: str):
    """echo, print, write, this function have a lot of names"""
    chars = str()
    for line in str(value).split('\n'):
        for char in line:
            chars += char
            print(f'\r{chars}', end='')
            dly()
        chars = str()
        dly()


def export():
    """export information"""
    data = info()
    for k, v in data.items():
        writeln(f'{k}: ')
        print(v)
        dly()


if __name__ == '__main__':
    main()
