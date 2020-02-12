# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: response_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='response_data.proto',
  package='sendrequest',
  syntax='proto3',
  serialized_options=_b('\242\002\004ResD'),
  serialized_pb=_b('\n\x13response_data.proto\x12\x0bsendrequest\"\xcf\x02\n\x08\x43ontract\x12\r\n\x05\x63onId\x18\x01 \x01(\x05\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0f\n\x07secType\x18\x03 \x01(\t\x12\x10\n\x08\x65xchange\x18\x04 \x01(\t\x12\x17\n\x0fprimaryExchange\x18\x05 \x01(\t\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12$\n\x1clastTradeDateOrContractMonth\x18\x07 \x01(\t\x12\x0e\n\x06strike\x18\x08 \x01(\x02\x12\r\n\x05right\x18\t \x01(\t\x12\x12\n\nmultiplier\x18\n \x01(\t\x12\x13\n\x0blocalSymbol\x18\x0b \x01(\t\x12\x14\n\x0ctradingClass\x18\x0c \x01(\t\x12\x16\n\x0eincludeExpired\x18\r \x01(\x08\x12\x11\n\tsecIdType\x18\x0e \x01(\t\x12\r\n\x05secId\x18\x0f \x01(\t\x12\x18\n\x10\x63omboLegsDescrip\x18\x10 \x01(\t\"c\n\x17\x43ontractDetailsResponse\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\x35\n\x0f\x63ontractDetails\x18\x02 \x01(\x0b\x32\x1c.sendrequest.ContractDetails\"T\n\x16HistoricalDataResponse\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\'\n\x08\x63ontract\x18\x02 \x01(\x0b\x32\x15.sendrequest.Contract\"b\n\x17\x46undamentalDataResponse\x12\x11\n\trequestId\x18\x01 \x01(\x05\x12\'\n\x08\x63ontract\x18\x02 \x01(\x0b\x32\x15.sendrequest.Contract\x12\x0b\n\x03xml\x18\x03 \x01(\t\"\x19\n\x06Status\x12\x0f\n\x07message\x18\x01 \x01(\x08\"\xc0\x06\n\x0f\x43ontractDetails\x12\'\n\x08\x63ontract\x18\x01 \x01(\x0b\x32\x15.sendrequest.Contract\x12\x12\n\nmarketName\x18\x02 \x01(\t\x12\x0f\n\x07minTick\x18\x03 \x01(\x02\x12\x12\n\norderTypes\x18\x04 \x01(\t\x12\x16\n\x0evalidExchanges\x18\x05 \x01(\t\x12\x16\n\x0epriceMagnifier\x18\x06 \x01(\x05\x12\x12\n\nunderConId\x18\x07 \x01(\x05\x12\x10\n\x08longName\x18\x08 \x01(\t\x12\x15\n\rcontractMonth\x18\t \x01(\t\x12\x10\n\x08industry\x18\n \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\r \x01(\t\x12\x13\n\x0bsubcategory\x18\x0e \x01(\t\x12\x12\n\ntimeZoneId\x18\x0f \x01(\t\x12\x14\n\x0ctradingHours\x18\x10 \x01(\t\x12\x13\n\x0bliquidHours\x18\x11 \x01(\t\x12\x0e\n\x06\x65vRule\x18\x12 \x01(\t\x12\x14\n\x0c\x65vMultiplier\x18\x13 \x01(\x05\x12\x18\n\x10mdSizeMultiplier\x18\x14 \x01(\x05\x12\x10\n\x08\x61ggGroup\x18\x15 \x01(\x05\x12\x13\n\x0bunderSymbol\x18\x16 \x01(\t\x12\x14\n\x0cunderSecType\x18\x17 \x01(\t\x12\x15\n\rmarketRuleIds\x18\x18 \x01(\t\x12\x1a\n\x12realExpirationDate\x18\x19 \x01(\t\x12\x15\n\rlastTradeTime\x18\x1a \x01(\t\x12\r\n\x05\x63usip\x18\x1b \x01(\t\x12\x0f\n\x07ratings\x18\x1c \x01(\t\x12\x12\n\ndescAppend\x18\x1d \x01(\t\x12\x10\n\x08\x62ondType\x18\x1e \x01(\t\x12\x12\n\ncouponType\x18\x1f \x01(\t\x12\x10\n\x08\x63\x61llable\x18  \x01(\x08\x12\x0f\n\x07putable\x18! \x01(\x08\x12\x0e\n\x06\x63oupon\x18\" \x01(\x05\x12\x13\n\x0b\x63onvertible\x18# \x01(\x08\x12\x10\n\x08maturity\x18$ \x01(\t\x12\x11\n\tissueDate\x18% \x01(\t\x12\x16\n\x0enextOptionDate\x18& \x01(\t\x12\x16\n\x0enextOptionType\x18\' \x01(\t\x12\x19\n\x11nextOptionPartial\x18( \x01(\t\x12\r\n\x05notes\x18) \x01(\t2\x88\x02\n\x0cResponseData\x12R\n\x13SendContractDetails\x12$.sendrequest.ContractDetailsResponse\x1a\x13.sendrequest.Status\"\x00\x12P\n\x12SendHistoricalData\x12#.sendrequest.HistoricalDataResponse\x1a\x13.sendrequest.Status\"\x00\x12R\n\x13SendFundamentalData\x12$.sendrequest.FundamentalDataResponse\x1a\x13.sendrequest.Status\"\x00\x42\x07\xa2\x02\x04ResDb\x06proto3')
)




_CONTRACT = _descriptor.Descriptor(
  name='Contract',
  full_name='sendrequest.Contract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conId', full_name='sendrequest.Contract.conId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='sendrequest.Contract.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secType', full_name='sendrequest.Contract.secType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='sendrequest.Contract.exchange', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primaryExchange', full_name='sendrequest.Contract.primaryExchange', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='sendrequest.Contract.currency', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastTradeDateOrContractMonth', full_name='sendrequest.Contract.lastTradeDateOrContractMonth', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strike', full_name='sendrequest.Contract.strike', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='sendrequest.Contract.right', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='sendrequest.Contract.multiplier', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localSymbol', full_name='sendrequest.Contract.localSymbol', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradingClass', full_name='sendrequest.Contract.tradingClass', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='includeExpired', full_name='sendrequest.Contract.includeExpired', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secIdType', full_name='sendrequest.Contract.secIdType', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secId', full_name='sendrequest.Contract.secId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comboLegsDescrip', full_name='sendrequest.Contract.comboLegsDescrip', index=15,
      number=16, type=9, cpp_type=9, label=1,
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
  serialized_start=37,
  serialized_end=372,
)


_CONTRACTDETAILSRESPONSE = _descriptor.Descriptor(
  name='ContractDetailsResponse',
  full_name='sendrequest.ContractDetailsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='sendrequest.ContractDetailsResponse.requestId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contractDetails', full_name='sendrequest.ContractDetailsResponse.contractDetails', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=374,
  serialized_end=473,
)


_HISTORICALDATARESPONSE = _descriptor.Descriptor(
  name='HistoricalDataResponse',
  full_name='sendrequest.HistoricalDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='sendrequest.HistoricalDataResponse.requestId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract', full_name='sendrequest.HistoricalDataResponse.contract', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  ],
  serialized_start=475,
  serialized_end=559,
)


_FUNDAMENTALDATARESPONSE = _descriptor.Descriptor(
  name='FundamentalDataResponse',
  full_name='sendrequest.FundamentalDataResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='requestId', full_name='sendrequest.FundamentalDataResponse.requestId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contract', full_name='sendrequest.FundamentalDataResponse.contract', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='xml', full_name='sendrequest.FundamentalDataResponse.xml', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=561,
  serialized_end=659,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='sendrequest.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='sendrequest.Status.message', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=661,
  serialized_end=686,
)


_CONTRACTDETAILS = _descriptor.Descriptor(
  name='ContractDetails',
  full_name='sendrequest.ContractDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contract', full_name='sendrequest.ContractDetails.contract', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketName', full_name='sendrequest.ContractDetails.marketName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minTick', full_name='sendrequest.ContractDetails.minTick', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderTypes', full_name='sendrequest.ContractDetails.orderTypes', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validExchanges', full_name='sendrequest.ContractDetails.validExchanges', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priceMagnifier', full_name='sendrequest.ContractDetails.priceMagnifier', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underConId', full_name='sendrequest.ContractDetails.underConId', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longName', full_name='sendrequest.ContractDetails.longName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contractMonth', full_name='sendrequest.ContractDetails.contractMonth', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='industry', full_name='sendrequest.ContractDetails.industry', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='sendrequest.ContractDetails.category', index=10,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subcategory', full_name='sendrequest.ContractDetails.subcategory', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeZoneId', full_name='sendrequest.ContractDetails.timeZoneId', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradingHours', full_name='sendrequest.ContractDetails.tradingHours', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liquidHours', full_name='sendrequest.ContractDetails.liquidHours', index=14,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evRule', full_name='sendrequest.ContractDetails.evRule', index=15,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evMultiplier', full_name='sendrequest.ContractDetails.evMultiplier', index=16,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mdSizeMultiplier', full_name='sendrequest.ContractDetails.mdSizeMultiplier', index=17,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggGroup', full_name='sendrequest.ContractDetails.aggGroup', index=18,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underSymbol', full_name='sendrequest.ContractDetails.underSymbol', index=19,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underSecType', full_name='sendrequest.ContractDetails.underSecType', index=20,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketRuleIds', full_name='sendrequest.ContractDetails.marketRuleIds', index=21,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='realExpirationDate', full_name='sendrequest.ContractDetails.realExpirationDate', index=22,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastTradeTime', full_name='sendrequest.ContractDetails.lastTradeTime', index=23,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cusip', full_name='sendrequest.ContractDetails.cusip', index=24,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratings', full_name='sendrequest.ContractDetails.ratings', index=25,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descAppend', full_name='sendrequest.ContractDetails.descAppend', index=26,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bondType', full_name='sendrequest.ContractDetails.bondType', index=27,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='couponType', full_name='sendrequest.ContractDetails.couponType', index=28,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callable', full_name='sendrequest.ContractDetails.callable', index=29,
      number=32, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='putable', full_name='sendrequest.ContractDetails.putable', index=30,
      number=33, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coupon', full_name='sendrequest.ContractDetails.coupon', index=31,
      number=34, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convertible', full_name='sendrequest.ContractDetails.convertible', index=32,
      number=35, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maturity', full_name='sendrequest.ContractDetails.maturity', index=33,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issueDate', full_name='sendrequest.ContractDetails.issueDate', index=34,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextOptionDate', full_name='sendrequest.ContractDetails.nextOptionDate', index=35,
      number=38, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextOptionType', full_name='sendrequest.ContractDetails.nextOptionType', index=36,
      number=39, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextOptionPartial', full_name='sendrequest.ContractDetails.nextOptionPartial', index=37,
      number=40, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='sendrequest.ContractDetails.notes', index=38,
      number=41, type=9, cpp_type=9, label=1,
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
  serialized_start=689,
  serialized_end=1521,
)

_CONTRACTDETAILSRESPONSE.fields_by_name['contractDetails'].message_type = _CONTRACTDETAILS
_HISTORICALDATARESPONSE.fields_by_name['contract'].message_type = _CONTRACT
_FUNDAMENTALDATARESPONSE.fields_by_name['contract'].message_type = _CONTRACT
_CONTRACTDETAILS.fields_by_name['contract'].message_type = _CONTRACT
DESCRIPTOR.message_types_by_name['Contract'] = _CONTRACT
DESCRIPTOR.message_types_by_name['ContractDetailsResponse'] = _CONTRACTDETAILSRESPONSE
DESCRIPTOR.message_types_by_name['HistoricalDataResponse'] = _HISTORICALDATARESPONSE
DESCRIPTOR.message_types_by_name['FundamentalDataResponse'] = _FUNDAMENTALDATARESPONSE
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['ContractDetails'] = _CONTRACTDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Contract = _reflection.GeneratedProtocolMessageType('Contract', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACT,
  __module__ = 'response_data_pb2'
  # @@protoc_insertion_point(class_scope:sendrequest.Contract)
  ))
_sym_db.RegisterMessage(Contract)

ContractDetailsResponse = _reflection.GeneratedProtocolMessageType('ContractDetailsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACTDETAILSRESPONSE,
  __module__ = 'response_data_pb2'
  # @@protoc_insertion_point(class_scope:sendrequest.ContractDetailsResponse)
  ))
_sym_db.RegisterMessage(ContractDetailsResponse)

HistoricalDataResponse = _reflection.GeneratedProtocolMessageType('HistoricalDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _HISTORICALDATARESPONSE,
  __module__ = 'response_data_pb2'
  # @@protoc_insertion_point(class_scope:sendrequest.HistoricalDataResponse)
  ))
_sym_db.RegisterMessage(HistoricalDataResponse)

FundamentalDataResponse = _reflection.GeneratedProtocolMessageType('FundamentalDataResponse', (_message.Message,), dict(
  DESCRIPTOR = _FUNDAMENTALDATARESPONSE,
  __module__ = 'response_data_pb2'
  # @@protoc_insertion_point(class_scope:sendrequest.FundamentalDataResponse)
  ))
_sym_db.RegisterMessage(FundamentalDataResponse)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), dict(
  DESCRIPTOR = _STATUS,
  __module__ = 'response_data_pb2'
  # @@protoc_insertion_point(class_scope:sendrequest.Status)
  ))
_sym_db.RegisterMessage(Status)

ContractDetails = _reflection.GeneratedProtocolMessageType('ContractDetails', (_message.Message,), dict(
  DESCRIPTOR = _CONTRACTDETAILS,
  __module__ = 'response_data_pb2'
  # @@protoc_insertion_point(class_scope:sendrequest.ContractDetails)
  ))
_sym_db.RegisterMessage(ContractDetails)


DESCRIPTOR._options = None

_RESPONSEDATA = _descriptor.ServiceDescriptor(
  name='ResponseData',
  full_name='sendrequest.ResponseData',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1524,
  serialized_end=1788,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendContractDetails',
    full_name='sendrequest.ResponseData.SendContractDetails',
    index=0,
    containing_service=None,
    input_type=_CONTRACTDETAILSRESPONSE,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendHistoricalData',
    full_name='sendrequest.ResponseData.SendHistoricalData',
    index=1,
    containing_service=None,
    input_type=_HISTORICALDATARESPONSE,
    output_type=_STATUS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendFundamentalData',
    full_name='sendrequest.ResponseData.SendFundamentalData',
    index=2,
    containing_service=None,
    input_type=_FUNDAMENTALDATARESPONSE,
    output_type=_STATUS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESPONSEDATA)

DESCRIPTOR.services_by_name['ResponseData'] = _RESPONSEDATA

# @@protoc_insertion_point(module_scope)