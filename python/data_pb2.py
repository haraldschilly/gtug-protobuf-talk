# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='data.proto',
  package='test',
  serialized_pb='\n\ndata.proto\x12\x04test\"S\n\x06Member\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03\x61ge\x18\x02 \x02(\x05\x12\x1f\n\x06skills\x18\x03 \x03(\x0e\x32\x0b.test.SkillB\x02\x10\x01\x12\r\n\x05\x65mail\x18\x04 \x01(\t\"2\n\x04\x43lub\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x1c\n\x06member\x18\x02 \x03(\x0b\x32\x0c.test.Member\"\x18\n\x05Reply\x12\x0f\n\x07\x61verage\x18\x01 \x02(\x01*@\n\x05Skill\x12\x07\n\x03\x41SM\x10\x00\x12\x05\n\x01\x43\x10\x01\x12\x07\n\x03\x43pp\x10\x02\x12\x08\n\x04Java\x10\x03\x12\n\n\x06Python\x10\x04\x12\x08\n\x04Perl\x10\x05')

_SKILL = descriptor.EnumDescriptor(
  name='Skill',
  full_name='test.Skill',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='ASM', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='C', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Cpp', index=2, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Java', index=3, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Python', index=4, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='Perl', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=183,
  serialized_end=247,
)


ASM = 0
C = 1
Cpp = 2
Java = 3
Python = 4
Perl = 5



_MEMBER = descriptor.Descriptor(
  name='Member',
  full_name='test.Member',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='test.Member.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='age', full_name='test.Member.age', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='skills', full_name='test.Member.skills', index=2,
      number=3, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='email', full_name='test.Member.email', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=20,
  serialized_end=103,
)


_CLUB = descriptor.Descriptor(
  name='Club',
  full_name='test.Club',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='name', full_name='test.Club.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='member', full_name='test.Club.member', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=105,
  serialized_end=155,
)


_REPLY = descriptor.Descriptor(
  name='Reply',
  full_name='test.Reply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='average', full_name='test.Reply.average', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=157,
  serialized_end=181,
)

_MEMBER.fields_by_name['skills'].enum_type = _SKILL
_CLUB.fields_by_name['member'].message_type = _MEMBER
DESCRIPTOR.message_types_by_name['Member'] = _MEMBER
DESCRIPTOR.message_types_by_name['Club'] = _CLUB
DESCRIPTOR.message_types_by_name['Reply'] = _REPLY

class Member(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MEMBER
  
  # @@protoc_insertion_point(class_scope:test.Member)

class Club(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUB
  
  # @@protoc_insertion_point(class_scope:test.Club)

class Reply(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _REPLY
  
  # @@protoc_insertion_point(class_scope:test.Reply)

# @@protoc_insertion_point(module_scope)