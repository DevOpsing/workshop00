from fabric.api import *

env.shell = "/usr/local/bin/bash -l -c"
jails = { 
        'jail00' : '10.100.182.11',
        'jail01' : '10.100.182.12',
        'jail02' : '10.100.182.13',
        'jail03' : '10.100.182.14',
        'jail04' : '10.100.182.15',
        'jail05' : '10.100.182.16',
        'jail06' : '10.100.182.17',
        'jail07' : '10.100.182.18',
        'jail08' : '10.100.182.19',
        'jail09' : '10.100.182.20',
        }

#env.hosts = jails.keys()

def simple_hello():
    print("Hello")

def variable_hello(name="Joe"):
    print("Hello %s" % name)

def where_am_i():
    run("pwd")

def hostname():
    run("hostname")

def make_jail(host_name, host_ip):
    command = "warden create {} --ipv4={}/24".format(host_name,host_ip)
    sudo(command)

def make_jails():
    for k,v in jails.items():
        make_jail(k,v)

def delete_jail(host_name): 
    command = "warden delete %s --confirm" % host_name
    sudo(command)

def delete_jails():
    for k,v in jails.items():
        delete_jail(k)

def start_jails():
    for k,v in jails.items():
        sudo('warden start %s' %k)

def install_packages(jailname):
    env.shell="/usr/local/bin/warden chroot %s" % jailname
    packages = ['sudo', 'bash', 'zsh', 'ksh93', 'python', 'databases/py-bsddb',
                'databases/py-gdbm', 'databases/py-sqlite3', 'py27-msgpack']
    sudo("pkg install -y %s" % ' '.join(packages))

def make_jail_user(jailname,username):
    env.shell="/usr/local/bin/warden chroot %s" % jailname
    command = "pw useradd -n {} -m".format(username)
    sudo(command)
    env.prompts = { 'New Password:': str(username) + '.password' }
    command = "passwd {}".format(username)
    sudo(command)
    command = "pw groupmod -M {} ".format(username)
    sudo(command)

def push_sudoers(jailname):
    file_name = '/usr/jails/%s/usr/local/etc/sudoers' % jailname
    put('files/sudoers',file_name, use_sudo=True)

def fix_sudoers(jailname):
    file_name = '/usr/jails/%s/usr/local/etc/sudoers' % jailname
    sudo("chown root:wheel %s" % file_name)

def provision_jails():
    for k,v in jails.items():
        make_jail_user(k,'student00')
        install_packages(k)

def provision_sudo():
    for k,v in jails.items():
        push_sudoers(k)
	fix_sudoers(k)

def push_hosts():
    put('files/hosts', '/etc', use_sudo=True)
