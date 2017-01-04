# enhanced-adb

```
$ adb ...
adb: error: connect failed: more than one device/emulator
```

Tired of seeing that line ? So did I! Let's replace it by:

```
$ adb ...
 0: 4b0ac276
 1: 192.168.56.101:5555
Please select a device:
```

## How to set that up

Let's start by downloading (or cloning) the project wherever you want. Maybe something like `/opt/enhanced-adb`. 
We need then to create an alias to call our enhanced version instead of the real adb executable file. Add the next line to your `~/.bashrc` or (`~/.bash_profile` if you are using mac os):

```
alias adb=<project path>/adb_enhanced.py
```

And that's it!

If needed, you can still bypass the selection using our good ol' `adb -s <identifier>` argument

## Options

The only option supported by now is the path to the actual adb executable file, computed at the very first call using the `ANDROID_HOME` variable, and saved in a configuration file located at `~/.adb-enhanced.ini`. That file can be easily updated afterward.

## Possible future features

- multiple selection to execute the adb command on each devices
- simple adb over wifi connections
- others adb enhancements
- ...

feel free to open an issue for any idea you'd have to improve that tools.

#MIT License

Copyright (c) 2016 Mederic Andrieux

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
