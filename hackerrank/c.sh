#!/bin/bash

case $1 in
pre)
  rm -f a.out
  cc -Wall -static $3.c
  ;;
run)
  ./a.out
  ;;
pos)
  rm a.out
  ;;
setup)
  ;;
*)
  echo unknown command, commands: pre run pos setup
  ;;
esac

