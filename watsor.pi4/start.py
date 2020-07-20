import sys
import subprocess
from multiprocessing import set_start_method

if __name__ == '__main__':
    set_start_method('spawn')

    for index, arg in enumerate(sys.argv):
        if arg == "/etc/watsor/config.yaml":
            config = subprocess.check_output(['./config.sh', 'CONFIG_FILE'])
            sys.argv[index] = config.decode('utf-8').strip()

    from watsor.main import Application

    app = Application()
    app.run()
