#!/bin/sh

#hadoop_jar_path='/home/opt/cloudera/parcels/CDH-5.2.0-1.cdh5.2.0.p0.36/jars/hadoop-core-2.5.0-mr1-cdh5.2.0.jar'
hadoop_path='/home/opt/cloudera/parcels/CDH/jars'
hadoop_jar_path=${hadoop_path}'/hadoop-core-2.5.0-mr1-cdh5.2.0.jar'
common_cli_path='/home/opt/cloudera/parcels/CDH/jars/commons-cli-1.2.jar'

soft_classes_path='./classes'

for f in `find ${hadoop_path} -type f -name "*.jar"`
do
  CLASSPATH=$CLASSPATH:$f
done


javac -encoding UTF8 -classpath ${CLASSPATH}:{$common_cli_path}:${soft_classes_path} -d ${soft_classes_path} ./src/IntSumReducer.java
javac -encoding UTF8 -classpath ${CLASSPATH}:{$common_cli_path}:${soft_classes_path} -d ${soft_classes_path} ./src/TokenizerMapper.java
javac -encoding UTF8 -classpath ${CLASSPATH}:{$common_cli_path}:${soft_classes_path} -d ${soft_classes_path} ./src/PVUVCount.java

jar cvf pvuv_count.jar -C ${soft_classes_path} .

