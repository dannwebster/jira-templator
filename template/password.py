from os.path import expanduser
import os.path
import getpass
from util import obscure
from util import deobscure

class Password:
    HOME=expanduser("~")
    CACHE_PATH=HOME
    CACHE_FILENAME=".jira_pwd"
    CACHE_FILE=os.path.join(CACHE_PATH, CACHE_FILENAME)
    PAD='knsp89njkmnasd09iopjk;clkl;asdkl;'

    @staticmethod
    def get_password():
        password = None
        if os.path.isfile(Password.CACHE_FILE) and os.access(Password.CACHE_FILE, os.R_OK):
            with open(Password.CACHE_FILE, 'r') as password_file:
                passw0rd = password_file.readline()
                password = deobscure(passw0rd, Password.PAD)
            print "(Using cached password)"
        if password is None:
            password = getpass.getpass("JIRA Password: ")
        return password

    def __init__(self):
        self.password = Password.get_password()

    def cache_password(self):
        with open(Password.CACHE_FILE, 'w') as password_file:
            passw0rd = obscure(self.password, Password.PAD)
            password_file.write(passw0rd)



