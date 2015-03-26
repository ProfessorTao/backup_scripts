#!/bin/sh

current_path=`pwd`
mongod_path="/home/work/local/mongodb/bin/mongod"
mongos_path="/home/work/local/mongodb/bin/mongos"

config_info=$1
ipaddr=`ifconfig |grep "inet addr" |grep -v "127.0.0.1" |sed 's/:/ /g' |awk '{print $3}'`

init_mongod()
{
    root_path=/home/disk11/mongodb/mongo_data
    mkdir -p $root_path
    cd $root_path
    mkdir db etc log var

    cd $current_path
    cfile=$root_path/etc/mongo_data.conf 

    echo "dbpath=$root_path/db" > $cfile
    echo "pidfilepath=$root_path/var/mongo_data.pid" >> $cfile
    echo "logpath=$root_path/log/mongo_data.log" >> $cfile    
    echo "logappend=false" >> $cfile
    echo "port=16001" >> $cfile
    echo "fork=true" >> $cfile
    echo "directoryperdb=true" >> $cfile
    echo "bind_ip=$ipaddr" >> $cfile
    echo "rest=true" >> $cfile

    #numactl --interleave=all $mongod_path -f $cfile
}

init_mongoc()
{
    root_path=/home/disk11/mongodb/mongo_config
    mkdir -p $root_path
    cd $root_path
    mkdir db etc log var

    cd $current_path
    cfile=$root_path/etc/mongo_config.conf

    echo "configsvr=true" > $cfile
    echo "dbpath=$root_path/db" >>$cfile
    echo "pidfilepath=$root_path/var/mongo_config.pid">>$cfile
    echo "logpath=$root_path/log/mongo_config.log" >>$cfile
    echo "logappend=false" >> $cfile
    echo "port=16011" >> $cfile
    echo "fork=true" >> $cfile
    echo "directoryperdb=true" >> $cfile
    echo "bind_ip=$ipaddr" >> $cfile
    echo "rest=true" >> $cfile

    #numactl --interleave=all $mongod_path -f $cfile
}

init_mongos()
{
    root_path=/home/disk11/mongodb/mongo_server
    mkdir -p $root_path
    cd $root_path
    mkdir db etc log var

    cd $current_path
    cfile=$root_path/etc/mongo_server.conf
    config_value=`python $current_path/read_list.py $config_info`

    echo "configdb=$config_value">$cfile
    echo "port=16000">>$cfile
    echo "pidfilepath=$root_path/var/mongo_server.pid">>$cfile
    echo "logpath=$root_path/log/mongo_server.log">>$cfile
    echo "fork=true">>$cfile

    #numactl --interleave=all $mongos_path -f $cfile
}
    
init_mongod

init_mongoc

#init_mongos


