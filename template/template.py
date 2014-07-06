from util import die
import os
import yaml

class Template:
    SUFFIX = ".yaml"

    def __init__(self, jira, assignee, path, filename, auto_all, issue_config):
        self.assignee = assignee
        self.jira = jira
        self.path = path
        self.auto_all  = auto_all
        self.filename = filename if filename.endswith(Template.SUFFIX) else filename + Template.SUFFIX
        self.file = os.path.join(self.path, self.filename)
        self.issue_config = issue_config
        if not os.path.isfile(self.file) and os.access(self.file, os.R_OK):
            die("template %s is not a file" % self.file)
        if not os.access(self.file, os.R_OK):
            die("template %s is not readable" % self.file)
        with open(self.file, 'r') as template_file:
            self.subtasks = yaml.load(template_file)

    def add_subtask(self, parent, description):
        subtask = {
            'assignee' : { 'name' : self.assignee },
            'project' : { 'key': parent.fields.project.key },
            'summary' : description,
            'description' : description,
            'issuetype' : { 'name' : 'Sub-task' },
            'parent' : { 'id' : parent.key},
        }
        print subtask
        subtask.update(self.issue_config)
        print subtask
        child = self.jira.create_issue(fields=subtask)
        return child

    def add_subtasks(self, parent):
        subtasks = []
        for task in self.select_subtasks():
            subtask = self.add_subtask(parent, task)
            subtasks.append(subtask)
        return subtasks

    def select_subtasks(self):
        selected_subtasks = []
        if self.auto_all:
            selected_subtasks.extend(self.subtasks)
        else:
            for task in self.subtasks:
                reply = raw_input("+'%s'? (Y/n) " % task)
                if reply != 'n':
                    selected_subtasks.append(task)
        return selected_subtasks
