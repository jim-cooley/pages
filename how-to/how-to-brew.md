# How to Install the Brew Package Manager on OSX

There are really a number of ways to instll software on OSX: manually download the files from the website and set them up 
manually, or use the excellent ['Brew' package manager](http://brew.sh/) for OSX.  I chose this route as Brew makes it 
simple to update/upgrade and we'll be installing a number of other packages that are supported in the 'Brew'-verse.

There are two components to Brew: Brew itself, and 'Brew Cask'.  Brew istelf contains ports of the standard
Linux packages to OSX (ports also does this btw).  Brew Cask enables support for any type of installer package, making
it possible to install not only Linux packages but any OS software, so this enables Brew to serve as general package
manager for OSX applications as well as linux ports.

> Brew Cask is contained as part of the Brew packaging system, so you no longer need to install it separately.  It will 
be ready for use once Brew is installed.

To Install Brew:
* Go to http://brew.sh/ and follow the instructions.

After installation, issue the following command and fix any issues that it reports before continuing.
```
brew doctor 
```
