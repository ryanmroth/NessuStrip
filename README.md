# NessuStrip

Strip hosts and report items from those unwieldy Nessus XML files.

## Installation

1. pip install requirements.txt
2. chmod +x NessuStrip.py
2. ./NessuStrip.py -h

## Usage

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

## TODO

1. Add additional strippers in the future
2. Seems to have problems with output files including spaces
