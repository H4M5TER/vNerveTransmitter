# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vNerve/vdb/vdb.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vNerve/vdb/vdb.proto',
  package='vNerve.vdb',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x14vNerve/vdb/vdb.proto\x12\nvNerve.vdb\"\x10\n\x0eGetVtbsRequest\"7\n\x10VtuberCollection\x12#\n\x07vtubers\x18\x01 \x03(\x0b\x32\x12.vNerve.vdb.Vtuber\"\xe4\x01\n\x06Vtuber\x12\x0c\n\x04uuid\x18\x01 \x01(\t\x12$\n\x04type\x18\x02 \x01(\x0e\x32\x16.vNerve.vdb.VtuberType\x12\x0b\n\x03\x62ot\x18\x03 \x01(\x08\x12%\n\x08\x61\x63\x63ounts\x18\x04 \x03(\x0b\x32\x13.vNerve.vdb.Account\x12\x12\n\ngroup_uuid\x18\x05 \x01(\t\x12\x10\n\x08model_2d\x18\x06 \x01(\x08\x12\x10\n\x08model_3d\x18\x07 \x01(\x08\x12\x1c\n\x14model_2d_artist_uuid\x18\x08 \x01(\t\x12\x1c\n\x14model_3d_artist_uuid\x18\t \x01(\t\"\x94\x02\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12-\n\x0c\x61\x63\x63ount_type\x18\x02 \x01(\x0e\x32\x17.vNerve.vdb.AccountType\x12\x35\n\x10\x61\x63\x63ount_platform\x18\x03 \x01(\x0e\x32\x1b.vNerve.vdb.AccountPlatform\x12\r\n\x05\x65xtra\x18\x04 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x42\n\x10name_translation\x18\x06 \x03(\x0b\x32(.vNerve.vdb.Account.NameTranslationEntry\x1a\x36\n\x14NameTranslationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01*E\n\nVtuberType\x12\x17\n\x13UNKNOWN_VTUBER_TYPE\x10\x00\x12\n\n\x06VTUBER\x10\x01\x12\t\n\x05GROUP\x10\x02\x12\x07\n\x03\x46\x41N\x10\x03*@\n\x0b\x41\x63\x63ountType\x12\x18\n\x14UNKNOWN_ACCOUNT_TYPE\x10\x00\x12\x0c\n\x08OFFICIAL\x10\x01\x12\t\n\x05RELAY\x10\x02*\x90\x03\n\x0f\x41\x63\x63ountPlatform\x12\x14\n\x10UNKNOWN_PLATFORM\x10\x00\x12\x0c\n\x08\x42ILIBILI\x10\x01\x12\x0b\n\x07TWITTER\x10\x02\x12\x0b\n\x07YOUTUBE\x10\x03\x12\r\n\tUSERLOCAL\x10\x04\x12\t\n\x05PEING\x10\x05\x12\x0f\n\x0bMARSHMALLOW\x10\x06\x12\t\n\x05PIXIV\x10\x07\x12\t\n\x05WEIBO\x10\x08\x12\t\n\x05\x42OOTH\x10\t\x12\n\n\x06\x41\x46\x44IAN\x10\n\x12\x07\n\x03WEB\x10\x0b\x12\t\n\x05\x45MAIL\x10\x0c\x12\r\n\tINSTAGRAM\x10\r\x12\x0b\n\x07POPIASK\x10\x0e\x12\x10\n\x0c\x41MAZON_CO_JP\x10\x0f\x12\n\n\x06TWITCH\x10\x10\x12\x0c\n\x08NICONICO\x10\x11\x12\x0c\n\x08\x46\x41\x43\x45\x42OOK\x10\x12\x12\r\n\tTEESPRING\x10\x13\x12\x0b\n\x07PATREON\x10\x14\x12\x0c\n\x08JVCMUSIC\x10\x15\x12\t\n\x05\x43I_EN\x10\x16\x12\n\n\x06GITHUB\x10\x17\x12\x08\n\x04LINE\x10\x18\x12\n\n\x06TIKTOK\x10\x19\x12\n\n\x06\x46\x41NTIA\x10\x1a\x12\x0c\n\x08SHOWROOM\x10\x1b\x12\x0c\n\x08TELEGRAM\x10\x1c\x32\xf3\x01\n\x0eVtuberDatabase\x12K\n\rGetAllVtubers\x12\x1a.vNerve.vdb.GetVtbsRequest\x1a\x1c.vNerve.vdb.VtuberCollection\"\x00\x12J\n\x0cGetAllGroups\x12\x1a.vNerve.vdb.GetVtbsRequest\x1a\x1c.vNerve.vdb.VtuberCollection\"\x00\x12H\n\nGetAllFans\x12\x1a.vNerve.vdb.GetVtbsRequest\x1a\x1c.vNerve.vdb.VtuberCollection\"\x00\x62\x06proto3'
)

_VTUBERTYPE = _descriptor.EnumDescriptor(
  name='VtuberType',
  full_name='vNerve.vdb.VtuberType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VTUBER_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VTUBER', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GROUP', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAN', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=621,
  serialized_end=690,
)
_sym_db.RegisterEnumDescriptor(_VTUBERTYPE)

VtuberType = enum_type_wrapper.EnumTypeWrapper(_VTUBERTYPE)
_ACCOUNTTYPE = _descriptor.EnumDescriptor(
  name='AccountType',
  full_name='vNerve.vdb.AccountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_ACCOUNT_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OFFICIAL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RELAY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=692,
  serialized_end=756,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTTYPE)

AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
_ACCOUNTPLATFORM = _descriptor.EnumDescriptor(
  name='AccountPlatform',
  full_name='vNerve.vdb.AccountPlatform',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_PLATFORM', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BILIBILI', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWITTER', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YOUTUBE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='USERLOCAL', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PEING', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MARSHMALLOW', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PIXIV', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEIBO', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOTH', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AFDIAN', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WEB', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSTAGRAM', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POPIASK', index=14, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AMAZON_CO_JP', index=15, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TWITCH', index=16, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NICONICO', index=17, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FACEBOOK', index=18, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TEESPRING', index=19, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PATREON', index=20, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JVCMUSIC', index=21, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CI_EN', index=22, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GITHUB', index=23, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LINE', index=24, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TIKTOK', index=25, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FANTIA', index=26, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SHOWROOM', index=27, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TELEGRAM', index=28, number=28,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=759,
  serialized_end=1159,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTPLATFORM)

AccountPlatform = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTPLATFORM)
UNKNOWN_VTUBER_TYPE = 0
VTUBER = 1
GROUP = 2
FAN = 3
UNKNOWN_ACCOUNT_TYPE = 0
OFFICIAL = 1
RELAY = 2
UNKNOWN_PLATFORM = 0
BILIBILI = 1
TWITTER = 2
YOUTUBE = 3
USERLOCAL = 4
PEING = 5
MARSHMALLOW = 6
PIXIV = 7
WEIBO = 8
BOOTH = 9
AFDIAN = 10
WEB = 11
EMAIL = 12
INSTAGRAM = 13
POPIASK = 14
AMAZON_CO_JP = 15
TWITCH = 16
NICONICO = 17
FACEBOOK = 18
TEESPRING = 19
PATREON = 20
JVCMUSIC = 21
CI_EN = 22
GITHUB = 23
LINE = 24
TIKTOK = 25
FANTIA = 26
SHOWROOM = 27
TELEGRAM = 28



_GETVTBSREQUEST = _descriptor.Descriptor(
  name='GetVtbsRequest',
  full_name='vNerve.vdb.GetVtbsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=52,
)


_VTUBERCOLLECTION = _descriptor.Descriptor(
  name='VtuberCollection',
  full_name='vNerve.vdb.VtuberCollection',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vtubers', full_name='vNerve.vdb.VtuberCollection.vtubers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=109,
)


_VTUBER = _descriptor.Descriptor(
  name='Vtuber',
  full_name='vNerve.vdb.Vtuber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuid', full_name='vNerve.vdb.Vtuber.uuid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='vNerve.vdb.Vtuber.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bot', full_name='vNerve.vdb.Vtuber.bot', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='accounts', full_name='vNerve.vdb.Vtuber.accounts', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_uuid', full_name='vNerve.vdb.Vtuber.group_uuid', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_2d', full_name='vNerve.vdb.Vtuber.model_2d', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_3d', full_name='vNerve.vdb.Vtuber.model_3d', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_2d_artist_uuid', full_name='vNerve.vdb.Vtuber.model_2d_artist_uuid', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='model_3d_artist_uuid', full_name='vNerve.vdb.Vtuber.model_3d_artist_uuid', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=340,
)


_ACCOUNT_NAMETRANSLATIONENTRY = _descriptor.Descriptor(
  name='NameTranslationEntry',
  full_name='vNerve.vdb.Account.NameTranslationEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='vNerve.vdb.Account.NameTranslationEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='vNerve.vdb.Account.NameTranslationEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=619,
)

_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='vNerve.vdb.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='vNerve.vdb.Account.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_type', full_name='vNerve.vdb.Account.account_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_platform', full_name='vNerve.vdb.Account.account_platform', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra', full_name='vNerve.vdb.Account.extra', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='vNerve.vdb.Account.name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_translation', full_name='vNerve.vdb.Account.name_translation', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_ACCOUNT_NAMETRANSLATIONENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=343,
  serialized_end=619,
)

_VTUBERCOLLECTION.fields_by_name['vtubers'].message_type = _VTUBER
_VTUBER.fields_by_name['type'].enum_type = _VTUBERTYPE
_VTUBER.fields_by_name['accounts'].message_type = _ACCOUNT
_ACCOUNT_NAMETRANSLATIONENTRY.containing_type = _ACCOUNT
_ACCOUNT.fields_by_name['account_type'].enum_type = _ACCOUNTTYPE
_ACCOUNT.fields_by_name['account_platform'].enum_type = _ACCOUNTPLATFORM
_ACCOUNT.fields_by_name['name_translation'].message_type = _ACCOUNT_NAMETRANSLATIONENTRY
DESCRIPTOR.message_types_by_name['GetVtbsRequest'] = _GETVTBSREQUEST
DESCRIPTOR.message_types_by_name['VtuberCollection'] = _VTUBERCOLLECTION
DESCRIPTOR.message_types_by_name['Vtuber'] = _VTUBER
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.enum_types_by_name['VtuberType'] = _VTUBERTYPE
DESCRIPTOR.enum_types_by_name['AccountType'] = _ACCOUNTTYPE
DESCRIPTOR.enum_types_by_name['AccountPlatform'] = _ACCOUNTPLATFORM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetVtbsRequest = _reflection.GeneratedProtocolMessageType('GetVtbsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETVTBSREQUEST,
  '__module__' : 'vNerve.vdb.vdb_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.vdb.GetVtbsRequest)
  })
_sym_db.RegisterMessage(GetVtbsRequest)

VtuberCollection = _reflection.GeneratedProtocolMessageType('VtuberCollection', (_message.Message,), {
  'DESCRIPTOR' : _VTUBERCOLLECTION,
  '__module__' : 'vNerve.vdb.vdb_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.vdb.VtuberCollection)
  })
_sym_db.RegisterMessage(VtuberCollection)

Vtuber = _reflection.GeneratedProtocolMessageType('Vtuber', (_message.Message,), {
  'DESCRIPTOR' : _VTUBER,
  '__module__' : 'vNerve.vdb.vdb_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.vdb.Vtuber)
  })
_sym_db.RegisterMessage(Vtuber)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {

  'NameTranslationEntry' : _reflection.GeneratedProtocolMessageType('NameTranslationEntry', (_message.Message,), {
    'DESCRIPTOR' : _ACCOUNT_NAMETRANSLATIONENTRY,
    '__module__' : 'vNerve.vdb.vdb_pb2'
    # @@protoc_insertion_point(class_scope:vNerve.vdb.Account.NameTranslationEntry)
    })
  ,
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'vNerve.vdb.vdb_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.vdb.Account)
  })
_sym_db.RegisterMessage(Account)
_sym_db.RegisterMessage(Account.NameTranslationEntry)


_ACCOUNT_NAMETRANSLATIONENTRY._options = None

_VTUBERDATABASE = _descriptor.ServiceDescriptor(
  name='VtuberDatabase',
  full_name='vNerve.vdb.VtuberDatabase',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1162,
  serialized_end=1405,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAllVtubers',
    full_name='vNerve.vdb.VtuberDatabase.GetAllVtubers',
    index=0,
    containing_service=None,
    input_type=_GETVTBSREQUEST,
    output_type=_VTUBERCOLLECTION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllGroups',
    full_name='vNerve.vdb.VtuberDatabase.GetAllGroups',
    index=1,
    containing_service=None,
    input_type=_GETVTBSREQUEST,
    output_type=_VTUBERCOLLECTION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllFans',
    full_name='vNerve.vdb.VtuberDatabase.GetAllFans',
    index=2,
    containing_service=None,
    input_type=_GETVTBSREQUEST,
    output_type=_VTUBERCOLLECTION,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_VTUBERDATABASE)

DESCRIPTOR.services_by_name['VtuberDatabase'] = _VTUBERDATABASE

# @@protoc_insertion_point(module_scope)
