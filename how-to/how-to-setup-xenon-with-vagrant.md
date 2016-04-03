#How to Setup Xenon with Vagrant

##Installing Vagrant

##Configuring The Project
Vagrant stores the box files in a local directory on your machine.  The easiest way to set this up is with a ./vagrant directory in the project home.  Alternate schems are of course possible.

```
mkdir -p "$XENON_ROOT"/vagrant
```

Next, we need to initialize the Vagrant box.  For now, we're using a convenient one: antarctica/trusty, which is a
ubuntu 14.04 build that seems to be maintained recently (TODO: build a box).

```
cd "$XENON_ROOT"/vagrant
vagrant init antarctica/trusty64

```