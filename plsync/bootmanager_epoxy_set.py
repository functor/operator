#!/usr/bin/env python

from planetlab import session
import sys


def main():
    if len(sys.argv) != 2:
        print "Expected one hostname argument."
        sys.exit(1)

    hostname = sys.argv[1]

    api = session.getapi()

    nodes = api.GetNodes({'hostname': hostname},['node_id'])
    if len(nodes) != 1:
        print "Expected to find one node with hostname %s" % hostname
        sys.exit(1)

    node_id = nodes[0]['node_id']
    
    bm_tags = api.GetNodeTags({'node_id': node_id, 'tagname': 'bootmanager'})
    if len(bm_tags) != 0:
        print "bootmanager tag already set for node %s" % hostname
        sys.exit(1)
    
    ret = api.AddNodeTag(node_id, 'bootmanager', 'epoxy')
    if ret <= 0:
        print "Failed to set node tag for node %s" % hostname
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
