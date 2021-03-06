# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ratchromadata.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='ratchromadata.proto',
  package='ratchroma',
  syntax='proto3',
  serialized_pb=_b('\n\x13ratchromadata.proto\x12\tratchroma\"\x99\x01\n\x0f\x43herenkovPhoton\x12\t\n\x01x\x18\x02 \x01(\x02\x12\t\n\x01y\x18\x03 \x01(\x02\x12\t\n\x01z\x18\x04 \x01(\x02\x12\t\n\x01t\x18\x05 \x01(\x02\x12\n\n\x02\x64x\x18\x06 \x01(\x02\x12\n\n\x02\x64y\x18\x07 \x01(\x02\x12\n\n\x02\x64z\x18\x08 \x01(\x02\x12\x12\n\nwavelength\x18\t \x01(\x02\x12\n\n\x02px\x18\n \x01(\x02\x12\n\n\x02py\x18\x0b \x01(\x02\x12\n\n\x02pz\x18\x0c \x01(\x02\"\xd7\x01\n\tScintStep\x12\x10\n\x08nphotons\x18\x01 \x01(\x05\x12\x14\n\x0cstep_start_x\x18\x02 \x01(\x02\x12\x14\n\x0cstep_start_y\x18\x03 \x01(\x02\x12\x14\n\x0cstep_start_z\x18\x04 \x01(\x02\x12\x14\n\x0cstep_start_t\x18\x05 \x01(\x02\x12\x12\n\nstep_end_x\x18\x06 \x01(\x02\x12\x12\n\nstep_end_y\x18\x07 \x01(\x02\x12\x12\n\nstep_end_z\x18\x08 \x01(\x02\x12\x12\n\nstep_end_t\x18\t \x01(\x02\x12\x10\n\x08material\x18\n \x01(\t\"x\n\nChromaData\x12\x0f\n\x07\x65ventid\x18\x01 \x01(\x05\x12\x31\n\rcherenkovdata\x18\x02 \x03(\x0b\x32\x1a.ratchroma.CherenkovPhoton\x12&\n\x08stepdata\x18\x03 \x03(\x0b\x32\x14.ratchroma.ScintStepB\x02H\x01\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CHERENKOVPHOTON = _descriptor.Descriptor(
  name='CherenkovPhoton',
  full_name='ratchroma.CherenkovPhoton',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='ratchroma.CherenkovPhoton.x', index=0,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='ratchroma.CherenkovPhoton.y', index=1,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='ratchroma.CherenkovPhoton.z', index=2,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='t', full_name='ratchroma.CherenkovPhoton.t', index=3,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dx', full_name='ratchroma.CherenkovPhoton.dx', index=4,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dy', full_name='ratchroma.CherenkovPhoton.dy', index=5,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dz', full_name='ratchroma.CherenkovPhoton.dz', index=6,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wavelength', full_name='ratchroma.CherenkovPhoton.wavelength', index=7,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='px', full_name='ratchroma.CherenkovPhoton.px', index=8,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='py', full_name='ratchroma.CherenkovPhoton.py', index=9,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pz', full_name='ratchroma.CherenkovPhoton.pz', index=10,
      number=12, type=2, cpp_type=6, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=188,
)


_SCINTSTEP = _descriptor.Descriptor(
  name='ScintStep',
  full_name='ratchroma.ScintStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nphotons', full_name='ratchroma.ScintStep.nphotons', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_start_x', full_name='ratchroma.ScintStep.step_start_x', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_start_y', full_name='ratchroma.ScintStep.step_start_y', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_start_z', full_name='ratchroma.ScintStep.step_start_z', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_start_t', full_name='ratchroma.ScintStep.step_start_t', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_end_x', full_name='ratchroma.ScintStep.step_end_x', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_end_y', full_name='ratchroma.ScintStep.step_end_y', index=6,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_end_z', full_name='ratchroma.ScintStep.step_end_z', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='step_end_t', full_name='ratchroma.ScintStep.step_end_t', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='material', full_name='ratchroma.ScintStep.material', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=406,
)


_CHROMADATA = _descriptor.Descriptor(
  name='ChromaData',
  full_name='ratchroma.ChromaData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='eventid', full_name='ratchroma.ChromaData.eventid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cherenkovdata', full_name='ratchroma.ChromaData.cherenkovdata', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stepdata', full_name='ratchroma.ChromaData.stepdata', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=408,
  serialized_end=528,
)

_CHROMADATA.fields_by_name['cherenkovdata'].message_type = _CHERENKOVPHOTON
_CHROMADATA.fields_by_name['stepdata'].message_type = _SCINTSTEP
DESCRIPTOR.message_types_by_name['CherenkovPhoton'] = _CHERENKOVPHOTON
DESCRIPTOR.message_types_by_name['ScintStep'] = _SCINTSTEP
DESCRIPTOR.message_types_by_name['ChromaData'] = _CHROMADATA

CherenkovPhoton = _reflection.GeneratedProtocolMessageType('CherenkovPhoton', (_message.Message,), dict(
  DESCRIPTOR = _CHERENKOVPHOTON,
  __module__ = 'ratchromadata_pb2'
  # @@protoc_insertion_point(class_scope:ratchroma.CherenkovPhoton)
  ))
_sym_db.RegisterMessage(CherenkovPhoton)

ScintStep = _reflection.GeneratedProtocolMessageType('ScintStep', (_message.Message,), dict(
  DESCRIPTOR = _SCINTSTEP,
  __module__ = 'ratchromadata_pb2'
  # @@protoc_insertion_point(class_scope:ratchroma.ScintStep)
  ))
_sym_db.RegisterMessage(ScintStep)

ChromaData = _reflection.GeneratedProtocolMessageType('ChromaData', (_message.Message,), dict(
  DESCRIPTOR = _CHROMADATA,
  __module__ = 'ratchromadata_pb2'
  # @@protoc_insertion_point(class_scope:ratchroma.ChromaData)
  ))
_sym_db.RegisterMessage(ChromaData)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('H\001'))
# @@protoc_insertion_point(module_scope)
