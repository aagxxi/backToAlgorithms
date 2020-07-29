#!/bin/bash

case $1 in
pre)
  javac $3.java
  ;;
run)
  java $3
  ;;
pos)
  rm *.class
  ;;
setup)
  ;;
*)
  echo unknown command, commands: pre run pos setup
  ;;
esac

