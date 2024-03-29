# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: historical_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='historical_data.proto',
  package='historical_data',
  syntax='proto3',
  serialized_options=_b('\242\002\002HD'),
  serialized_pb=_b('\n\x15historical_data.proto\x12\x0fhistorical_data\"\x82\x01\n\x07\x42\x61rData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0c\n\x04open\x18\x02 \x01(\x01\x12\x0c\n\x04high\x18\x03 \x01(\x01\x12\x0b\n\x03low\x18\x04 \x01(\x01\x12\r\n\x05\x63lose\x18\x05 \x01(\x01\x12\x0e\n\x06volume\x18\x06 \x01(\x05\x12\x10\n\x08\x62\x61rCount\x18\x07 \x01(\x05\x12\x0f\n\x07\x61verage\x18\x08 \x01(\x01\"c\n\x07Request\x12\r\n\x05stock\x18\x01 \x01(\t\x12\x11\n\tstartDate\x18\x02 \x01(\t\x12\x0f\n\x07\x65ndDate\x18\x03 \x01(\t\x12\x11\n\tpriceType\x18\x04 \x01(\t\x12\x12\n\ndateFormat\x18\x05 \x01(\t\"\x15\n\x13HistoricalDataToAdd\"\x07\n\x05\x45mpty\"\x19\n\tTimestamp\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"\x16\n\x06Result\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t2\x9c\x03\n\x0eHistoricalData\x12N\n\x14GetOneHistoricalData\x12\x18.historical_data.Request\x1a\x18.historical_data.BarData\"\x00\x30\x01\x12Q\n\x15GetManyHistoricalData\x12\x18.historical_data.Request\x1a\x18.historical_data.BarData\"\x00(\x01\x30\x01\x12S\n\x11\x41\x64\x64HistoricalData\x12$.historical_data.HistoricalDataToAdd\x1a\x16.historical_data.Empty\"\x00\x12G\n\x10GetHeadTimeStamp\x12\x18.historical_data.Request\x1a\x17.historical_data.Result\"\x00\x12I\n\x12GetLatestTimeStamp\x12\x18.historical_data.Request\x1a\x17.historical_data.Result\"\x00\x42\x05\xa2\x02\x02HDb\x06proto3')
)




_BARDATA = _descriptor.Descriptor(
  name='BarData',
  full_name='historical_data.BarData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='historical_data.BarData.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='open', full_name='historical_data.BarData.open', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high', full_name='historical_data.BarData.high', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='low', full_name='historical_data.BarData.low', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close', full_name='historical_data.BarData.close', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volume', full_name='historical_data.BarData.volume', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='barCount', full_name='historical_data.BarData.barCount', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='average', full_name='historical_data.BarData.average', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=43,
  serialized_end=173,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='historical_data.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stock', full_name='historical_data.Request.stock', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startDate', full_name='historical_data.Request.startDate', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endDate', full_name='historical_data.Request.endDate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priceType', full_name='historical_data.Request.priceType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dateFormat', full_name='historical_data.Request.dateFormat', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=175,
  serialized_end=274,
)


_HISTORICALDATATOADD = _descriptor.Descriptor(
  name='HistoricalDataToAdd',
  full_name='historical_data.HistoricalDataToAdd',
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
  serialized_start=276,
  serialized_end=297,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='historical_data.Empty',
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
  serialized_start=299,
  serialized_end=306,
)


_TIMESTAMP = _descriptor.Descriptor(
  name='Timestamp',
  full_name='historical_data.Timestamp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='historical_data.Timestamp.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=308,
  serialized_end=333,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='historical_data.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='historical_data.Result.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=335,
  serialized_end=357,
)

DESCRIPTOR.message_types_by_name['BarData'] = _BARDATA
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['HistoricalDataToAdd'] = _HISTORICALDATATOADD
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Timestamp'] = _TIMESTAMP
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BarData = _reflection.GeneratedProtocolMessageType('BarData', (_message.Message,), {
  'DESCRIPTOR' : _BARDATA,
  '__module__' : 'historical_data_pb2'
  # @@protoc_insertion_point(class_scope:historical_data.BarData)
  })
_sym_db.RegisterMessage(BarData)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'historical_data_pb2'
  # @@protoc_insertion_point(class_scope:historical_data.Request)
  })
_sym_db.RegisterMessage(Request)

HistoricalDataToAdd = _reflection.GeneratedProtocolMessageType('HistoricalDataToAdd', (_message.Message,), {
  'DESCRIPTOR' : _HISTORICALDATATOADD,
  '__module__' : 'historical_data_pb2'
  # @@protoc_insertion_point(class_scope:historical_data.HistoricalDataToAdd)
  })
_sym_db.RegisterMessage(HistoricalDataToAdd)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'historical_data_pb2'
  # @@protoc_insertion_point(class_scope:historical_data.Empty)
  })
_sym_db.RegisterMessage(Empty)

Timestamp = _reflection.GeneratedProtocolMessageType('Timestamp', (_message.Message,), {
  'DESCRIPTOR' : _TIMESTAMP,
  '__module__' : 'historical_data_pb2'
  # @@protoc_insertion_point(class_scope:historical_data.Timestamp)
  })
_sym_db.RegisterMessage(Timestamp)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), {
  'DESCRIPTOR' : _RESULT,
  '__module__' : 'historical_data_pb2'
  # @@protoc_insertion_point(class_scope:historical_data.Result)
  })
_sym_db.RegisterMessage(Result)


DESCRIPTOR._options = None

_HISTORICALDATA = _descriptor.ServiceDescriptor(
  name='HistoricalData',
  full_name='historical_data.HistoricalData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=360,
  serialized_end=772,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOneHistoricalData',
    full_name='historical_data.HistoricalData.GetOneHistoricalData',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_BARDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetManyHistoricalData',
    full_name='historical_data.HistoricalData.GetManyHistoricalData',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_BARDATA,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddHistoricalData',
    full_name='historical_data.HistoricalData.AddHistoricalData',
    index=2,
    containing_service=None,
    input_type=_HISTORICALDATATOADD,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetHeadTimeStamp',
    full_name='historical_data.HistoricalData.GetHeadTimeStamp',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetLatestTimeStamp',
    full_name='historical_data.HistoricalData.GetLatestTimeStamp',
    index=4,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_HISTORICALDATA)

DESCRIPTOR.services_by_name['HistoricalData'] = _HISTORICALDATA

# @@protoc_insertion_point(module_scope)
