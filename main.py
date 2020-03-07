"""workenv
Usage:
	main.py new <name>
	main.py setup
	main.py ls
	main.py delete <name>
	main.py <name>
	
Options:
	--version			show version
	
"""
from docopt import docopt
import os
from pathlib import Path
import json

VERSION = '0.0.1'
PATH = "{}/.workenv".format(str(Path.home()))

def setup():
	try:
		os.mkdir(PATH)
	except OSError:
		print("Creation of the directory {} failed".format(PATH))

def new(name):
	config = {
		"working_directory": {
			os.getcwd(): {}
		}
	}
	try:
		with open("{}/{}.json".format(PATH, name), "w+") as config_file:
			config_file.write(json.dumps(config))
	except Exception:
		print("Creation of the file {}.cfg failed".format(name))


def go(name):
	config = {}
	if os.path.isfile("{}/{}.json".format(PATH, name)):
		with open("{}/{}.json".format(PATH, name), "r") as config_file:
			config = json.load(config_file)
		path_list = list(config["working_directory"].keys())
		
def ls():
	for (_,_,filenames) in os.walk(PATH):
		for filename in filenames:
			print(filename[:-5])
		break


def delete(name):
	try:
		os.remove("{}/{}.json".format(PATH, name))
	except Exception:
		print("This working environment does not exists")



if __name__=='__main__':
	arguments = docopt(__doc__, version="workenv {}".format(VERSION))
	if arguments["setup"] is True:
		setup()
	elif arguments["new"] is True:
		new(arguments["<name>"])
	elif arguments["delete"] is True:
		delete(arguments["<name>"])
	elif arguments["ls"] is True:
		ls()
	elif arguments["<name>"]:
		go(arguments["<name>"])