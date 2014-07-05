from util import die
import os

class Template:
    SUFFIX = ".yaml"

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename if filename.endswith(Template.SUFFIX) else filename + Template.SUFFIX
        self.file = os.path.join(self.path, self.filename)
        self.subtasks = []
        if not os.path.isfile(self.file) and os.access(self.file, os.R_OK):
            die("template %s is not a file" % self.file)
        if not os.access(self.file, os.R_OK):
            die("template %s is not readable" % self.file)
        with open(self.file, 'r') as template_file:
            for line in template_file:
                self.subtasks.append(line)

    def dosubtask(self, description):
        print description

    def dosubtasks(self):
        for task in self.subtasks:
            self.dosubtask(task)
