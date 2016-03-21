[[code]]
NOTE: You can also use 'dbi', Ruby's direct database interaction layer.  I have installed it

sudo gem install dbi

But it will require much of the mysql-client installation below, so I have not written a page on it yet.
[[/code]]



Simple to install the client tools and server, difficult to configure the Ruby extensions. 

Here's what I think will get you there (the key seems to be step 1).

1. Install MySQL client binaries
[[code]]
sudo apt-get install mysql-client
sudo apt-get install libmysqlclient-dev	# nobody ever tells you to do this step :-)
[[/code]]

2. Install the MySQL/Ruby package from [*http://www.tmtm.org/en/mysql/ruby/ here]
3. Unpack into some random directory (like $HOME/bin/mysql)
4. Move the **lib** and **include** directories from this installation to either a) somewhere on Ruby's path, b) somewhere and modify Ruby's path

Exploring option B.
1. Move them to /usr/local/lib/mysql, and /usr/local/include/mysql
2. Modify the $RUBYLIB environment variable to point to the libs

Back to core instructions:
5. Install the Ruby MySQL Gem
[[code]]
sudo gem install mysql
[[/code]]

Can't guarantee this will get you all the way there, but it's close.

How to Check

I placed my MySQL/Ruby connector in /usr/local/mysql, which could have caused part of the problem (you now need to add it to your RUBYPATH).  Wherever you installed it, 'cd' there and.
[[code]]
ruby extconf.rb
make
ruby ./test.rb -- [hostname] [user] [password] [dbname] [port]
[[/code]]

If this does not work, troubleshoot your setup until it does.

When it does, execute
[[code]]
sudo make install		# you won't have permissions to overwrite the Ruby lib otherwise (the one that doesn't work)
[[/code]]