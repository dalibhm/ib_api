# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contract.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contract.proto',
  package='contracts',
  syntax='proto3',
  serialized_options=_b('\242\002\002CD'),
  serialized_pb=_b('\n\x0e\x63ontract.proto\x12\tcontracts\"\x18\n\x07Request\x12\r\n\x05\x63onId\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\"\x9c\x03\n\x08\x43ontract\x12\r\n\x05\x63onId\x18\x01 \x01(\x05\x12\x0e\n\x06symbol\x18\x02 \x01(\t\x12\x0f\n\x07secType\x18\x03 \x01(\t\x12\x10\n\x08\x65xchange\x18\x04 \x01(\t\x12\x17\n\x0fprimaryExchange\x18\x05 \x01(\t\x12\x10\n\x08\x63urrency\x18\x06 \x01(\t\x12$\n\x1clastTradeDateOrContractMonth\x18\x07 \x01(\t\x12\x0e\n\x06strike\x18\x08 \x01(\x02\x12\r\n\x05right\x18\t \x01(\t\x12\x12\n\nmultiplier\x18\n \x01(\t\x12\x13\n\x0blocalSymbol\x18\x0b \x01(\t\x12\x14\n\x0ctradingClass\x18\x0c \x01(\t\x12\x16\n\x0eincludeExpired\x18\r \x01(\x08\x12\x11\n\tsecIdType\x18\x0e \x01(\t\x12\r\n\x05secId\x18\x0f \x01(\t\x12\x18\n\x10\x63omboLegsDescrip\x18\x10 \x01(\t\x12\x11\n\tcomboLegs\x18\x11 \x01(\t\x12\x1c\n\x14\x64\x65ltaNeutralContract\x18\x12 \x01(\t\x12\x1a\n\x12\x64\x65rivativeSecTypes\x18\x13 \x01(\t\"\xbe\x06\n\x0f\x43ontractDetails\x12\x12\n\ncontractId\x18\x01 \x01(\x05\x12\x12\n\nmarketName\x18\x02 \x01(\t\x12\x0f\n\x07minTick\x18\x03 \x01(\x02\x12\x12\n\norderTypes\x18\x04 \x01(\t\x12\x16\n\x0evalidExchanges\x18\x05 \x01(\t\x12\x16\n\x0epriceMagnifier\x18\x06 \x01(\x05\x12\x12\n\nunderConId\x18\x07 \x01(\x05\x12\x10\n\x08longName\x18\x08 \x01(\t\x12\x15\n\rcontractMonth\x18\t \x01(\t\x12\x10\n\x08industry\x18\n \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\r \x01(\t\x12\x13\n\x0bsubcategory\x18\x0e \x01(\t\x12\x12\n\ntimeZoneId\x18\x0f \x01(\t\x12\x14\n\x0ctradingHours\x18\x10 \x01(\t\x12\x13\n\x0bliquidHours\x18\x11 \x01(\t\x12\x0e\n\x06\x65vRule\x18\x12 \x01(\t\x12\x14\n\x0c\x65vMultiplier\x18\x13 \x01(\x05\x12\x18\n\x10mdSizeMultiplier\x18\x14 \x01(\x05\x12\x10\n\x08\x61ggGroup\x18\x15 \x01(\x05\x12\x13\n\x0bunderSymbol\x18\x16 \x01(\t\x12\x14\n\x0cunderSecType\x18\x17 \x01(\t\x12\x15\n\rmarketRuleIds\x18\x18 \x01(\t\x12\x11\n\tsecIdList\x18\x19 \x01(\t\x12\x1a\n\x12realExpirationDate\x18\x1a \x01(\t\x12\x15\n\rlastTradeTime\x18\x1b \x01(\t\x12\r\n\x05\x63usip\x18\x1c \x01(\t\x12\x0f\n\x07ratings\x18\x1d \x01(\t\x12\x12\n\ndescAppend\x18\x1e \x01(\t\x12\x10\n\x08\x62ondType\x18\x1f \x01(\t\x12\x12\n\ncouponType\x18  \x01(\t\x12\x10\n\x08\x63\x61llable\x18! \x01(\x08\x12\x0f\n\x07putable\x18\" \x01(\x08\x12\x0e\n\x06\x63oupon\x18# \x01(\x05\x12\x13\n\x0b\x63onvertible\x18$ \x01(\x08\x12\x10\n\x08maturity\x18% \x01(\t\x12\x11\n\tissueDate\x18& \x01(\t\x12\x16\n\x0enextOptionDate\x18\' \x01(\t\x12\x16\n\x0enextOptionType\x18( \x01(\t\x12\x19\n\x11nextOptionPartial\x18) \x01(\x08\x12\r\n\x05notes\x18* \x01(\t2\x91\x02\n\x0f\x43ontractService\x12\x38\n\x0bGetContract\x12\x12.contracts.Request\x1a\x13.contracts.Contract\"\x00\x12\x36\n\x0b\x41\x64\x64\x43ontract\x12\x13.contracts.Contract\x1a\x10.contracts.Empty\"\x00\x12\x46\n\x12GetContractDetails\x12\x12.contracts.Request\x1a\x1a.contracts.ContractDetails\"\x00\x12\x44\n\x12\x41\x64\x64\x43ontractDetails\x12\x1a.contracts.ContractDetails\x1a\x10.contracts.Empty\"\x00\x42\x05\xa2\x02\x02\x43\x44\x62\x06proto3')
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='contracts.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conId', full_name='contracts.Request.conId', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=29,
  serialized_end=53,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='contracts.Empty',
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
  serialized_start=55,
  serialized_end=62,
)


_CONTRACT = _descriptor.Descriptor(
  name='Contract',
  full_name='contracts.Contract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='conId', full_name='contracts.Contract.conId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='symbol', full_name='contracts.Contract.symbol', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secType', full_name='contracts.Contract.secType', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='contracts.Contract.exchange', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='primaryExchange', full_name='contracts.Contract.primaryExchange', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='currency', full_name='contracts.Contract.currency', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastTradeDateOrContractMonth', full_name='contracts.Contract.lastTradeDateOrContractMonth', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strike', full_name='contracts.Contract.strike', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='contracts.Contract.right', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='contracts.Contract.multiplier', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='localSymbol', full_name='contracts.Contract.localSymbol', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradingClass', full_name='contracts.Contract.tradingClass', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='includeExpired', full_name='contracts.Contract.includeExpired', index=12,
      number=13, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secIdType', full_name='contracts.Contract.secIdType', index=13,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secId', full_name='contracts.Contract.secId', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comboLegsDescrip', full_name='contracts.Contract.comboLegsDescrip', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='comboLegs', full_name='contracts.Contract.comboLegs', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deltaNeutralContract', full_name='contracts.Contract.deltaNeutralContract', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='derivativeSecTypes', full_name='contracts.Contract.derivativeSecTypes', index=18,
      number=19, type=9, cpp_type=9, label=1,
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
  serialized_start=65,
  serialized_end=477,
)


_CONTRACTDETAILS = _descriptor.Descriptor(
  name='ContractDetails',
  full_name='contracts.ContractDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contractId', full_name='contracts.ContractDetails.contractId', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketName', full_name='contracts.ContractDetails.marketName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minTick', full_name='contracts.ContractDetails.minTick', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='orderTypes', full_name='contracts.ContractDetails.orderTypes', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='validExchanges', full_name='contracts.ContractDetails.validExchanges', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='priceMagnifier', full_name='contracts.ContractDetails.priceMagnifier', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underConId', full_name='contracts.ContractDetails.underConId', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='longName', full_name='contracts.ContractDetails.longName', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='contractMonth', full_name='contracts.ContractDetails.contractMonth', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='industry', full_name='contracts.ContractDetails.industry', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category', full_name='contracts.ContractDetails.category', index=10,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subcategory', full_name='contracts.ContractDetails.subcategory', index=11,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeZoneId', full_name='contracts.ContractDetails.timeZoneId', index=12,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tradingHours', full_name='contracts.ContractDetails.tradingHours', index=13,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='liquidHours', full_name='contracts.ContractDetails.liquidHours', index=14,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evRule', full_name='contracts.ContractDetails.evRule', index=15,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evMultiplier', full_name='contracts.ContractDetails.evMultiplier', index=16,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mdSizeMultiplier', full_name='contracts.ContractDetails.mdSizeMultiplier', index=17,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aggGroup', full_name='contracts.ContractDetails.aggGroup', index=18,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underSymbol', full_name='contracts.ContractDetails.underSymbol', index=19,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='underSecType', full_name='contracts.ContractDetails.underSecType', index=20,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='marketRuleIds', full_name='contracts.ContractDetails.marketRuleIds', index=21,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secIdList', full_name='contracts.ContractDetails.secIdList', index=22,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='realExpirationDate', full_name='contracts.ContractDetails.realExpirationDate', index=23,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastTradeTime', full_name='contracts.ContractDetails.lastTradeTime', index=24,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cusip', full_name='contracts.ContractDetails.cusip', index=25,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ratings', full_name='contracts.ContractDetails.ratings', index=26,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='descAppend', full_name='contracts.ContractDetails.descAppend', index=27,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bondType', full_name='contracts.ContractDetails.bondType', index=28,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='couponType', full_name='contracts.ContractDetails.couponType', index=29,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='callable', full_name='contracts.ContractDetails.callable', index=30,
      number=33, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='putable', full_name='contracts.ContractDetails.putable', index=31,
      number=34, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coupon', full_name='contracts.ContractDetails.coupon', index=32,
      number=35, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='convertible', full_name='contracts.ContractDetails.convertible', index=33,
      number=36, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maturity', full_name='contracts.ContractDetails.maturity', index=34,
      number=37, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issueDate', full_name='contracts.ContractDetails.issueDate', index=35,
      number=38, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextOptionDate', full_name='contracts.ContractDetails.nextOptionDate', index=36,
      number=39, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextOptionType', full_name='contracts.ContractDetails.nextOptionType', index=37,
      number=40, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nextOptionPartial', full_name='contracts.ContractDetails.nextOptionPartial', index=38,
      number=41, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notes', full_name='contracts.ContractDetails.notes', index=39,
      number=42, type=9, cpp_type=9, label=1,
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
  serialized_start=480,
  serialized_end=1310,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Contract'] = _CONTRACT
DESCRIPTOR.message_types_by_name['ContractDetails'] = _CONTRACTDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'contract_pb2'
  # @@protoc_insertion_point(class_scope:contracts.Request)
  })
_sym_db.RegisterMessage(Request)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'contract_pb2'
  # @@protoc_insertion_point(class_scope:contracts.Empty)
  })
_sym_db.RegisterMessage(Empty)

Contract = _reflection.GeneratedProtocolMessageType('Contract', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACT,
  '__module__' : 'contract_pb2'
  # @@protoc_insertion_point(class_scope:contracts.Contract)
  })
_sym_db.RegisterMessage(Contract)

ContractDetails = _reflection.GeneratedProtocolMessageType('ContractDetails', (_message.Message,), {
  'DESCRIPTOR' : _CONTRACTDETAILS,
  '__module__' : 'contract_pb2'
  # @@protoc_insertion_point(class_scope:contracts.ContractDetails)
  })
_sym_db.RegisterMessage(ContractDetails)


DESCRIPTOR._options = None

_CONTRACTSERVICE = _descriptor.ServiceDescriptor(
  name='ContractService',
  full_name='contracts.ContractService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1313,
  serialized_end=1586,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetContract',
    full_name='contracts.ContractService.GetContract',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_CONTRACT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddContract',
    full_name='contracts.ContractService.AddContract',
    index=1,
    containing_service=None,
    input_type=_CONTRACT,
    output_type=_EMPTY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetContractDetails',
    full_name='contracts.ContractService.GetContractDetails',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_CONTRACTDETAILS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='AddContractDetails',
    full_name='contracts.ContractService.AddContractDetails',
    index=3,
    containing_service=None,
    input_type=_CONTRACTDETAILS,
    output_type=_EMPTY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CONTRACTSERVICE)

DESCRIPTOR.services_by_name['ContractService'] = _CONTRACTSERVICE

# @@protoc_insertion_point(module_scope)