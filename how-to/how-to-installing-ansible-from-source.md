# Installing and Running Ansible from Source

Installing and running Ansible from source is pretty easy, check out the more complete documentation here,
and go ahead and clone the project on github:

```
git clone git://github.com/ansible/ansible.git --recursive
cd ./ansible
```

You will need to install 'Pip', and a few modules that Ansible requires.  Pip can be installed 
directly or using 'brew'.  We'll use 'brew' for this walkthrough:

```
# sudo easy_install pip # using easy_install to install pip
brew install pip        # using brew to install pip on OS X

# additional modules:
sudo pip install paramiko PyYAML Jinja2 httplib2 six
```

> Note: Once running the env-setup script you’ll be running from checkout and the default inventory file will be /etc/ansible/hosts. 
> You can optionally specify an inventory file (see Inventory) other than /etc/ansible/hosts:

```
$ echo "127.0.0.1" > ~/ansible_hosts
$ export ANSIBLE_INVENTORY=~/ansible_hosts
```

Now you're ready to start it up!

```
source ./hacking/env-setup
```


## To Update Ansible:

To update Ansible, it is important to remmeber to update the subprojects as well as the main project:

```
git pull --rebase
git submodule update --init --recursive
```
