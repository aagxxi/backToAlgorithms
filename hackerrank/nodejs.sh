#!/bin/bash

STARTPATH="$( /bin/pwd -P )"
SCRIPTPATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; /bin/pwd -P )"

case $1 in
pre)
  ;;
run)
  source ${SCRIPTPATH}/.nenv/bin/activate
  node $2.js
  deactivate_node
  ;;
pos)
  ;;
setup)
  cd ${SCRIPTPATH}
  echo Installing NodeJS environment at `/bin/pwd -P`/.nenv
  nodeenv -j 4 --force --clean-src -v .nenv
  ;;
*)
  echo unknown command, commands: pre run pos setup
  ;;
esac
