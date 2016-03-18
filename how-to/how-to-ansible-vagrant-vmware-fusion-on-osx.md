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

Install Brew:
* Go to http://brew.sh/ and follow the instructions for installing Brew.

Issue the following after installation and fix any issues that it reports before continuing.
```
brew doctor 
```

## Installing Vagrant

```
brew install vagrant
```

Then create a vagrant directory like 

```
mkdir ~/vagrant
```

## Links to great articles
Here are some links to some great articles that served as some of the direction and reference for this.  
Please note: there are discrepancies between these articles and this one.  If this document references it, 
then this information is (likely) newer unless your configuration is different.  Please use your own 
recognizance however and don't leap blindly.  Trust, but verify.

* http://kendrickcoleman.com/index.php/Tech-Blog/how-to-setup-your-mac-with-vmware-fusion-vagrant-and-boot2docker.html
