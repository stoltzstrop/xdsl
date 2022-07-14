from __future__ import annotations
from dataclasses import dataclass

from xdsl.irdl import *
from xdsl.ir import *
from typing import overload

# How to deal with 32 and 64? -- see cmath??

@dataclass
class Float:
    ctx: MLContext

def __post_init__(self):
    self.ctx.register_attr(FloatAttr)
    self.ctx.register_attr(FloatType)

@irdl_attr_definition
class FloatAttr(Data):
    name = "float"
    data: float
    #data: ParameterDef[Float64Type | Float32Type]

    @staticmethod
    def parse(parser: Parser) -> FloatAttr:
        data = parser.parse_float_literal()
        return FloatAttr(data)

    def print(self, printer: Printer) -> None:
        printer.print_string(f'{self.data}')

    @staticmethod
    @builder
    def from_float(data: float) -> FloatAttr:
        return FloatAttr(data)

@irdl_attr_definition
class FloatType(ParametrizedAttribute):
    name = "float_type"
    width = ParameterDef(FloatAttr)

    @staticmethod
    @builder
    def from_width(width: float) -> Attribute:
        return FloatType([FloatAttr.from_float(width)])

f32 = FloatType.from_width(32)
f64 = FloatType.from_width(64)

#@irdl_attr_definition
#class Float32Attr(ParametrizedAttribute):
#    name = "float32"
#    value = ParameterDef(FloatAttr)
#    typ = ParameterDef([Float32Type])
#
#    @staticmethod
#    @builder
#    def from_float_and_width(value: float, width: float) -> Float32Attr:
#        return Float32Attr(
#            [FloatAttr.from_float(value),
#             Float32Type.from_width(width)])
#
#    @staticmethod
#    @builder
#    def from_params(value: Union[float, FloatAttr],
#                    typ: Union[float, Attribute]) -> Float32Attr:
#        value = FloatAttr.build(value)
#        return Float32Attr([value, typ])

