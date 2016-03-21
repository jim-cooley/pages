The instructions on the linked page are missing a couple of key gotchas:

* A bridged connection is not needed on the Host -- ie. you do not have to go to the Windows Networking Center and create a bridged connection with the VBox Host Adapter.  But you **DO** have to use bridged networking and bridge to the Host Adapter (use the actual NIC card, I did).
* You should check to see that the default firewall in Ubuntu is turned off, or add the port filtering rules to allow the port you are binding MySQL to.  
* 'sudo ufw disable', or 'gufw' should do the trick.
* you can also make sure the iptables are empty (don't think this really matters, but check out how to [*http://www.cyberciti.biz/faq/ubuntu-server-disable-firewall/ Disable Firewall on Ubuntu]

 **MAKE ABSOLUTELY SURE YOU:**
* Grant permissions to access the schema with the MySQL user you are trying to access with remotely.  
* Grant permissions to using the login from a remote host.
* Do Not Bind MySQL to 'localhost.  i.e. skip network binding in the MySQL configuration file /etc/mysql/my.cnf, by commenting out the bind_address line.  This will allow connections from any host, so.. watch out.

* Finally, check here: [*http://forge.mysql.com/wiki/Error2003-CantConnectToMySQLServer Can't Connect to MySQL] that should work you through it...
* Here is another link to the [*http://dev.mysql.com/doc/refman/5.0/en/can-not-connect-to-server.html MySQL troubleshooting guide].

 **Troubleshooting**
Remember, there are only a few things that can be going wrong:
# The VBox network connector is not bridged or allowing connections to the host & visa-versa
# MySQL is not allowing external connections.
# MySQL is not started/bound to the port you think it is.
# The 'user' you are using has no permissions to log on remotely, or access tables in any way (see manage users).
# There is a firewall (either Linux,Windows, or both).

Troubleshooting suggestions:
# Check ping (both directions), fix the network until this works.
# With ping, try logging into mysql locally.
# Check the MySQL configuration file for the port and binding info
# Play with the user permissions until it works

See [[[http://www.munkyonline.com/articles/lamp-ubuntu-server-on-virtualbox#mysql|Orignial Instructions]]] for the original instructions, which are pretty good aside from the notes above.