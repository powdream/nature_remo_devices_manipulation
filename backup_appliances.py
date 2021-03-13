#!/usr/bin/env python

import requests
import json
from os import environ
from datetime import date
from pathlib import Path

URL_PREFIX='https://api.nature.global'
ACCESS_TOKEN=environ.get('NATURE_REMO_CLOUD_ACCESS_TOKEN')
HEADERS={
  'authorization': f'Bearer {ACCESS_TOKEN}',
  'accept': 'application/json'}

def is_ok(response: requests.Response) -> bool:
  return response.status_code == 200

def api(path: str) -> str:
  return f'{URL_PREFIX}{path}'

def get_appliances() -> object:
  response = requests.get(api('/1/appliances'), headers=HEADERS)
  if is_ok(response):
    return response.json()
  else:
    return None
  pass

def get_devices() -> object:
  response = requests.get(api('/1/devices'), headers=HEADERS)
  if is_ok(response):
    return response.json()
  else:
    return None
  pass

def backup_object(obj: object, target_filepath: Path):
  # Ensure the parent's existence.
  target_filepath.parent.mkdir(parents=True, exist_ok=True)
  with target_filepath.open(mode='w') as f:
    json.dump(obj, f, indent=2)
  pass

if __name__ == '__main__':
  print(f'ACCESS_TOKEN={ACCESS_TOKEN}')
  today = date.today()

  applieances = get_appliances()
  if applieances != None:
    backup_object(applieances, Path(f'./backup/{str(today)}/appliances.json'))
    pass

  devices = get_devices()
  if devices != None:
    backup_object(devices, Path(f'./backup/{str(today)}/devices.json'))
    pass
  pass
