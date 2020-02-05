#!/usr/bin/python3
#
# Reiko Kaps 2015 <r31k@k4p5.de>

import json
import sys, os, argparse
import shutil
import subprocess

try: 
    import requests
    from requests.exceptions import ConnectionError
except ImportError as e:
    print('please install requests python module')
    sys.exit(1)

DIR_URL='https://directory.spaceapi.io/'


def download(url):
    """Download a file to local filesystem
    Parameter url: URL 
    returns string (json)
    """
    try:
        file = requests.get(url)
    except ConnectionError as e:
        raise e
        
    return file.json()


def save(json):
    status(json)
    file = open("./spaceapi.json", 'w')
    file.write(str(json))
    file.close()

def status(json, verbose):
    """Ermittelt aus dem Json den Status des Hackerspace"""
    if verbose is True:
        pass
    
    if json['state']['open'] is False:
        print('🧘 closed'.format(str(json['space'])))
        return False

    print('🌞 open'.format(str(json['space'])))
    return True


def getHomepage(json, verbose):
    """Ermittelt aus dem Json die Homepage des Hackerspace"""
    if json['url']:
        print('opening {}'.format(json['url']))
        subprocess.run(['firefox', json['url']])
        
    else:
        return False


def getspaceurl(name, debug=False):
    try:
        directory = download(DIR_URL)
    except ConnectionError:
        raise
    if name in directory:    
        return directory[name]
    else:
        if debug:
            print('Space {} was not found!'.format(name))
        for key in directory:
            if name.lower() in key.lower():
                if debug:
                    print("Trying simulare spacename '{}' ...".format(key))
                return directory[key]
        sys.exit(1)

def main(args):
    if args.v:
        debug = args.v
    else:
        debug = False
        
    try:
        json = download(getspaceurl(args.name, debug))
    except ConnectionError as e:
        print('not connected')
        sys.exit(1)

    if args.w:
        getHomepage(json, debug)
        sys.exit(0)
        
    if status(json, verbose=False):
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Show Space Status')
    parser.add_argument('-n', '--name', help='Name of Hackerspace', default='LeineLab')
    parser.add_argument('-v', action='store_true', help='Show more Infos of Hackerspace')
    parser.add_argument('-w', action='store_true', help='get homepage url')
    args = parser.parse_args()
    
    main(args)
    
    
    
