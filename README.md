== JIRA Templator ==

=== Setup ===

%> sudo su
%> curl https://bootstrap.pypa.io/ez_setup.py -o - | python
%> easy_install pyyaml
%> easy_install requests

%> cp config.yaml.example ~/config.yaml
%> vi ~/config.yaml # and fill in with your project as shown below

== Configuration
Values set in config.yaml are overridden if the same option is set in the command line options
config.yaml
- jira : root URL of JIRA
- project_id : JIRA api id of your project
- username : JIRA username

=== Options ===
    -c, --config : full path to config file (defaults to !/config.yaml)
    -t, --template_name : template to work from (stored in ./templates)
    -d, --template_dir : alternate template directory (defaults to ./templates)
    -p, --project_id : project id to add to
    -h, --host : host for jira
    -b, --base_path : base path to jira
    -u, --username : username to use to log into JIRA
