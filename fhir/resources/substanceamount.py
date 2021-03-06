# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SubstanceAmount
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, element


class SubstanceAmount(backboneelement.BackboneElement):
    """ Chemical substances are a single substance type whose primary defining
    element is the molecular structure. Chemical substances shall be defined on
    the basis of their complete covalent molecular structure; the presence of a
    salt (counter-ion) and/or solvates (water, alcohols) is also captured.
    Purity, grade, physical form or particle size are not taken into account in
    the definition of a chemical substance or in the assignment of a Substance
    ID.
    """

    resource_type = "SubstanceAmount"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amountQuantity = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `Quantity` (represented as `dict` in JSON). """

        self.amountRange = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `Range` (represented as `dict` in JSON). """

        self.amountString = None
        """ Used to capture quantitative values for a variety of elements. If
        only limits are given, the arithmetic mean would be the average. If
        only a single definite value for a given element is given, it would
        be captured in this field.
        Type `str`. """

        self.amountText = None
        """ A textual comment on a numeric value.
        Type `str`. """

        self.amountType = None
        """ Most elements that require a quantitative value will also have a
        field called amount type. Amount type should always be specified
        because the actual value of the amount is often dependent on it.
        EXAMPLE: In capturing the actual relative amounts of substances or
        molecular fragments it is essential to indicate whether the amount
        refers to a mole ratio or weight ratio. For any given element an
        effort should be made to use same the amount type for all related
        definitional elements.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.referenceRange = None
        """ Reference range of possible or expected values.
        Type `SubstanceAmountReferenceRange` (represented as `dict` in JSON). """

        super(SubstanceAmount, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SubstanceAmount, self).elementProperties()
        js.extend(
            [
                (
                    "amountQuantity",
                    "amountQuantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    "amount",
                    False,
                ),
                (
                    "amountRange",
                    "amountRange",
                    range.Range,
                    "Range",
                    False,
                    "amount",
                    False,
                ),
                ("amountString", "amountString", str, "string", False, "amount", False),
                ("amountText", "amountText", str, "string", False, None, False),
                (
                    "amountType",
                    "amountType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "referenceRange",
                    "referenceRange",
                    SubstanceAmountReferenceRange,
                    "SubstanceAmountReferenceRange",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class SubstanceAmountReferenceRange(element.Element):
    """ Reference range of possible or expected values.
    """

    resource_type = "SubstanceAmountReferenceRange"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.highLimit = None
        """ Upper limit possible or expected.
        Type `Quantity` (represented as `dict` in JSON). """

        self.lowLimit = None
        """ Lower limit possible or expected.
        Type `Quantity` (represented as `dict` in JSON). """

        super(SubstanceAmountReferenceRange, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(SubstanceAmountReferenceRange, self).elementProperties()
        js.extend(
            [
                (
                    "highLimit",
                    "highLimit",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "lowLimit",
                    "lowLimit",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
