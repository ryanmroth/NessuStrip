#!/usr/bin/env python3

# NessuStrip v1.0
# By Ryan Roth

"""
Usage:  NessuStrip [options] host <ip> INFILE [OUTFILE]
        NessuStrip [options] plugin <id> INFILE [OUTFILE]
        NessuStrip [options] severity (none|low|medium|high|critical) INFILE [OUTFILE]
        NessuStrip (-h | --help)
        NessuStrip (-v | --version)

Options:
   -h, --help         Show this screen and exit
   -v, --version      Print the NessuStrip version

The following strippers are currently available :) :
   host               Remove an entire host's findings by IP address
   plugin             Remove findings by Nessus plugin ID
   severity           Remove findings by risk rating
"""

import ipaddress, os, sys
from docopt import docopt
from lxml import etree

is_windows = sys.platform.startswith('win')

# Console Colors
if is_windows:
    # Windows deserves coloring too :D
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white
    try:
        import win_unicode_console , colorama
        win_unicode_console.enable()
        colorama.init()
        #Now the unicode will work ^_^
    except:
        print("[!] Error: Coloring libraries not installed, no coloring will be used.")
        G = Y = B = R = W = G = Y = B = R = W = ''


else:
    G = '\033[92m'  # green
    Y = '\033[93m'  # yellow
    B = '\033[94m'  # blue
    R = '\033[91m'  # red
    W = '\033[0m'   # white

def banner():
    print(r"""%s
   _  __                 ______      _
  / |/ /__ ___ ___ __ __/ __/ /_____(_)__
 /    / -_|_-<(_-</ // /\ \/ __/ __/ / _ \
/_/|_/\__/___/___/\_,_/___/\__/_/ /_/ .__/
                                   /_/
                                   %s
                # Coded By @f1rstm4tter%s
    """ % (B,G,W))

# Parses docopt arguements, returning only
# those passed in by the user
def parse_args(args):
  try:
    used_args = {}
    for key, val in args.items():
      if args[key]:
        used_args[key] = val
    return used_args
  except KeyError:
    pass

# Validate the input file provided
# Ensure the input file exists and ends in .nessus
# Further validation is done by XML root in the file parser def
def validate_infile(input):
  if not os.path.isfile(input):
    print("%sError: The input file does not exist."% (R))
    return False
  elif not input.lower().endswith(('.nessus')):
    print("%sError: The input file is not a valid Nessus file."% (R))
    return False
  else:
    return True

# Make sure the user gives us a valid IP address
def validate_ip(ip):
  try:
    ipaddress.ip_address(ip)
    return True
  except ValueError as errorCode:
    print("%sError: "% (R) + str(errorCode))
    return False

# Nessus uses specific ranges for its plugin IDs
# We can use this to validate passed ID
def validate_plugin_id(id):
  if 10001 <= int(id) <= 97999 or 99000 <= int(id) <= 699999:
    return True
  else:
    print("%sError: The plugin ID provided is invalid."% (R))
    return False

# Parse the Nessus input file
# Make sure the root element matches Nessus files
def parse_nessus(input):
  try:
    with open(input, 'r') as file:
      xml = file.read()
      file.close()
      print("%s[-] Parsing Nessus input file: %s%s%s%s" % (Y, W, B, input, W))
      tree = etree.fromstring(xml)
      if tree.tag == 'NessusClientData_v2':
        return tree
      else:
        print("%sError: The input file is not a valid Nessus file."% (R))
        pass
  except OSError as errorCode:
    print("%sError: "% (R) + str(errorCode))
    pass

# Strip ReportItems by severity
def strip_severity(severity,input):
  try:
    # Parse input file
    tree = parse_nessus(input)
    print("%s[-] Removing findings with a severity of '"% (Y) + severity.capitalize() + "' from input file.")
    # Use XPATH to find all the risk factors matching the passed severity
    for risk_factor in tree.xpath("//risk_factor[text() = '" + severity.capitalize() + "']/parent::*", namespaces = {"cm": "http://www.nessus.org/cm"}):
      # Find the risk factor parent and strip it away
      risk_factor.getparent().remove(risk_factor)
    return tree
  except ValueError as errorCode:
    print("%sError: "% (R) + str(errorCode))
    pass

# Strip a host
def strip_host(ip,input):
  try:
    # Parse input file
    tree = parse_nessus(input)
    print("%s[-] Removing hosts with an ip of '"% (Y) + ip + "' from input file.")
    # Use XPATH to find all the hosts matching the passed IP
    for host in tree.xpath("//ReportHost[@name='" + ip + "']", namespaces = {"cm": "http://www.nessus.org/cm"}):
      # Remove em
      host.getparent().remove(host)
    return tree
  except ValueError as errorCode:
    print("%sError: "% (R) + str(errorCode))
    pass

# Strip findings by plugin
def strip_plugin(id,input):
  try:
    # Parse input file
    tree = parse_nessus(input)
    print("%s[-] Removing findings with a plugin ID of '"% (Y) + id + "' from input file.")
    # Use XPATH to find all the ReportItems generated by the plugin having the ID
    for plugin in tree.xpath("//ReportItem[@pluginID='" + id + "']", namespaces = {"cm": "http://www.nessus.org/cm"}):
      plugin.getparent().remove(plugin)
    return tree
  except ValueError as errorCode:
    print("%sError: "% (R) + str(errorCode))
    pass

# Writes the output to a file of the user's choosing
def write_output(outfile,input):
  try:
    with open(outfile, 'w') as file:
      print("%s[-] Writing output to file: %s%s%s%s" % (Y, W, B, outfile, W))
      file.write(input)
      file.close()
  except OSError as errorCode:
    print("%sError: "% (R) + str(errorCode) + ".")
    pass

if __name__ == '__main__':
  banner()
  args = docopt(__doc__,
                version='NessuStrip version 1.0',
                options_first=True)
  # Parse the args into dict
  passed_args = parse_args(args)
  # Make sure the input file is good
  if validate_infile(args['INFILE']):
    # Iter the dict args
    for key, val in passed_args.items():
      # We can assume they are stripping severity by checking for these
      if key == 'none' or key == 'low' or key == 'medium' or key == 'high' or key == 'critical':
        # Strip severity
        results = etree.tostring(strip_severity(key,args['INFILE']),encoding='unicode')
      # They want to strip host, don't forget to validate the IP
      if key == 'host' and validate_ip(args['<ip>']):
        # Strip it
        results = etree.tostring(strip_host(args['<ip>'],args['INFILE']),encoding='unicode')
      # They want to strip plugin, don't forget to validate the ID
      if key == 'plugin' and validate_plugin_id(args['<id>']):
        # Strip it
        results = etree.tostring(strip_plugin(args['<id>'],args['INFILE']),encoding='unicode')
    # Write the output file
    # For future: do we care if its .nessus or xml?
    if args['OUTFILE']:
      write_output(args['OUTFILE'],results)
    else:
      write_output("NessuStrip-Output.nessus",results)
