# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Invoice
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Invoice(domainresource.DomainResource):
    """ Invoice containing ChargeItems from an Account.

    Invoice containing collected ChargeItems from an Account with calculated
    individual and total price for Billing purpose.
    """

    resource_type = "Invoice"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.account = None
        """ Account that is being balanced.
        Type `FHIRReference` referencing `['Account']` (represented as `dict` in JSON). """

        self.cancelledReason = None
        """ Reason for cancellation of this Invoice.
        Type `str`. """

        self.date = None
        """ Invoice date / posting date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.identifier = None
        """ Business Identifier for item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.issuer = None
        """ Issuing Organization of Invoice.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.lineItem = None
        """ Line items of this Invoice.
        List of `InvoiceLineItem` items (represented as `dict` in JSON). """

        self.note = None
        """ Comments made about the invoice.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.participant = None
        """ Participant in creation of this Invoice.
        List of `InvoiceParticipant` items (represented as `dict` in JSON). """

        self.paymentTerms = None
        """ Payment details.
        Type `str`. """

        self.recipient = None
        """ Recipient of this invoice.
        Type `FHIRReference` referencing `['Organization', 'Patient', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | issued | balanced | cancelled | entered-in-error.
        Type `str`. """

        self.subject = None
        """ Recipient(s) of goods and services.
        Type `FHIRReference` referencing `['Patient', 'Group']` (represented as `dict` in JSON). """

        self.totalGross = None
        """ Gross total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """

        self.totalNet = None
        """ Net total of this Invoice.
        Type `Money` (represented as `dict` in JSON). """

        self.totalPriceComponent = None
        """ Components of Invoice total.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Invoice, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Invoice, self).elementProperties()
        js.extend(
            [
                (
                    "account",
                    "account",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "cancelledReason",
                    "cancelledReason",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                (
                    "issuer",
                    "issuer",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "lineItem",
                    "lineItem",
                    InvoiceLineItem,
                    "InvoiceLineItem",
                    True,
                    None,
                    False,
                ),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                (
                    "participant",
                    "participant",
                    InvoiceParticipant,
                    "InvoiceParticipant",
                    True,
                    None,
                    False,
                ),
                ("paymentTerms", "paymentTerms", str, "markdown", False, None, False),
                (
                    "recipient",
                    "recipient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("totalGross", "totalGross", money.Money, "Money", False, None, False),
                ("totalNet", "totalNet", money.Money, "Money", False, None, False),
                (
                    "totalPriceComponent",
                    "totalPriceComponent",
                    InvoiceLineItemPriceComponent,
                    "InvoiceLineItemPriceComponent",
                    True,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class InvoiceLineItem(backboneelement.BackboneElement):
    """ Line items of this Invoice.

    Each line item represents one charge for goods and services rendered.
    Details such as date, code and amount are found in the referenced
    ChargeItem resource.
    """

    resource_type = "InvoiceLineItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.chargeItemCodeableConcept = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.chargeItemReference = None
        """ Reference to ChargeItem containing details of this line item or an
        inline billing code.
        Type `FHIRReference` referencing `['ChargeItem']` (represented as `dict` in JSON). """

        self.priceComponent = None
        """ Components of total line item price.
        List of `InvoiceLineItemPriceComponent` items (represented as `dict` in JSON). """

        self.sequence = None
        """ Sequence number of line item.
        Type `int`. """

        super(InvoiceLineItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(InvoiceLineItem, self).elementProperties()
        js.extend(
            [
                (
                    "chargeItemCodeableConcept",
                    "chargeItemCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "chargeItem",
                    True,
                ),
                (
                    "chargeItemReference",
                    "chargeItemReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "chargeItem",
                    True,
                ),
                (
                    "priceComponent",
                    "priceComponent",
                    InvoiceLineItemPriceComponent,
                    "InvoiceLineItemPriceComponent",
                    True,
                    None,
                    False,
                ),
                ("sequence", "sequence", int, "positiveInt", False, None, False),
            ]
        )
        return js


class InvoiceLineItemPriceComponent(backboneelement.BackboneElement):
    """ Components of total line item price.

    The price for a ChargeItem may be calculated as a base price with
    surcharges/deductions that apply in certain conditions. A
    ChargeItemDefinition resource that defines the prices, factors and
    conditions that apply to a billing code is currently under development. The
    priceComponent element can be used to offer transparency to the recipient
    of the Invoice as to how the prices have been calculated.
    """

    resource_type = "InvoiceLineItemPriceComponent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amount = None
        """ Monetary amount associated with this component.
        Type `Money` (represented as `dict` in JSON). """

        self.code = None
        """ Code identifying the specific component.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.factor = None
        """ Factor used for calculating this component.
        Type `float`. """

        self.type = None
        """ base | surcharge | deduction | discount | tax | informational.
        Type `str`. """

        super(InvoiceLineItemPriceComponent, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(InvoiceLineItemPriceComponent, self).elementProperties()
        js.extend(
            [
                ("amount", "amount", money.Money, "Money", False, None, False),
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("factor", "factor", float, "decimal", False, None, False),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


class InvoiceParticipant(backboneelement.BackboneElement):
    """ Participant in creation of this Invoice.

    Indicates who or what performed or participated in the charged service.
    """

    resource_type = "InvoiceParticipant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ Individual who was involved.
        Type `FHIRReference` referencing `['Practitioner', 'Organization', 'Patient', 'PractitionerRole', 'Device', 'RelatedPerson']` (represented as `dict` in JSON). """

        self.role = None
        """ Type of involvement in creation of this Invoice.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(InvoiceParticipant, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(InvoiceParticipant, self).elementProperties()
        js.extend(
            [
                (
                    "actor",
                    "actor",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + ".annotation"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
try:
    from . import money
except ImportError:
    money = sys.modules[__package__ + ".money"]
