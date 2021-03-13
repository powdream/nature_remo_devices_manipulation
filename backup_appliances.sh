#!/usr/bin/env sh

temp="$(pip list | grep requests)"
if [ -z "$temp" ]; then
  pip install requests
fi

python backup_appliances.py $@
