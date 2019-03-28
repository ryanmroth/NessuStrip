# NessuStrip

Strip hosts and report items from those unwieldy Nessus XML files.

## Installation

1. pip install requirements.txt
2. ./NessuStrip -h

## Usage

Usage: NessuStrip host <ip> INPUT-FILE [OUTPUT-FILE]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NessuStrip plugin <id> INPUT-FILE [OUTPUT-FILE]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NessuStrip severity (none|low|medium|high|critical) INPUT-FILE [OUTPUT-FILE]  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NessuStrip (-h | --help)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;NessuStrip (-v | --version)  
  
* Note: Output file is optional. Defaults to 'NessuStrip-Output.nessus'  
  
Options:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-h, --help&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Show this screen and exit  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-v, --version&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Print the NessuStrip version  

The following strippers are currently available :) :  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove an entire host's findings by IP address  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;plugin&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove findings by Nessus plugin ID  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;severity&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove findings by risk rating  
  
## TODO
  
1. Add additional strippers in the future
