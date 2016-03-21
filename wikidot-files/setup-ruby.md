[[f>toc]]

Back to [[[ruby-ref|The Ruby Page]]]

----

+ Basic Ruby Install

This will get the latest stable build of the current recommended version (1.8).
Ruby Gems is required to install & maintain additional Ruby packages.

[[code]]
sudo apt-get install ruby
sudo apt-get install ruby-dev build-essential
sudo apt-get install rubygems
sudo apt-get install libopenssl-ruby			# required for HTTPS
sudo apt-get autoremove
sudo apt-get install ruby-debug-ide --include-dependencies
[[/code]]

++* Note 1: 
* If 'ruby-dev build-essential' is not installed, mkmf won't be installed and you will not be able to install any gems.
* This can probably be condensed to:
* More info on installing RubyGems, including advanced directory management of the install locations, can be found [*http://docs.rubygems.org/read/chapter/3 here]

++* Note 2:
* See [*http://blogs.sun.com/observatory/entry/installer_the_fast_ruby_debugger installing the Fast Ruby Debugger Engine] for more information on installing the ruby-debug-ide.

[[code]]
# unverified

sudo apt-get install ruby-dev build-essential
sudo apt-get install rubygems
sudo apt-get install libopenssl-ruby			# required for HTTPS
[[/code]]

++ Validating Ruby Install
[[code]]
ruby -v								          # displays Ruby version
[[/code]]

+ Basic Gems

[[code]]
sudo gem install hpricot						  # the Hpricot HTML shredding library
sudo gem install rest-open-uri					# drop-in replacement for 'open-uri' that handles POST and other verbs.
sudo gem install builder						  # greatly facilitates HTML, XML generation.
sudo gem install rake						  # standard command-line build for ruby
[[/code]]

++ Validating Gems
[[code]]
gem -v										   # displays gem version
gem search								       # displays gems installed locally
gem search --remote							  # displays gems you could install. 
gem search --remote cloth						# optionally searches for a name/portion of a name
[[/code]]

+ Camping
[[code]]
sudo gem install sqlite3-ruby	# sqlite3 is already installed, could be missing a 'sudo apt-get install sqlite3'
sudo apt-get install mongrel
sudo gem install markaby		# for views
sudo gem install activerecord 	# database
sudo gem install rack		# interface between web apps and database?

sudo gem install camping
# sudo gem install camping-omnibus	# to get the full libs

[[/code]]
Note: Likes Mongrel, but will fall back to webrick

+ Rails
[[code]]
sudo gem install rails
[[/code]]

++* Note: 
* This failed on me the first time.  I played with 'sudo apt-get install' for some libs that could have been missing (but it reported they were current).  
I then re-ran the install and it worked

++ Validating Rails Install
[[code]]
rails -v
rails new path/to/your/new/application
cd path/to/your/new/application
rails server
[[/code]]