# NessuStrip
Strip hosts and report items from those unwieldy Nessus XML files.

### Installation

NessuStrip requires [Docopt](http://docopt.org/) and [Lxml](https://lxml.de/).

#### Install the dependencies

```sh
$ cd NessuStrip
$ pip install requirements.txt
```

### Usage

```sh
$ NessuStrip host <ip> INPUT-FILE [OUTPUT-FILE]
$ NessuStrip plugin <id> INPUT-FILE [OUTPUT-FILE]
$ NessuStrip severity (none|low|medium|high|critical) INPUT-FILE [OUTPUT-FILE]
$ NessuStrip (-h | --help)
$ NessuStrip (-v | --version)
```
* Note: Output file is optional. Defaults to 'NessuStrip-Output.nessus' in CWD

### Todos

 - Add additional strippers
 
### License

MIT License

**Free Software, Hell Yeah!**
