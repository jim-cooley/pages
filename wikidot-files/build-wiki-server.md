To consolidate space, I've combined the SVN server, the build server, cruise-control server, and the wiki server.  The purpose for this is that: a) they need to be running together, and b) it saves on Amazon instance costs to have one instance serving split-duty, and c) maybe most importantly, all you need to do to back everything up that you care about is to do a snapshot on this server to S3.

+++ __Prerequisites:__
+++++ Install Linux x64 - LAMP Server ([http://www.ubuntugeek.com/install-gui-in-ubuntu-server.html you can install a GUI if you want], but not needed)
[[code]]
sudo apt-get install xubuntu-desktop
[[/code]]

+++ __Install WebMin__
[[code]]
# pre-requisites
sudo aptitude install perl libnet-ssleay-perl openssl libauthen-pam-perl libpam-runtime libio-pty-perl libmd5-perl
# note: this fails for me on the libmd5-perl install & webmin seems to work fine...
[[/code]]

Edit the sources.list to add-in the webmin repository
[[code]]
sudo xedit /etc/apt/sources.list

#add this line:
deb http://download.webmin.com/download/repository sarge contrib

#save and exit
[[/code]]

Fetch and install the GPG key with which the repository is signed, with the commands : cd /root

[[code]]
wget http://www.webmin.com/jcameron-key.asc
sudo apt-key add jcameron-key.asc
[[/code]]

You will now be able to install with the commands
[[code]]
sudo apt-get update
sudo apt-get install webmin
[[/code]]

Test the installation with your browser via: [https://your-server-ip:10000/ https://your-server-ip:10000/]


+++ __Install Redmine:__ (see [http://www.redmine.org/projects/redmine/wiki/HowTo_Install_Redmine_in_Ubuntu here])
This installs v 0.9.x:
[[code]]
sudo aa-complain /usr/sbin/mysqld # default AppArmor can get in the way
sudo apt-get install redmine redmine-mysql subversion apache2 mysql-server libapache2-mod-passenger
[[/code]]

To try installation w/updated PPA for redmine 1.1:
[[code]]
sudo add-apt-repository ppa:ondrej/redmine
sudo apt-get update
sudo apt-get install redmine  
# or try: sudo apt-get install redmine redmine-mysql subversion redmin-mysql subversion
[[/code]]

Install Apache2, Passenger, and fastcgi mods if you haven't already (LAMP installs Apache2, but...)
[[code]]
sudo apt-get install apache2 libapache2-mod-passenger libapache2-mod-fastcgi
# note: when I did this, Apache2 was installed, but not libapache2-mod-passenger or libapache2-mod-fastcgi.. 
# so worth doing.

# install ruby-dev
sudo apt-get install ruby1.8-dev # redmine is on 1.8
[[/code]]

Create virtual root for redmine (may be already configured, but let's try)
[[code]]
# from webmin:
* click 'apache webserver' from 'servers' menu item
* click 'create virtual host' tab on apache config page
* pick directory and create
[[/code]]

Edit Apache.conf file
[[code]]
# in the apache/modules/passenger.load file, add:
LoadModule passenger_module /var/lib/gems/1.8/gems/passenger-3.0.2/ext/apache2/mod_passenger.so
PassengerRoot /var/lib/gems/1.8/gems/passenger-3.0.2
PassengerRuby /usr/bin/ruby1.8
[[/code]]

+++++ Notes
* Think the above mixed a couple things together - don't think the above is the right thing (leave defaults)
* Webmin configuration is different (better)
* Configure Redmine via 'admin' account (password 'admin').  Users cannot register on their own.
* Need to setup svn properly (don't have permissions right)
* Need to work on moving redmine data (mysql, pages) to /volumes/redmine & /volumes/mysql for easy backup (via snapshot).


+++++ Old stuff (skip)
* Install Ruby
* Install SVN (server?)
* Install Git

[[code]]
sudo apt-get install ruby
sudo apt-get install subversion
sudo apt-get install git
[[/code]]


+++ __CruiseControl.rb__
* Download and unpack cruisecontrol.rb

[[code]]
sudo git cruisecontrol.rb
[[/code]]

------------------------------------------------------------
Additional Stuff:
* SSH public/private keys: http://www.debuntu.org/ssh-key-based-authentication
* Git server (instead of subversion): http://www.hackido.com/2010/01/installing-git-on-server-ubuntu-or.html
* Also: http://tumblr.intranation.com/post/766290565/how-set-up-your-own-private-git-server-linux
* Installing Redmine w/GIT: *[﻿http://www.x2on.de/2011/04/23/tutorial-redmine-with-git-and-gitosis-on-ubuntu-11-04 here]
* *[http://www.redmine.org/projects/redmine/wiki/HowTos Redmine HowTos]