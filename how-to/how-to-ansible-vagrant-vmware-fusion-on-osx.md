# How to Set Up: Vagrant, VMWare Fusion, Ansible and Docker Macine on OSX

## Pre-Conditions
To set up Vagrant, there are really two choices: manually download the files from the website and set them up manually, 
or use the excellent ['Brew' package manager](http://brew.sh/) for OSX.  I chose this route as Brew makes it simple to 
update/upgrade and we'll be installing a number of other packages that are supported in the 'Brew'-verse.

There are two components to Brew: Brew itself, and 'Brew Cask'.  Brew istelf contains ports of the standard
Linux packages to OSX (ports also does this btw).  Brew Cask enables support for any type of installer package, making
it possible to install not only Linux packages but any OS software, so this enables Brew to serve as general package
manager for OSX applications as well as linux ports.

> Brew Cask is contained as part of the Brew packaging system, so you no longer need to install it

> Note: be sure to check the version of Vagrant, et al installed this way.  Though convenient -- and it seems to be up to
date -- often the versions included with some of the linux distros are out of date.

Install Brew:
* Go to http://brew.sh/ and follow the instructions for installing Brew.

Issue the following after installation and fix any issues that it reports before continuing.
```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ brew doctor
```

Once the ```brew doctor``` has given your environment a clean bill of health,
move on to installing the remaining pre-conditions:

```
$ brew install brew-cask      # should be included in recent ```brew``` installs
$ brew install vmware-fusion  # better for paravirt
$ brew install virtualbox     # default for many of the tools
$ brew install packer         # vagrant box packaging tool
```

## Proceed

### Installing Ansible
```
$ brew install ansible
```

### Installing Vagrant

```
$ brew install vagrant
$ vagrant --version     # to validate basic install
```

Now with the basic instal of Vagrant completed, we need to get busy setting up some comfiguration
for both Vagrant and the additional components we have in the system:
```
# install vmware plugin for vagrant
$ vagrant plugin install vagrant-vmware-fusion
$ vagrant plugin license vagrant-vmware-fusion /Users/*name*/Documents/Vagrant/license.lic
```

Then create a vagrant directory.  I also add a sub-directory for local vagrant boxes [optional]

```
$ mkdir -p ~/vagrant/demo
$ export REPO_ROOT=${REPO_ROOT:-"~/repository"}
$ export VAGRANT_ROOT=${VAGRANT_ROOT:-"$(cd ~/vagrant && pwd)"}
$ alias vr='cd "$VAGRANT_ROOT"'   # optional shortcut
```

The Vagrant instructions seem to be missing a pre-condition.  Use the following to get the sample precise64
box up and going on osx:

```
$ cd "$VAGRANT_ROOT/demo"
$ vagrant box add hashicorp/precise64 # seems to be missing from Hashicorp quickstart
==> box: Loading metadata for box 'hashicorp/precise64'
    box: URL: https://atlas.hashicorp.com/hashicorp/precise64
This box can work with multiple providers! The providers that it
can work with are listed below. Please review the list and choose
the provider you will be working with.

1) hyperv
2) virtualbox
3) vmware_fusion

Enter your choice: 3
==> box: Adding box 'hashicorp/precise64' (v1.1.0) for provider: vmware_fusion
    box: Downloading: https://atlas.hashicorp.com/hashicorp/boxes/precise64/versions/1.1.0/providers/vmware_fusion.box
==> box: Successfully added box 'hashicorp/precise64' (v1.1.0) for 'vmware_fusion'!
```
##Proceed to Run
Let's test out the base system before complicating it with additional integrations.  The ```precise64``` box
is a default install of Ubuntu 12.04 that works with a broad array of hardware.  When the box was installed,
a directory was created for it in the current working directory.  Now, when we initialize vagrant, it will
create a ```Vagrantfile``` in the current working directory as well.  So, we want to drop into the box directory
before creating this file (you can move it manually if you made a mistake).

```
$ cd precise64
$ vagrant init hashicorp/precise64      # you'll want to specify the box as this info goes into the Vagrantfile
$ vagrant up
```

>A little known magic trick is that whatever is in this vagrant project directory is replicated securely
over to the guest instance and mounted as a volume in the appropriate operating-system-specific location
(/mnt/hgfs/-vagrant on the hashicorp/precise64 box).  This can come in handy when you want to automatically
provision a few scripts over or get something back.

Given the above information on replication going in the background for us, there are a couple of places that you
can immediately take advantage of this.  Number one, of course, is the ```Vagrantfile```.  This file is replicated
over and invoked on the appropriate lifecycle events.  The file is in ruby, so be aware of that when you modify it.

Some quick keys:
The following portion of the Vagrantfile represents the main provisioning function.  The '2' defines the configuration
version and is hard-coded per convention.  Presume what is executed inside will be executed against the guest instance
```
Vagrant.configure(2) do |config|
    ...
end
```
Checkout the [chapter on Vagrantfiles](https://www.vagrantup.com/docs/vagrantfile/) for more information

### Notes on Vagrant Search Paths
* One of the important things to note is how Vagrant looks for the Vagrantfiles.  Its default search path starts in the current
directory and continues looking in each parent directory up to the root of the volume until if finds a Vagrantfile.
Including /Vagrantfile.  This can be helpful so that you can run from any directory in the project but has some
odd ramifications once it bubbles up past the project base directory.
* Vagrant actually loads a series of Vagrantfiles and merges them.  This enables settings to be broken into
user-settings, project-settings, and default, among other things.  But when merging, Vagrant will not override something
set in a previous file.  So be aware of that when splitting things up -- this usually won't be a problem.
The search path is:
  1. Vagrantfile packaged with the 'box' that is to be used for a given machine.
  1. Vagrantfile in your Vagrant home directory (defaults to ~/.vagrant.d).
  1. Vagrantfile from the project directory search path (this is the one that you'll be modifying most of the time)
  1. multi-machine overrides if any
  1. provider-specific overrides if any

##Troubleshooting
* Check the firewall rules to make sure that hashicorp is a valid destination from the Terminal you are using.

* Check the versions of the installed components.  This article installed them using the ```brew``` package
manager as it had the latest versions as of this writing, however its possible that there
has since been a version mismatch introduced
```
brew --version
brew cask info virtualbox
brew cask info vmware-fusion
vagrant version
vagrant plugin list
vagrant box list
ansible --version
```

## Links to great articles
Here are some links to some great articles that served as some of the direction and reference for this.  
Please note: there are discrepancies between these articles and this one.  If this document references it, 
then this information is (likely) newer unless your configuration is different.  Please use your own 
recognizance however and don't leap blindly.  Trust, but verify.

* http://kendrickcoleman.com/index.php/Tech-Blog/how-to-setup-your-mac-with-vmware-fusion-vagrant-and-boot2docker.html
