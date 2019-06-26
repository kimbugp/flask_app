import argparse
import os
import shutil
import sys

cwd = os.getcwd()
script_dir = cwd+'/flask_app'


def program(argv):
    parser = argparse.ArgumentParser(
        description='My flask  app boilerplate code')
    parser.add_argument('appname', help='The application name')
    parser.add_argument('-d', '--destination', help='Folder to copy code to')
    args = parser.parse_args()

    appname = args.appname
    destination = args.destination
    
    destination_path = os.path.join(destination, appname)
    shutil.copytree(os.path.join(script_dir), destination_path)

    # create .env file
    shutil.copy(destination_path+'/.env.sample', destination_path+'/.env')


def main():
    program(sys.argv)


if __name__ == '__main__':
    main()
