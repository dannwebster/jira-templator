from util import die
import os
import yaml

class Template:
    SUFFIX = ".yaml"

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename if filename.endswith(Template.SUFFIX) else filename + Template.SUFFIX
        self.file = os.path.join(self.path, self.filename)
        if not os.path.isfile(self.file) and os.access(self.file, os.R_OK):
            die("template %s is not a file" % self.file)
        if not os.access(self.file, os.R_OK):
            die("template %s is not readable" % self.file)
        with open(self.file, 'r') as template_file:
            self.subtasks = yaml.load(template_file)

    def do_subtask(self, description):
        print description

    def do_subtasks(self, auto_all):
        for task in self.select_subtasks(auto_all):
            self.do_subtask(task)

    def select_subtasks(self, auto_all):
        selected_subtasks = []
        if auto_all:
            selected_subtasks.extend(self.subtasks)
        else:
            for task in self.subtasks:
                reply = raw_input("+'%s'? (Y/n) " % task)
                if reply != 'n':
                    selected_subtasks.append(task)
        return selected_subtasks
