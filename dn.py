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
class DN(object):
  def __init__(self, dn):
    self._dn = dn.replace(',dn', '')
    self._cn = []
    self._displayName = []
    self._givenName = []
    self._homePhone = []
    self._homePostalAddress = []
    self._mail = []
    self._mobile = []
    self._o = []
    self._objectClass = []
    self._sn = []
    self._telephoneNumber = []
    self._title = []

  @property
  def dn(self): return self._dn

  @property
  def cn(self): return self._cn
  @cn.setter
  def cn(self, v):
    self._cn.append(v)

  @property
  def displayName(self): return self._displayName
  @displayName.setter
  def displayName(self, v):
    self._displayName.append(v)

  @property
  def givenName(self): return self._givenName
  @givenName.setter
  def givenName(self, v):
    self._givenName.append(v)

  @property
  def homePhone(self): return self._homePhone
  @homePhone.setter
  def homePhone(self, v):
    self._homePhone.append(v)

  @property
  def homePostalAddress(self): return self._homePostalAddress
  @homePostalAddress.setter
  def homePostalAddress(self, v):
    self._homePostalAddress.append(v)

  @property
  def mail(self): return self._mail
  @mail.setter
  def mail(self, v):
    self._mail.append(v)

  @property
  def mobile(self): return self._mobile
  @mobile.setter
  def mobile(self, v):
    self._mobile.append(v)

  @property
  def o(self): return self._o
  @o.setter
  def o(self, v):
    self._o.append(v)

  @property
  def objectClass(self): return self._objectClass
  @objectClass.setter
  def objectClass(self, v):
    self._objectClass.append(v)

  @property
  def sn(self): return self._sn
  @sn.setter
  def sn(self, v):
    self._sn.append(v)

  @property
  def telephoneNumber(self): return self._telephoneNumber
  @telephoneNumber.setter
  def telephoneNumber(self, v):
    self._telephoneNumber.append(v)

  @property
  def title(self): return self._title
  @title.setter
  def title(self, v):
    self._title.append(v)

  def csv(self):
    items = []
    items.append(self.displayName)
    items.append(self.givenName)
    items.append(self.sn)
    items.append(self.title)

    items.append(['Home'])
    items.append(self.homePhone)

    items.append(['Mobile'])
    items.append(self.mobile)

    items.append(['Mobile'])
    items.append(self.telephoneNumber)

    items.append(['Home'])
    items.append(self.homePostalAddress)

    items.append(self.mail)

    items.append(self.o)

    return ','.join([' ::: '.join([x.replace(',', ' ') for x in i]) for i in items])

  def __str__(self):
    s = 'DN<dn=%s' % self._dn
    if self.cn != []: s += ', cn=%s' % self.cn
    if self.displayName != []: s += ', displayName=%s' % self.displayName
    if self.givenName != []: s += ', givenName=%s' % self.givenName
    if self.homePhone != []: s += ', homePhone=%s' % self.homePhone
    if self.homePostalAddress != []: s += ', homePostalAddress=%s' % self.homePostalAddress
    if self.mail != []: s += ', mail=%s' % self.mail
    if self.mobile != []: s += ', mobile=%s' % self.mobile
    if self.o != []: s += ', o=%s' % self.o
    if self.objectClass != []: s += ', objectClass=%s' % self.objectClass
    if self.sn != []: s += ', sn=%s' % self.sn
    if self.telephoneNumber != []: s += ', telephoneNumber=%s' % self.telephoneNumber
    if self.title != []: s += ', title=%s' % self.title
    return s + '>'

