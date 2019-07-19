#!/bin/bash

set username "root"
set password "omgtest"
set hosts "omp_ip"
spawn ssh  $username@$hosts
expect "$username@$hosts's password:"
send -- "$password\n"
expect "#"
send -- "service docker stop\n"