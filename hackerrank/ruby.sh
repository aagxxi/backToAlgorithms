#!/bin/bash

case $1 in
pre)
  ;;
run)
  /usr/bin/ruby $2.rb
  ;;
pos)
  ;;
*)
  echo unknown command, commands: pre run pos
  ;;
esac
