#
# Copyright 2015 Fasih
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import argparse
import logging
import os
import subprocess

import dn
import parser

logger = logging.getLogger(__name__)

def parse_args():
  arg_parser = argparse.ArgumentParser()
  arg_parser.add_argument('--phone_pin')
  arg_parser.add_argument('--debug', default=False, action='store_true')
  arg_parser.add_argument('--output', default='contacts.csv')

  return arg_parser.parse_args()

def check_binary():
  try:
    subprocess.check_call('btool')
  except OSError:
    logger.error('btool binary not found, please install with:\n\nsudo apt-get install barry-util\n')
    return False
  return True

if __name__ == '__main__':
  args = parse_args()
  logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)
  if not check_binary(): os.sys.exit(1)

  cmd = ['btool', '-c', 'dn']
  if args.phone_pin:
    cmd.extend(['-P', args.phone_pin])

  logger.debug('Executing: %s', ' '.join(cmd))
  text = subprocess.check_output(cmd).splitlines()

  parser.Parser(text).parse(output=args.output)
