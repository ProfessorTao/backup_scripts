
#coding:utf-8

import sys, os

shard_file = sys.argv[1]
shard_list = []

src_path = "/home/work/taotianyi/mongodb_clusters"
des_path = "/home/work/publish/scripts/mongodb_clusters"

fp = open(shard_file, 'r')
for line in fp:
    shard_list.append(line.strip())
fp.close()


for item in shard_list:
    print item

    cmd_sh = "mkdir -p %s; exit" % (des_path)
    #cmd_sh = "rm -rf %s; mkdir -p %s; exit" % (des_path, des_path)
    cmd = "ssh %s %s" % (item, cmd_sh)
    os.system(cmd)

    cmd = "scp %s/* %s:%s" % (src_path, item, des_path)
    print cmd
    os.system(cmd)

    cmd_sh = "sh %s/run_mongo_sharding_start.sh; exit" % (des_path)
    cmd = "ssh %s %s" % (item, cmd_sh)
    os.system(cmd)

