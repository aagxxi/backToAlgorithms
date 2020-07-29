#!/bin/bash

case $1 in
pre)
  ;;
run)
  /usr/bin/python3 $2.py
  ;;
pos)
  ;;
*)
  echo unknown command, commands: pre run pos
  ;;
esac
