## Caching Pandora with Squid

Let's face it, Pandora is a super-popular music service and if you're working as a sysadmin for even a medium-sized company, this issue has or will come up:  Pandora (and other music or streaming media services) can chew a considerable portion of your bandwidth.

### Faced with this, there are really two options:**
1. Block Pandora and other such streaming services.
2. Deal with the problem by setting up a caching proxy.

We'll set out to deal with this problem, using 'Pandaora' as an example.

| NOTE: Not all streaming services can be cached, based on protocols used.  Secondarily, most (Pandora included) tell you they can't (short content expiry, do-not-cache headers, queries in the url, etc), so its a bit of a challenge to deal with the problem instead of just blocking it.

### Here goes

(note: setup on osx as a workthrough - move to linux distro for page)

We're going to use 'squid' proxy for this.  

#### Step 1: Set it up

```
brew install squid
```
