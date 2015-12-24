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
import logging

import dn

logger = logging.getLogger(__name__)

class Parser(object):
  def __init__(self, text):
    self._text = text

  def parse(self, output):
    with open(output, 'w') as csv:
      print >>csv, "Name, Given Name, Family Name, Name Prefix, " \
        "Phone 1 - Type, Phone 1 - Value, Phone 2 - Type, Phone 2 - Value, " \
        "Phone 3 - Type, Phone 3 - Value, Address 1 - Type, Address 1 - Formatted, " \
        "Email, Occupation"
      record = None
      for l in self._text:
        l = l.strip()
        if not l and record is not None:
          print >>csv, record.csv()
          record = None
          continue
        if l.startswith('#'): continue
        key, value = [x.strip() for x in l.split(':', 1)]
        if key == 'dn': record = dn.DN(value)
        elif key == 'cn': record.cn = value
        elif key == 'displayName': record.displayName = value
        elif key == 'givenName': record.givenName = value
        elif key == 'homePhone': record.homePhone = value
        elif key == 'homePostalAddress': record.homePostalAddress = value
        elif key == 'mail': record.mail = value
        elif key == 'mobile': record.mobile = value
        elif key == 'o': record.o = value
        elif key == 'objectClass': record.objectClass = value
        elif key == 'sn': record.sn = value
        elif key == 'telephoneNumber': record.telephoneNumber = value
        elif key == 'title': record.title = value
        else: logger.error('Key: %s value: %s not supported, ignoring', key, value)
