import requests
from util import die

class Jira:
    def __init__(self, url, username, password):
        self.username = username
        self.password = password
        self.url = url

    def create_issue(self, description):
        print "creating issue with description %s" % description
        url = self.url + "issue/" + description
        r = requests.post(url, auth=(self.username, self.password))
        if r.status_code != 200:
            die("failed to create issue do to error '%s'" % r.status_code)
            print r
        return r

    def get_issue(self, issue):
        url = self.url + "issue/" + issue
        print "getting issue '%s'" % url
        r = requests.get(url, auth=(self.username, self.password))
        if r.status_code != 200:
            die("failed to get issue do to error '%s'" % r.status_code)
            print r
        return r;