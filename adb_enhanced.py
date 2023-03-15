#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import subprocess
import sys
from configparser import ConfigParser

CONFIG_PATH = os.path.expanduser("~/.adb-enhanced.ini")
KEY_ADB_PATH = "adb-path"

config = ConfigParser()
config.read(CONFIG_PATH)
properties = config.defaults()
if properties is None:
    properties = {}


def devices(adb):
    result = []
    raw_output = (
        subprocess.Popen([adb, "devices"], stdout=subprocess.PIPE)
        .communicate()[0]
        .decode("utf-8")
    )
    output = raw_output.split("\n")[1:]
    for output_line in output:
        identifier = output_line.split("\t")[0].strip()
        if len(identifier) > 0:
            result.append(identifier)

    return result


def compute_adb_path():
    result = properties.get(KEY_ADB_PATH)
    if result is None:
        android_home = os.environ.get("ANDROID_HOME")
        if android_home is None:
            print("adb path not found. Have you defined ANDROID_HOME variable?")
        else:
            result = os.path.join(android_home, "platform-tools/adb")
            config.defaults()[KEY_ADB_PATH] = result
            with open(CONFIG_PATH, "w") as output:
                config.write(output)
            print(
                'adb path set to "'
                + result
                + '". Configuration stored in "'
                + CONFIG_PATH
                + '"'
            )
    return result


def prompt_identifier(identifiers):
    for index, identifier in enumerate(identifiers):
        print(" " + str(index) + ": " + identifier)
    print(" a: all devices")

    selection = input("Please select a device: ")
    print(selection)
    if selection == "a":
        return list(identifiers)
    else:
        return [identifiers[int(selection)]]


def main():
    try:
        adb = compute_adb_path()
        if adb is not None:
            args = sys.argv[1:]
            identifiers = devices(adb)
            command = [adb]
            if (
                len(identifiers) <= 1
                or len(args) == 0
                or args[0] == "-s"
                or args[0] == "start-server"
                or args[0] == "kill-server"
                or args[0] == "devices"
            ):
                subprocess.call(command + args)
            else:
                selected_identifiers = prompt_identifier(identifiers)
                for target in selected_identifiers:
                    if len(selected_identifiers) > 0:
                        print(target + ":")
                    device_command = list(command)
                    device_command.append("-s")
                    device_command.append(target)
                    subprocess.call(device_command + args)

    except (KeyboardInterrupt, SystemExit):
        print("")


if __name__ == "__main__":
    main()
