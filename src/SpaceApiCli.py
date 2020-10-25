#!/usr/bin/python3
#
# Reiko Kaps 2015-2020 <r31k@k4p5.de>

import argparse
import json
import subprocess
import sys

try:
    import requests
    from requests.exceptions import ConnectionError
except ImportError:
    print('please install requests python module')
    sys.exit(1)

DIR_URL = 'https://directory.spaceapi.io/'


def download(url):
    """
    Download json endpoint
    Parameter url: URL
    returns string (json)
    """
    try:
        file = requests.get(url)
    except ConnectionError as e:
        raise e

    return file.json()


def list_spaces():
    """
    list all directory entries
    """
    try:
        directory = download(DIR_URL)
    except ConnectionError:
        raise
    # print all entries
    for name in directory:
        print('{}'.format(name))


def details(data, verbose):
    """Show all details"""
    print(json.dumps(data, indent=4, sort_keys=True))


def status(json_data, verbose):
    """Ermittelt aus dem JSON den Status des Hackerspace"""
    if verbose is True:
        pass

    if json_data['state']['open'] is False:
        print('{} is closed'.format(str(json_data['space'])))
        return False

    print('{} is open'.format(str(json_data['space'])))
    return True


def getHomepage(json_data, verbose):
    """Ermittelt aus dem Json die Homepage des Hackerspace"""
    if json_data['url']:
        print('opening {}'.format(json_data['url']))
        subprocess.run(['firefox', json_data['url']])
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

    if args.verbose:
        debug = True
    else:
        debug = False

    # get the full hackspace list and exit
    if args.list:
        list_spaces()
        sys.exit(0)

    try:
        data = download(getspaceurl(args.name, debug))
    except ConnectionError:
        print('not connected')
        sys.exit(1)

    if args.details:
        details(data, debug)
        sys.exit(0)

    if args.web:
        getHomepage(data, debug)
        sys.exit(0)

    if status(data, verbose=False):
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Show Space Status')
    parser.add_argument('-n', '--name', help='Name of Hackerspace', default='LeineLab')
    parser.add_argument('-d', '--details', help='Shows more details of Hackerspace')
    parser.add_argument('-l', '--list', action='store_true', help='List all Hackspaces on Spaceapi')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('-w', '--web', action='store_true', help='get homepage url')
    args = parser.parse_args()

    main(args)
