from fabric.api import * 

env.shell = "/usr/local/bin/bash -l -c" 

jails = {
            'jail00': '10.100.182.11', 
            'jail01': '10.100.182.12', 
            'jail02': '10.100.182.13', 
            'jail03': '10.100.182.14', 
            'jail04': '10.100.182.15', 
            'jail05': '10.100.182.16', 
            'jail06': '10.100.182.17', 
            'jail07': '10.100.182.18', 
            'jail08': '10.100.182.19', 
            'jail09': '10.100.182.20', 
        }

env.hosts == jails.keys()

def ssh_push():
    run("mkdir -p ~/.ssh")
    put("~/.ssh/id_rsa.pub",".ssh/authorized_keys")
    run("chmod 600 ~/.ssh/authorized_keys")

def patch_salt():
    new_vt_py = ".pyenv/versions/2.7.9/lib/python2.7/site-packages/salt/utils/vt.py"
    put("files/vt.py",new_vt_py)
    run("chmod 644 %s" % new_vt_py)
