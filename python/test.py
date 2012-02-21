#!/usr/bin/env python
# -*- coding: utf8 -*-

from data_pb2 import *
import random, string

def printMember(self):
  return "%s [%s]" % (self.name, self.age)

members = []
for i in range(10,20):
  m = Member()
  m.name = ''.join((random.choice(string.lowercase) for _ in range(random.randint(5,15))))
  m.age = random.randint(18,100)
  m.skills.extend(random.sample([C, Cpp, Java, Python, Perl, ASM], 2))
  members.append(m)

print map(printMember, members)

haxxors = Club()
haxxors.name = "3l33t h4xx0r5"
haxxors.member.extend(members) # or .add(...)
print haxxors

haxxors_data = haxxors.SerializeToString()

### client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("", 9090))
s.sendall(haxxors_data)
data = s.recv(1024)
reply = Reply()
reply.ParseFromString(data)
print "reply: ", reply
