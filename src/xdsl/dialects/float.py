from __future__ import annotations

from xdsl.dialects.builtin import IntAttr
from xdsl.irdl import *
from xdsl.ir import *


@dataclass
class Float:
    ctx: MLContext

    def __post_init__(self):
        self.ctx.register_attr(FloatAttr)
        self.ctx.register_attr(FloatType)

@irdl_attr_definition
class FloatAttr(Data[float]):
    name = "float"
    data: float

    @staticmethod
    def parse(parser: Parser) -> FloatAttr:
        data = parser.parse_float_literal()
        return data

    def print(self, printer: Printer) -> None:
        printer.print_string(f'{self.data}')

    @staticmethod
    @builder
    def from_float(data: float) -> FloatAttr:
        return FloatAttr(data)

    def verify(self, attr: Attribute) -> None:
        if not isinstance(attr, Float):
            raise Exception(f"expected data Float but got {attr}")
        for e in cast(FloatAttr[Attribute], attr).data:
            self.elem_constr.verify(e)

@irdl_attr_definition
class FloatType(ParametrizedAttribute):
    name = "float_type"
    width: ParameterDef[IntAttr]

    @staticmethod
    @builder
    def from_width(width: int) -> FloatType:
        return FloatType([IntAttr.from_int(width)])

ft32 = FloatType.from_width(32)
ft64 = FloatType.from_width(64)

