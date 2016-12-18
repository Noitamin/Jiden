#!/bin/bash

NEWPASS=$1
echo "pi:$NEWPASS" | chpasswd
