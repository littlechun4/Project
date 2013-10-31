#!/bin/bash
cd /sys/kernel/debug/tracing
# stop logging
echo 0 > tracing_on
echo nop > current_tracer
# set current tracer as function_graph
echo function_graph > current_tracer
# clear trce ring buffer
echo > trace
# add some information to function_graph
echo funcgraph-proc >> trace_options
echo sys_write > set_graph_function
# start logging
echo 1 > tracing_on
# start testing
dd if=/dev/zero of=/home/selin/temp bs=1M count=1024 oflag=direct conv=fdatasync

# save logs to file
cat trace > /home/selin/project/trace.txt
# disable logging
echo 0 > tracing_on

# remove test file
rm /home/selin/temp
