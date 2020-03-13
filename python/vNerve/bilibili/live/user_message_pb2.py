# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vNerve/bilibili/live/user_message.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='vNerve/bilibili/live/user_message.proto',
  package='vNerve.bilibili.live',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\'vNerve/bilibili/live/user_message.proto\x12\x14vNerve.bilibili.live\"\xb9\x04\n\x0bUserMessage\x12,\n\x04user\x18\x01 \x01(\x0b\x32\x1e.vNerve.bilibili.live.UserInfo\x12\x37\n\x07\x64\x61nmaku\x18\x02 \x01(\x0b\x32$.vNerve.bilibili.live.DanmakuMessageH\x00\x12\x31\n\x04gift\x18\x03 \x01(\x0b\x32!.vNerve.bilibili.live.GiftMessageH\x00\x12<\n\nsuper_chat\x18\x04 \x01(\x0b\x32&.vNerve.bilibili.live.SuperChatMessageH\x00\x12:\n\tnew_guard\x18\x05 \x01(\x0b\x32%.vNerve.bilibili.live.NewGuardMessageH\x00\x12>\n\x0bwelcome_vip\x18\x06 \x01(\x0b\x32\'.vNerve.bilibili.live.WelcomeVIPMessageH\x00\x12\x42\n\rwelcome_guard\x18\x07 \x01(\x0b\x32).vNerve.bilibili.live.WelcomeGuardMessageH\x00\x12@\n\x0cuser_blocked\x18\x10 \x01(\x0b\x32(.vNerve.bilibili.live.UserBlockedMessageH\x00\x12\x45\n\x0fuser_kicked_out\x18\x11 \x01(\x0b\x32*.vNerve.bilibili.live.UserKickedOutMessageH\x00\x42\t\n\x07payload\"\xc5\x02\n\x08UserInfo\x12\x0b\n\x03uid\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\navatar_url\x18\x03 \x01(\t\x12\x12\n\nuser_level\x18\x04 \x01(\x05\x12\x10\n\x08user_exp\x18\x05 \x01(\x03\x12\x1f\n\x17user_level_border_color\x18\x06 \x01(\x07\x12\r\n\x05\x61\x64min\x18\x07 \x01(\x08\x12\x10\n\x08main_vip\x18\x08 \x01(\x08\x12\x35\n\tvip_level\x18\t \x01(\x0e\x32\".vNerve.bilibili.live.LiveVipLevel\x12\r\n\x05title\x18\n \x01(\t\x12.\n\x05medal\x18\x0b \x01(\x0b\x32\x1f.vNerve.bilibili.live.MedalInfo\x12\x16\n\x0ephone_verified\x18\x0c \x01(\x08\x12\x14\n\x0cregular_user\x18\r \x01(\x08\"_\n\tMedalInfo\x12\x12\n\nmedal_name\x18\x01 \x01(\t\x12\x13\n\x0bmedal_level\x18\x02 \x01(\r\x12\x13\n\x0bmedal_color\x18\x03 \x01(\x07\x12\x14\n\x0cstreamer_uid\x18\x04 \x01(\x04\"u\n\x0e\x44\x61nmakuMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12>\n\x0clottery_type\x18\x02 \x01(\x0e\x32(.vNerve.bilibili.live.LotteryDanmakuType\x12\x12\n\nfrom_guard\x18\x03 \x01(\x08\"\xb4\x01\n\x10SuperChatMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\r\n\x05price\x18\x02 \x01(\r\x12\n\n\x02id\x18\x03 \x01(\r\x12\r\n\x05token\x18\x04 \x01(\t\x12\x11\n\tprice_cny\x18\x05 \x01(\r\x12\x12\n\nprice_coin\x18\x06 \x01(\r\x12\x18\n\x10lasting_time_sec\x18\x07 \x01(\r\x12\x12\n\nstart_time\x18\x08 \x01(\x04\x12\x10\n\x08\x65nd_time\x18\t \x01(\x04\"p\n\x0bGiftMessage\x12\x0f\n\x07is_gold\x18\x01 \x01(\x08\x12\x12\n\ntotal_coin\x18\x02 \x01(\r\x12\x0f\n\x07gift_id\x18\x03 \x01(\r\x12\x11\n\tgift_name\x18\x04 \x01(\t\x12\x18\n\x10gift_single_coin\x18\x05 \x01(\r\"S\n\x11WelcomeVIPMessage\x12/\n\x03vip\x18\x01 \x01(\x0e\x32\".vNerve.bilibili.live.LiveVipLevel\x12\r\n\x05\x61\x64min\x18\x02 \x01(\x08\"F\n\x13WelcomeGuardMessage\x12/\n\x05guard\x18\x01 \x01(\x0e\x32 .vNerve.bilibili.live.GuardLevel\"P\n\x0fNewGuardMessage\x12/\n\x05level\x18\x01 \x01(\x0e\x32 .vNerve.bilibili.live.GuardLevel\x12\x0c\n\x04\x63oin\x18\x02 \x01(\r\"\x14\n\x12UserBlockedMessage\"\x16\n\x14UserKickedOutMessage*3\n\x0cLiveVipLevel\x12\n\n\x06NO_VIP\x10\x00\x12\x0b\n\x07MONTHLY\x10\x01\x12\n\n\x06YEARLY\x10\x02*<\n\x12LotteryDanmakuType\x12\x0e\n\nNO_LOTTERY\x10\x00\x12\t\n\x05STORM\x10\x01\x12\x0b\n\x07LOTTERY\x10\x02*>\n\nGuardLevel\x12\x0c\n\x08NO_GUARD\x10\x00\x12\n\n\x06LEVEL1\x10\x01\x12\n\n\x06LEVEL2\x10\x02\x12\n\n\x06LEVEL3\x10\x03\x62\x06proto3'
)

_LIVEVIPLEVEL = _descriptor.EnumDescriptor(
  name='LiveVipLevel',
  full_name='vNerve.bilibili.live.LiveVipLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_VIP', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MONTHLY', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='YEARLY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1763,
  serialized_end=1814,
)
_sym_db.RegisterEnumDescriptor(_LIVEVIPLEVEL)

LiveVipLevel = enum_type_wrapper.EnumTypeWrapper(_LIVEVIPLEVEL)
_LOTTERYDANMAKUTYPE = _descriptor.EnumDescriptor(
  name='LotteryDanmakuType',
  full_name='vNerve.bilibili.live.LotteryDanmakuType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_LOTTERY', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STORM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOTTERY', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1816,
  serialized_end=1876,
)
_sym_db.RegisterEnumDescriptor(_LOTTERYDANMAKUTYPE)

LotteryDanmakuType = enum_type_wrapper.EnumTypeWrapper(_LOTTERYDANMAKUTYPE)
_GUARDLEVEL = _descriptor.EnumDescriptor(
  name='GuardLevel',
  full_name='vNerve.bilibili.live.GuardLevel',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NO_GUARD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL1', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LEVEL3', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1878,
  serialized_end=1940,
)
_sym_db.RegisterEnumDescriptor(_GUARDLEVEL)

GuardLevel = enum_type_wrapper.EnumTypeWrapper(_GUARDLEVEL)
NO_VIP = 0
MONTHLY = 1
YEARLY = 2
NO_LOTTERY = 0
STORM = 1
LOTTERY = 2
NO_GUARD = 0
LEVEL1 = 1
LEVEL2 = 2
LEVEL3 = 3



_USERMESSAGE = _descriptor.Descriptor(
  name='UserMessage',
  full_name='vNerve.bilibili.live.UserMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user', full_name='vNerve.bilibili.live.UserMessage.user', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='danmaku', full_name='vNerve.bilibili.live.UserMessage.danmaku', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gift', full_name='vNerve.bilibili.live.UserMessage.gift', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='super_chat', full_name='vNerve.bilibili.live.UserMessage.super_chat', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_guard', full_name='vNerve.bilibili.live.UserMessage.new_guard', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='welcome_vip', full_name='vNerve.bilibili.live.UserMessage.welcome_vip', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='welcome_guard', full_name='vNerve.bilibili.live.UserMessage.welcome_guard', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_blocked', full_name='vNerve.bilibili.live.UserMessage.user_blocked', index=7,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_kicked_out', full_name='vNerve.bilibili.live.UserMessage.user_kicked_out', index=8,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='payload', full_name='vNerve.bilibili.live.UserMessage.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=66,
  serialized_end=635,
)


_USERINFO = _descriptor.Descriptor(
  name='UserInfo',
  full_name='vNerve.bilibili.live.UserInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='vNerve.bilibili.live.UserInfo.uid', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='vNerve.bilibili.live.UserInfo.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avatar_url', full_name='vNerve.bilibili.live.UserInfo.avatar_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='vNerve.bilibili.live.UserInfo.user_level', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_exp', full_name='vNerve.bilibili.live.UserInfo.user_exp', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_level_border_color', full_name='vNerve.bilibili.live.UserInfo.user_level_border_color', index=5,
      number=6, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admin', full_name='vNerve.bilibili.live.UserInfo.admin', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='main_vip', full_name='vNerve.bilibili.live.UserInfo.main_vip', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip_level', full_name='vNerve.bilibili.live.UserInfo.vip_level', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='vNerve.bilibili.live.UserInfo.title', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medal', full_name='vNerve.bilibili.live.UserInfo.medal', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone_verified', full_name='vNerve.bilibili.live.UserInfo.phone_verified', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='regular_user', full_name='vNerve.bilibili.live.UserInfo.regular_user', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=638,
  serialized_end=963,
)


_MEDALINFO = _descriptor.Descriptor(
  name='MedalInfo',
  full_name='vNerve.bilibili.live.MedalInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='medal_name', full_name='vNerve.bilibili.live.MedalInfo.medal_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medal_level', full_name='vNerve.bilibili.live.MedalInfo.medal_level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='medal_color', full_name='vNerve.bilibili.live.MedalInfo.medal_color', index=2,
      number=3, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='streamer_uid', full_name='vNerve.bilibili.live.MedalInfo.streamer_uid', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=965,
  serialized_end=1060,
)


_DANMAKUMESSAGE = _descriptor.Descriptor(
  name='DanmakuMessage',
  full_name='vNerve.bilibili.live.DanmakuMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='vNerve.bilibili.live.DanmakuMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lottery_type', full_name='vNerve.bilibili.live.DanmakuMessage.lottery_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_guard', full_name='vNerve.bilibili.live.DanmakuMessage.from_guard', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1062,
  serialized_end=1179,
)


_SUPERCHATMESSAGE = _descriptor.Descriptor(
  name='SuperChatMessage',
  full_name='vNerve.bilibili.live.SuperChatMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='vNerve.bilibili.live.SuperChatMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='vNerve.bilibili.live.SuperChatMessage.price', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='vNerve.bilibili.live.SuperChatMessage.id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token', full_name='vNerve.bilibili.live.SuperChatMessage.token', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_cny', full_name='vNerve.bilibili.live.SuperChatMessage.price_cny', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price_coin', full_name='vNerve.bilibili.live.SuperChatMessage.price_coin', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lasting_time_sec', full_name='vNerve.bilibili.live.SuperChatMessage.lasting_time_sec', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='vNerve.bilibili.live.SuperChatMessage.start_time', index=7,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='vNerve.bilibili.live.SuperChatMessage.end_time', index=8,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1182,
  serialized_end=1362,
)


_GIFTMESSAGE = _descriptor.Descriptor(
  name='GiftMessage',
  full_name='vNerve.bilibili.live.GiftMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_gold', full_name='vNerve.bilibili.live.GiftMessage.is_gold', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_coin', full_name='vNerve.bilibili.live.GiftMessage.total_coin', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gift_id', full_name='vNerve.bilibili.live.GiftMessage.gift_id', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gift_name', full_name='vNerve.bilibili.live.GiftMessage.gift_name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gift_single_coin', full_name='vNerve.bilibili.live.GiftMessage.gift_single_coin', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1364,
  serialized_end=1476,
)


_WELCOMEVIPMESSAGE = _descriptor.Descriptor(
  name='WelcomeVIPMessage',
  full_name='vNerve.bilibili.live.WelcomeVIPMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='vip', full_name='vNerve.bilibili.live.WelcomeVIPMessage.vip', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='admin', full_name='vNerve.bilibili.live.WelcomeVIPMessage.admin', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=1478,
  serialized_end=1561,
)


_WELCOMEGUARDMESSAGE = _descriptor.Descriptor(
  name='WelcomeGuardMessage',
  full_name='vNerve.bilibili.live.WelcomeGuardMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='guard', full_name='vNerve.bilibili.live.WelcomeGuardMessage.guard', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1563,
  serialized_end=1633,
)


_NEWGUARDMESSAGE = _descriptor.Descriptor(
  name='NewGuardMessage',
  full_name='vNerve.bilibili.live.NewGuardMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='vNerve.bilibili.live.NewGuardMessage.level', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coin', full_name='vNerve.bilibili.live.NewGuardMessage.coin', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1635,
  serialized_end=1715,
)


_USERBLOCKEDMESSAGE = _descriptor.Descriptor(
  name='UserBlockedMessage',
  full_name='vNerve.bilibili.live.UserBlockedMessage',
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
  serialized_start=1717,
  serialized_end=1737,
)


_USERKICKEDOUTMESSAGE = _descriptor.Descriptor(
  name='UserKickedOutMessage',
  full_name='vNerve.bilibili.live.UserKickedOutMessage',
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
  serialized_start=1739,
  serialized_end=1761,
)

_USERMESSAGE.fields_by_name['user'].message_type = _USERINFO
_USERMESSAGE.fields_by_name['danmaku'].message_type = _DANMAKUMESSAGE
_USERMESSAGE.fields_by_name['gift'].message_type = _GIFTMESSAGE
_USERMESSAGE.fields_by_name['super_chat'].message_type = _SUPERCHATMESSAGE
_USERMESSAGE.fields_by_name['new_guard'].message_type = _NEWGUARDMESSAGE
_USERMESSAGE.fields_by_name['welcome_vip'].message_type = _WELCOMEVIPMESSAGE
_USERMESSAGE.fields_by_name['welcome_guard'].message_type = _WELCOMEGUARDMESSAGE
_USERMESSAGE.fields_by_name['user_blocked'].message_type = _USERBLOCKEDMESSAGE
_USERMESSAGE.fields_by_name['user_kicked_out'].message_type = _USERKICKEDOUTMESSAGE
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['danmaku'])
_USERMESSAGE.fields_by_name['danmaku'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['gift'])
_USERMESSAGE.fields_by_name['gift'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['super_chat'])
_USERMESSAGE.fields_by_name['super_chat'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['new_guard'])
_USERMESSAGE.fields_by_name['new_guard'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['welcome_vip'])
_USERMESSAGE.fields_by_name['welcome_vip'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['welcome_guard'])
_USERMESSAGE.fields_by_name['welcome_guard'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['user_blocked'])
_USERMESSAGE.fields_by_name['user_blocked'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERMESSAGE.oneofs_by_name['payload'].fields.append(
  _USERMESSAGE.fields_by_name['user_kicked_out'])
_USERMESSAGE.fields_by_name['user_kicked_out'].containing_oneof = _USERMESSAGE.oneofs_by_name['payload']
_USERINFO.fields_by_name['vip_level'].enum_type = _LIVEVIPLEVEL
_USERINFO.fields_by_name['medal'].message_type = _MEDALINFO
_DANMAKUMESSAGE.fields_by_name['lottery_type'].enum_type = _LOTTERYDANMAKUTYPE
_WELCOMEVIPMESSAGE.fields_by_name['vip'].enum_type = _LIVEVIPLEVEL
_WELCOMEGUARDMESSAGE.fields_by_name['guard'].enum_type = _GUARDLEVEL
_NEWGUARDMESSAGE.fields_by_name['level'].enum_type = _GUARDLEVEL
DESCRIPTOR.message_types_by_name['UserMessage'] = _USERMESSAGE
DESCRIPTOR.message_types_by_name['UserInfo'] = _USERINFO
DESCRIPTOR.message_types_by_name['MedalInfo'] = _MEDALINFO
DESCRIPTOR.message_types_by_name['DanmakuMessage'] = _DANMAKUMESSAGE
DESCRIPTOR.message_types_by_name['SuperChatMessage'] = _SUPERCHATMESSAGE
DESCRIPTOR.message_types_by_name['GiftMessage'] = _GIFTMESSAGE
DESCRIPTOR.message_types_by_name['WelcomeVIPMessage'] = _WELCOMEVIPMESSAGE
DESCRIPTOR.message_types_by_name['WelcomeGuardMessage'] = _WELCOMEGUARDMESSAGE
DESCRIPTOR.message_types_by_name['NewGuardMessage'] = _NEWGUARDMESSAGE
DESCRIPTOR.message_types_by_name['UserBlockedMessage'] = _USERBLOCKEDMESSAGE
DESCRIPTOR.message_types_by_name['UserKickedOutMessage'] = _USERKICKEDOUTMESSAGE
DESCRIPTOR.enum_types_by_name['LiveVipLevel'] = _LIVEVIPLEVEL
DESCRIPTOR.enum_types_by_name['LotteryDanmakuType'] = _LOTTERYDANMAKUTYPE
DESCRIPTOR.enum_types_by_name['GuardLevel'] = _GUARDLEVEL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserMessage = _reflection.GeneratedProtocolMessageType('UserMessage', (_message.Message,), {
  'DESCRIPTOR' : _USERMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.UserMessage)
  })
_sym_db.RegisterMessage(UserMessage)

UserInfo = _reflection.GeneratedProtocolMessageType('UserInfo', (_message.Message,), {
  'DESCRIPTOR' : _USERINFO,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.UserInfo)
  })
_sym_db.RegisterMessage(UserInfo)

MedalInfo = _reflection.GeneratedProtocolMessageType('MedalInfo', (_message.Message,), {
  'DESCRIPTOR' : _MEDALINFO,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.MedalInfo)
  })
_sym_db.RegisterMessage(MedalInfo)

DanmakuMessage = _reflection.GeneratedProtocolMessageType('DanmakuMessage', (_message.Message,), {
  'DESCRIPTOR' : _DANMAKUMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.DanmakuMessage)
  })
_sym_db.RegisterMessage(DanmakuMessage)

SuperChatMessage = _reflection.GeneratedProtocolMessageType('SuperChatMessage', (_message.Message,), {
  'DESCRIPTOR' : _SUPERCHATMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.SuperChatMessage)
  })
_sym_db.RegisterMessage(SuperChatMessage)

GiftMessage = _reflection.GeneratedProtocolMessageType('GiftMessage', (_message.Message,), {
  'DESCRIPTOR' : _GIFTMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.GiftMessage)
  })
_sym_db.RegisterMessage(GiftMessage)

WelcomeVIPMessage = _reflection.GeneratedProtocolMessageType('WelcomeVIPMessage', (_message.Message,), {
  'DESCRIPTOR' : _WELCOMEVIPMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.WelcomeVIPMessage)
  })
_sym_db.RegisterMessage(WelcomeVIPMessage)

WelcomeGuardMessage = _reflection.GeneratedProtocolMessageType('WelcomeGuardMessage', (_message.Message,), {
  'DESCRIPTOR' : _WELCOMEGUARDMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.WelcomeGuardMessage)
  })
_sym_db.RegisterMessage(WelcomeGuardMessage)

NewGuardMessage = _reflection.GeneratedProtocolMessageType('NewGuardMessage', (_message.Message,), {
  'DESCRIPTOR' : _NEWGUARDMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.NewGuardMessage)
  })
_sym_db.RegisterMessage(NewGuardMessage)

UserBlockedMessage = _reflection.GeneratedProtocolMessageType('UserBlockedMessage', (_message.Message,), {
  'DESCRIPTOR' : _USERBLOCKEDMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.UserBlockedMessage)
  })
_sym_db.RegisterMessage(UserBlockedMessage)

UserKickedOutMessage = _reflection.GeneratedProtocolMessageType('UserKickedOutMessage', (_message.Message,), {
  'DESCRIPTOR' : _USERKICKEDOUTMESSAGE,
  '__module__' : 'vNerve.bilibili.live.user_message_pb2'
  # @@protoc_insertion_point(class_scope:vNerve.bilibili.live.UserKickedOutMessage)
  })
_sym_db.RegisterMessage(UserKickedOutMessage)


# @@protoc_insertion_point(module_scope)
