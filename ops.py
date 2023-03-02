import os
import platform
import string
import sys
import time


def main():
    information = OPS()
    information.present()
    information.option()


class OPS:
    """
    ops: os, platform, system get system information, to act base on.
    author: NightFox | OPS v0.1
    """

    def __init__(self):
        self.info = self.info()  # Get information
        self.readable = '\n'.join([f'{k:22}|{v}' for k, v in self.info.items()])
        self.version = '0.1'

    def __iter__(self):
        return iter(self.info.items())

    def __len__(self):
        return len(self.info)

    def __repr__(self):
        return str(self.info)

    def __str__(self):
        return str(self.info)

    @staticmethod
    def info():
        # Gathering basic data
        _info = {
            # user_info
            'getlogin': os.getlogin(),
            'node': platform.node(),
            # current_dir
            'getcwd': os.getcwd(),
            'listdir': os.listdir(),
            'scandir': os.scandir(),
            # system_info
            'system': platform.system(),
            'platform': [platform.platform(), sys.platform],
            'processor': platform.processor(),
            'uname': platform.uname(),
            'architecture': platform.architecture(),
            'machine': platform.machine(),
            'cpu_count': os.cpu_count(),
            # time
            'time': time.time(),
            'ctime': time.ctime(),
            'tzname': time.tzname,
            'timezone': time.timezone,
            'altzone': time.altzone,
            # runtime_info
            'times': os.times(),
            'getpid': os.getpid(),
            'getppid': os.getppid(),
            'environ': os.environ,
            'get_exec_path': os.get_exec_path(),
            'name': os.name,
            'path': os.path,
            'argv': sys.argv,
            'version': sys.version,
            # python
            'python_compiler': platform.python_compiler(),
            'python_implementation': platform.python_implementation(),
            'python_version': platform.python_version(),
            # windows
            'win32_edition': platform.win32_edition(),
            'win32_is_iot': platform.win32_is_iot(),
            'win32_ver': platform.win32_ver(),
            # more info
            'encoding': sys.getdefaultencoding(),
            'abort': os.abort,  # abort command
            'exit': sys.exit,  # exit command
        }
        # for 'Windows' os, find and add the HDD Drives
        if _info['system'].lower() == 'windows':
            _info['drivers'] = [f'{i}:\\' for i in string.ascii_uppercase if os.path.isdir(f'{i}:\\')]
        return _info

    def present(self):
        # info presentation
        print(self.readable)

    def option(self):
        ans = input('\nOption: (export/exit)').strip()
        if ans.lower() in ['export']:
            self.export()
        elif ans.lower() in ['quit', 'exit']:
            self.exit()

    def export(self):
        # export info as text file
        with open('ops.txt', 'w') as f:
            f.write(self.readable)
        print('export completed!')

    def exit(self):
        # exit function
        self.info['exit']()


if __name__ == '__main__':
    main()
