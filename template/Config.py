
import os
from os.path import expanduser
from util import die

class Config:
    HOME=expanduser("~")

    DEFAULT_TEMPLATE_DIR="./templates"
    DEFAULT_CONFIG_PATH=HOME
    DEFAULT_CONFIG_FILENAME="config.yaml"
    DEFAULT_CONFIG_FILE=os.path.join(DEFAULT_CONFIG_PATH, DEFAULT_CONFIG_FILENAME)

    @staticmethod
    def opt_or_conf(options, config_dict, name, default_val = None):
        return \
            getattr(options, name) if (getattr(options, name) is not None) \
            else config_dict[name] if (name in config_dict is not None) \
                    else default_val

    def validate(config):
        if config.username is None: die("username required")
        if config.password is None: die("password required")
        if config.template is None: die("template required")
        if config.template_dir is None: die("template_dir required")
        if config.story is None and config.issue is None : die("story or issue is required")
        if config.jira is None: die("jira required")
        if config.project_id is None: die("project_id required")

    def __init__(self, password, template, options, config_dict):
        self.password = password
        self.template = template
        self.story = options.story
        self.issue = options.issue
        self.jira = Config.opt_or_conf(options, config_dict, "jira")
        self.project_id = Config.opt_or_conf(options, config_dict, "project_id")
        self.username = Config.opt_or_conf(options, config_dict, "username")
        self.template_dir = Config.opt_or_conf(options, config_dict, "template_dir", Config.DEFAULT_TEMPLATE_DIR)
        Config.validate(self)

    def is_story(self):
        return self.story is not None

    def is_issue(self):
        return self.issue is not None
