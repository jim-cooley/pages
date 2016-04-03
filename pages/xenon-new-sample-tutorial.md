# HA Example Tutorial

## The Problem
If we use ExampleTaskService. We will not exactly show a task restarting and continuing to do work, but we will show node restart and task services being loaded again, in their last known state. Here is what i recommend.

Your tutorial:
1. shows how to join 3 nodes (using --peerNodes, just like in MultiNodeTutorial

2. discusses how membershipQuorum is set automatically, when peerNodes is set, to majority. Your tutorial sets it to total number of nodes, and explains that is the safest thing, when starting a cluster, since then we wait for all nodes to be available

3. Your tutorials shows how quorum can be set explicitly using a JVM xenon property (see NodeState.java, membershipQuorum, and setting it using a command line jvm property: -Dxenon.NodeState.membershipQuorum=3

4. your tutorial, using xenon, issues a bunch of POSTs to the example task service factory, creating these tasks. It shows them going through their stages by doing a query, with INCLUDE_ALL_VERSIONS,

5. you stop one node (either with Ctrl-C, or better, sending a DELETE to /core/management on one of the nodes

6. since quorum is still set to 3, you show how doing a POST to create a new task fails

7. You relax the quorum, by sending a UpdateQuorumRequest PATCH to one of the remaining nodes, to the core/node-groupds/default, with groupUpdate=true (in the body). Set membershipQuorum=2

8. try step 6 again, now it should work

9. discuss how synchronization automatically occurs (there will be log messages) and a factory will rebalance services between the remaining 2 nodes, assigning new oenrs in the services

10. now restart the node you stopped

11. demonstrate, using a query or a GET to the example task factory of the restarted node, that all the tasks are there. Do this after you check /available on the factory, on all nodes, to show the factory is done synchronization

12. show that the tasks stayed in their FINISHED state, since in handleStart, they check if they are done or not (if not, we need to fix the example task service :wink: )

that should be good for now. We dont show "restart" since its hard to stop a node while task service is in the middle of performing its task, but it shoul dget the point across

##
we should actually focus on building and demonstrating a restartable, owner selected task that does a job, globally across nodes, (similar to bootstrap of users, authz, cleanup) leveraging xenon guarantees.
https://github.com/vmware/xenon/wiki/Highly-Available-Task-Tutorial

Please review the other tutorias, run them after you pull xenon locally and build. then, we can talk further on what this taks can do.  A big part of it will be to capture best practices for multi node deployments :
1) setting quorum properly
2) doing stuff when node group is formed
3) showing restart etc
