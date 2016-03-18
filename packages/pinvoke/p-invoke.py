#!/usr/local/bin/python

import collections
import shlex, subprocess
import sys


def p_invoke(cmdline):
    print cmdline
    args = shlex.split(cmdline[0])
    try:
        p = subprocess.Popen(args, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    stdin=subprocess.PIPE)
        # note, any input can be passed into communicate and will map to stdin
        out, err = p.communicate()
        rc = p.returncode

        result_ctx = collections.namedtuple('CmdContext', ['rc', 'stdout', 'stderr'])
        result = result_ctx(rc, stdout=out, stderr=sys.stderr)
        return result
        
    except (OSError, ValueError) as e:
        # shell/application error
        print "failed with %s" % e
        pass
    
    return rc

def stream_print(stream):
    for line in stream:
        print "%s" % line


if __name__ == "__main__":
    result = p_invoke(sys.argv[1:])
    print result.stdout
#   stream_print(sys.stdout)
    