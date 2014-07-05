== JIRA Templator ==

=== Setup ===

%> sudo su
%> curl https://bootstrap.pypa.io/ez_setup.py -o - | python
%> easy_install pyyaml

== Configuration
Values set in config.yaml are overridden if the same option is set in the command line options
config.yaml
- server : root URL of JIRA
    - host : host name of server
    - base_path : base path of server
- project : project to add to
    - name : name of project to add to
    - id : id of project to add to


=== Options ===
    -c, --config : full path to config file (defaults to !/config.yaml)
    -t, --template_name : template to work from (stored in ./templates)
    -d, --template_dir : alternate template directory (defaults to ./templates)
    -p, --project_id : project id to add to
    -h, --host : host for jira
    -b, --base_path : base path to jira
    -u, --username : username to use to log into JIRA
