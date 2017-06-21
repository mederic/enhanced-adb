#! /usr/bin/python
# -*- coding: utf-8 -*-

import ConfigParser
import os
import string
import subprocess
import sys

CONFIG_PATH = os.path.expanduser('~/.adb-enhanced.ini')
KEY_ADB_PATH = 'adb-path'

config = ConfigParser.ConfigParser()
config.read(CONFIG_PATH)
properties = config.defaults()
if properties is None:
	properties = {}

def devices():
	result = []
	raw_output = subprocess.Popen(['adb', 'devices'], stdout=subprocess.PIPE).communicate()[0]
	output = string.split(raw_output, '\n')[1:]
	for output_line in output:
		identifier = string.split(output_line, '\t')[0].strip()
		if (len(identifier) > 0):
			result.append(identifier)

	return result

def compute_adb_path():
	result = properties.get(KEY_ADB_PATH)
	if result is None:
		android_home = os.environ.get('ANDROID_HOME')
		if android_home is None:
			print 'adb path not found. Have you defined ANDROID_HOME variable?'
		else:
			result = os.path.join(android_home, 'platform-tools/adb')
			config.defaults()[KEY_ADB_PATH] = result
			with open(CONFIG_PATH, 'w') as output:
				config.write(output)
			print 'adb path set to "' + result + '". Configuration stored in "' + CONFIG_PATH + '"'
	return result


def prompt_identifier(identifiers):
	for index, identifier in enumerate(identifiers):
		print " " + str(index) + ": " + identifier
	return identifiers[input("Please select a device: ")]

def main():
    try:
		adb = compute_adb_path()
		if adb is not None:
			args = sys.argv[1:]
			identifiers = devices()

			command = [adb]
			if (len(identifiers) > 1 and len(args) > 0 
					and args[0] != '-s' 
					and args[0] != 'start-server' 
					and args[0] != 'kill-server' 
					and args[0] != 'devices'):
				command.append('-s')
				command.append(prompt_identifier(identifiers))
				
			subprocess.call(command + args)
    except (KeyboardInterrupt, SystemExit):
    	print ''

if __name__ == "__main__":
    main()


