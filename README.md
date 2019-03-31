# NessuStrip
Strip hosts and report items from those unwieldy Nessus XML files.

### Installation

NessuStrip requires [Docopt](http://docopt.org/) and [Lxml](https://lxml.de/), .

<<<<<<< HEAD
Install the dependencies.

```sh
$ cd NessuStrip
$ pip install requirements.txt
```
### Todos

 - Add additional strippers
 - Seems to have problems with output files that include spaces

License
----
=======
NessuStrip host <ip> INPUT-FILE [OUTPUT-FILE]
NessuStrip plugin <id> INPUT-FILE [OUTPUT-FILE]
NessuStrip severity (none|low|medium|high|critical) INPUT-FILE [OUTPUT-FILE]
NessuStrip (-h | --help)
NessuStrip (-v | --version)

* Note: Output file is optional. Defaults to 'NessuStrip-Output.nessus' in CWD

Options:
-h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show this screen and exit
-v, --version&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print the NessuStrip version

The following strippers are currently available :) :
host&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove an entire host's findings by IP address
plugin&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove findings by Nessus plugin ID
severity&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove findings by risk rating
>>>>>>> d7740a53bd67ed1bfb25c30779b4837f699f4787

MIT License

**Free Software, Hell Yeah!**
