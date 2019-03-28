# NessuStrip

Strip hosts and report items from those unwieldy Nessus XML files.

## Installation

1. pip install requirements.txt
2. ./NessuStrip -h

## Usage

Usage:  NessuStrip host <ip> INPUT-FILE [OUTPUT-FILE]  
        NessuStrip plugin <id> INPUT-FILE [OUTPUT-FILE]  
        NessuStrip severity (none|low|medium|high|critical) INPUT-FILE [OUTPUT-FILE]  
        NessuStrip (-h | --help)  
        NessuStrip (-v | --version)  
  
* Note: Output file is optional. Defaults to 'NessuStrip-Output.nessus'  
  
Options:  
   -h, --help         Show this screen and exit  
   -v, --version      Print the NessuStrip version  

The following strippers are currently available :) :  
   host               Remove an entire host's findings by IP address  
   plugin             Remove findings by Nessus plugin ID  
   severity           Remove findings by risk rating  
  
## TODO
  
1. Add additional strippers in the future
