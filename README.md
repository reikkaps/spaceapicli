# SpaceApiCli

![Python application](https://github.com/reikkaps/spaceapicli/workflows/Python%20application/badge.svg)

a simple cmdline tool to access the hackspace-API from 
the unix console or toolbars like polybar

## Install

1. Clone the repository

	git clone https://github.com/reikkaps/spaceapicli.git
	
2. run setup.py

	python setup.py install
	

## Usage

	usage: SpaceApiCli.py [-h] [-n NAME] [-l] [-v] [-w]

	Show Space Status

	optional arguments:
		-h, --help            show this help message and exit
		-n NAME, --name NAME  Name of Hackerspace
		-l, --list            List all Hackspaces on Spaceapi
		-v, --verbose         Show more Infos of Hackspace
		-w, --web             get homepage url
	

Defaults: without option -n it will get the state of the hackspace 
LeineLab in Hannover, Germany <https://leinelab.org>. 



