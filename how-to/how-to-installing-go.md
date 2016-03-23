# Installing Go on OSX using Brew

The official 'Go' site contains instructions for installing go on a variety of platforms.  Here,
we'll use the ```brew``` package manager.

```
brew update  # always do before installing new packages
brew info go # check the version of 'go' to be installed, ensure its what you expect

brew install go
```

While this configuration will work out of the box (try ```go version```), you need to set a couple 
environment variables for ```go``` before you can install and use packages.  Brew will install
```go``` in a directory that looks like ```/usr/local/Cellar/go/1.6/```.  Set the following in
your ```.bashrc``` file:

```
#go
export GOPATH="/usr/local/Cellar/go/1.6/bin"
export GOROOT="/usr/local/Cellar/go/1.6/libexec"
export PATH="$PATH:$GOROOT:$GOPATH"
```

```GOROOT``` is the location of the go tools, while ```GOPATH``` is a search path to find installed
packages and etc.  Packages installed with ```go get``` will be installed to ```GOPATH```.


