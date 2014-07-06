
import yaml
import os
import os.path
from os.path import expanduser
from optparse import OptionParser
from collections import namedtuple
from config import Config
from password import Password
from jira.client import JIRA
from template import Template
from util import die


# constants


"""
-- Required
    template : the name of the template to use (from dir specified by -d option)

-- Options
    -a, --all : automatically create all of the subtasks in the template

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

def main():
    parser = OptionParser(usage="%prog <template> [options]")

    # Defaulted
    parser.add_option("-c", "--config", dest="config", help="full path to YAML config file", default=Config.DEFAULT_CONFIG_FILE)

    # Defaulted
    parser.add_option("-a", "--all", dest="auto_all", action="store_true", help="automatically create all of the subtasks in the template")

    # One of these is required
    parser.add_option("-s", "--story", dest="story" , help="Story text to use for the parent story")
    parser.add_option("-i", "--issue", dest="issue", help="JIRA Issue to create all the subtasks under")

    # Most likely in config.yaml, but overridable
    parser.add_option("-e", "--assignee", dest="assignee", help="username of JIRA user to assign tasks and subtasks to")
    parser.add_option("-p", "--project_id", dest="project_id", help="name of template to work from")
    parser.add_option("-j", "--jira", dest="jira", help="JIRA api URL")
    parser.add_option("-u", "--username", dest="username", help="username to log into JIRA with")

    # Most likely defaulted, but possibly from config.yaml
    parser.add_option("-d", "--template_dir", dest="template_dir", help="name of template to work from")

    (options, args) = parser.parse_args()

    if len(args) != 1:
        die('template name not given')

    if not os.path.isfile(options.config):
        die("Config file '%s' does not exist or is not a file" % options.config)

    if not os.access(options.config, os.R_OK):
        die("Config file '%s' is not readable" % options.config)

    if options.story is None and options.issue is None:
        die("You must specify either a JIRA story (-s, --story) to create or a JIRA issue (-i, --issue) to modify")

    template=args[0]

    with open(options.config, 'r') as config_yaml:
        config_dict = yaml.load(config_yaml)


    password = Password()
    config = Config(password.password, template, options, config_dict)

    options = {
        'server': config.jira,
        'rest_api_version' : "latest",
    }

    jira = JIRA(options, basic_auth=(config.username, config.password))
    template = Template(jira, config.assignee, config.template_dir, config.template, config.auto_all, config_dict["issue_config"])

    if config.is_story():
        print "Creating story with description: '%s'" % config.story
        parent = jira.create_issue(config.story)
    else:
        print "Adding sub-tasks to issue: '%s'" % config.issue
        parent = jira.issue(config.issue)

    print parent
    print parent.fields.project.key

    subtasks = template.add_subtasks(parent)
    for subtask in subtasks:
        print subtask
    password.cache_password()

