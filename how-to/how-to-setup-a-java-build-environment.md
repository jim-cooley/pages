#How to Set up a CICD toolchain and JAVA Build Environment on OS X

#Installing
```
brew install maven      # required for Java builds
brew install git        # making sure we have an updated version
brew install git-review # for gerrit workflow
brew cask install java  # easiest method, while we're at it
brew install go         # needed for parts of xenon test infrastructure
brew install jq         # command line JSON processor
```

>Set JAVA_HOME to point to the JDK installed

#Setting up Environment

##IntelliJ
1. Install IntelliJ 2016
1. Install Gerrit Plugin
1. Configure Git/Gerrit

##Loading Project
1. Open the POM.xml (import) and let it do everything automatically

##Comamnd-line Build
* can build on the command line with: ```./mvnw clean install``` to test

##Configure IntelliJ Project 
* can run Maven w/o the ```mvnw``` wrapper:
* open 'Maven Projects Tool' from the ```Tool Windows``` menu item.
* select ```xenon-host```, then expand
* click ```Lifecycle``` and exand
* select ```clean``` and ```install```, then 
* right-click & select 'run, debug, or create xenon-... configuration'

##Running the Sample Host Directly on OS X
* Start the example host, which listens on port 8000 (in the xenon-host directory):
```
$ java -jar xenon-host/target/xenon-host-*-with-dependencies.jar
```

Now, you can connect via ```curl``` as in the following:
```
$ curl -s localhost:8000/core/management | jq .codeProperties
{
  "git.commit.id": "8a29875692bde8bfb8262393749caed72cd8d7f9",
  "git.commit.id.describe-short": "v0.7.5-release-22",
  "git.commit.time": "28.03.2016 @ 12:48:07 PDT",
  "git.commit.id.abbrev": "8a29875",
  "git.commit.id.describe": "v0.7.5-release-22-g8a29875"
}
```

