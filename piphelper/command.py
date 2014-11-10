import sys
import os
import pprint

from . import install_with_pip

def main():

    print(pprint.pprint(sys.path))

    this_python = sys.executable

    home = os.environ.get('HOME')

    venv_path = os.path.expandvars(
        os.path.expanduser(
            os.environ.get('WORKON_HOME', home + os.sep + 'virtualenvs')
        )
    )

    all_paths = os.walk(venv_path).__next__()[1]

    if this_python and os.path.exists(venv_path):
        this_path = os.sep.join(this_python.split(os.sep)[0:-3])

        if this_path != venv_path:
            all_paths.insert(0, os.sep.join(this_python.split(os.sep)[0:-2]))

    print('Select an environment to install to:')
    print(os.linesep.join(all_paths))

    # install_with_pip(sys.argv[1])
