import argparse
import codecs
import os
import shutil
import sys
import jinja2


cwd = os.getcwd()
script_dir = os.path.dirname(os.path.realpath(__file__))


def main(argv):
    parser = argparse.ArgumentParser(description='My flask  app boilerplate code')
    parser.add_argument('appname', help='The application name')
    parser.add_argument('-d', '--destination', help='Folder to copy code to')
    args = parser.parse_args()

    appname = args.appname
    fullpath = os.path.join(cwd, appname)
    destination = args.destination

    shutil.copytree(os.path.join(script_dir, destination), fullpath)


if __name__ == '__main__':
    main(sys.argv)
