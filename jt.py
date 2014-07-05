#!/usr/bin/python

import json
import yaml
import os
import os.path
from os.path import expanduser
from optparse import OptionParser

# constants
DEFAULT_CONFIG_PATH=expanduser("~")
DEFAULT_CONFIG_FILENAME="config.yaml"
DEFAULT_CONFIG_FILE=DEFAULT_CONFIG_PATH + "/" + DEFAULT_CONFIG_FILENAME

DEFAULT_TEMPLATE_DIR="./templates"

"""
-- Required
    template : the name of the template to use (from dir specified by -d option)

-- One of these is required
    -s, --story : Story text to use for the parent story
    -i, --issue : JIRA Issue to create all the subtasks under

-- Defaulted
    -c, -config : full path to YAML config file (defaults to ~/config.yaml)

-- Most likely in config.yaml, but overridable
    -p, --project_id : project id to add to
    -j, --jira : Complete URL for JIRA

-- Most likely defaulted, but possibly from config.yaml
    -d, --template_dir : alternate template directory (defaults to ./templates)
"""

parser = OptionParser(usage="%prog <template> [options]")

# Defaulted
parser.add_option("-c", "--config", dest="config", help="full path to YAML config file", default=DEFAULT_CONFIG_FILE)

# One of these is required
parser.add_option("-s", "--story", dest="story" , help="Story text to use for the parent story")
parser.add_option("-i", "--issue", dest="issue", help="JIRA Issue to create all the subtasks under")

# Most likely in config.yaml, but overridable
parser.add_option("-p", "--project_id", dest="project_id", help="name of template to work from")
parser.add_option("-j", "--jira", dest="jira", help="JIRA api URL")
parser.add_option("-u", "--username", dest="username", help="username to log into JIRA with")

# Most likely defaulted, but possibly from config.yaml
parser.add_option("-d", "--template_dir", dest="template_dir", help="name of template to work from")

(options, args) = parser.parse_args()

def die(msg):
    print(msg)
    exit(-1)

if len(args) != 1:
    die('template name not given')

if not os.path.isfile(options.config):
    die("Config file '%s' does not exist or is not a file" % options.config)

if not os.access(options.config, os.R_OK):
    die("Config file '%s' is not readable" % options.config)

template=args[0]
with open(options.config, 'r') as config_yaml:
    yaml.load(config_yaml)

