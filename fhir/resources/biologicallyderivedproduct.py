# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BiologicallyDerivedProduct
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class BiologicallyDerivedProduct(domainresource.DomainResource):
    """ A material substance originating from a biological entity.

    A material substance originating from a biological entity intended to be
    transplanted or infused
    into another (possibly the same) biological entity.
    """

    resource_type = "BiologicallyDerivedProduct"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.collection = None
        """ How this product was collected.
        Type `BiologicallyDerivedProductCollection` (represented as `dict` in JSON). """

        self.identifier = None
        """ External ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.manipulation = None
        """ Any manipulation of product post-collection.
        Type `BiologicallyDerivedProductManipulation` (represented as `dict` in JSON). """

        self.parent = None
        """ BiologicallyDerivedProduct parent.
        List of `FHIRReference` items referencing `['BiologicallyDerivedProduct']` (represented as `dict` in JSON). """

        self.processing = None
        """ Any processing of the product during collection.
        List of `BiologicallyDerivedProductProcessing` items (represented as `dict` in JSON). """

        self.productCategory = None
        """ organ | tissue | fluid | cells | biologicalAgent.
        Type `str`. """

        self.productCode = None
        """ What this biologically derived product is.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.quantity = None
        """ The amount of this biologically derived product.
        Type `int`. """

        self.request = None
        """ Procedure request.
        List of `FHIRReference` items referencing `['ServiceRequest']` (represented as `dict` in JSON). """

        self.status = None
        """ available | unavailable.
        Type `str`. """

        self.storage = None
        """ Product storage.
        List of `BiologicallyDerivedProductStorage` items (represented as `dict` in JSON). """

        super(BiologicallyDerivedProduct, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(BiologicallyDerivedProduct, self).elementProperties()
        js.extend(
            [
                (
                    "collection",
                    "collection",
                    BiologicallyDerivedProductCollection,
                    "BiologicallyDerivedProductCollection",
                    False,
                    None,
                    False,
                ),
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
                    "manipulation",
                    "manipulation",
                    BiologicallyDerivedProductManipulation,
                    "BiologicallyDerivedProductManipulation",
                    False,
                    None,
                    False,
                ),
                (
                    "parent",
                    "parent",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "processing",
                    "processing",
                    BiologicallyDerivedProductProcessing,
                    "BiologicallyDerivedProductProcessing",
                    True,
                    None,
                    False,
                ),
                ("productCategory", "productCategory", str, "code", False, None, False),
                (
                    "productCode",
                    "productCode",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("quantity", "quantity", int, "integer", False, None, False),
                (
                    "request",
                    "request",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
                (
                    "storage",
                    "storage",
                    BiologicallyDerivedProductStorage,
                    "BiologicallyDerivedProductStorage",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class BiologicallyDerivedProductCollection(backboneelement.BackboneElement):
    """ How this product was collected.
    """

    resource_type = "BiologicallyDerivedProductCollection"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.collectedDateTime = None
        """ Time of product collection.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.collectedPeriod = None
        """ Time of product collection.
        Type `Period` (represented as `dict` in JSON). """

        self.collector = None
        """ Individual performing collection.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.source = None
        """ Who is product from.
        Type `FHIRReference` referencing `['Patient', 'Organization']` (represented as `dict` in JSON). """

        super(BiologicallyDerivedProductCollection, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(BiologicallyDerivedProductCollection, self).elementProperties()
        js.extend(
            [
                (
                    "collectedDateTime",
                    "collectedDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "collected",
                    False,
                ),
                (
                    "collectedPeriod",
                    "collectedPeriod",
                    period.Period,
                    "Period",
                    False,
                    "collected",
                    False,
                ),
                (
                    "collector",
                    "collector",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "source",
                    "source",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class BiologicallyDerivedProductManipulation(backboneelement.BackboneElement):
    """ Any manipulation of product post-collection.

    Any manipulation of product post-collection that is intended to alter the
    product.  For example a buffy-coat enrichment or CD8 reduction of
    Peripheral Blood Stem Cells to make it more suitable for infusion.
    """

    resource_type = "BiologicallyDerivedProductManipulation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of manipulation.
        Type `str`. """

        self.timeDateTime = None
        """ Time of manipulation.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timePeriod = None
        """ Time of manipulation.
        Type `Period` (represented as `dict` in JSON). """

        super(BiologicallyDerivedProductManipulation, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(BiologicallyDerivedProductManipulation, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                (
                    "timeDateTime",
                    "timeDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "time",
                    False,
                ),
                (
                    "timePeriod",
                    "timePeriod",
                    period.Period,
                    "Period",
                    False,
                    "time",
                    False,
                ),
            ]
        )
        return js


class BiologicallyDerivedProductProcessing(backboneelement.BackboneElement):
    """ Any processing of the product during collection.

    Any processing of the product during collection that does not change the
    fundamental nature of the product. For example adding anti-coagulants
    during the collection of Peripheral Blood Stem Cells.
    """

    resource_type = "BiologicallyDerivedProductProcessing"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.additive = None
        """ Substance added during processing.
        Type `FHIRReference` referencing `['Substance']` (represented as `dict` in JSON). """

        self.description = None
        """ Description of of processing.
        Type `str`. """

        self.procedure = None
        """ Procesing code.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.timeDateTime = None
        """ Time of processing.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timePeriod = None
        """ Time of processing.
        Type `Period` (represented as `dict` in JSON). """

        super(BiologicallyDerivedProductProcessing, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(BiologicallyDerivedProductProcessing, self).elementProperties()
        js.extend(
            [
                (
                    "additive",
                    "additive",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "procedure",
                    "procedure",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "timeDateTime",
                    "timeDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "time",
                    False,
                ),
                (
                    "timePeriod",
                    "timePeriod",
                    period.Period,
                    "Period",
                    False,
                    "time",
                    False,
                ),
            ]
        )
        return js


class BiologicallyDerivedProductStorage(backboneelement.BackboneElement):
    """ Product storage.
    """

    resource_type = "BiologicallyDerivedProductStorage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.description = None
        """ Description of storage.
        Type `str`. """

        self.duration = None
        """ Storage timeperiod.
        Type `Period` (represented as `dict` in JSON). """

        self.scale = None
        """ farenheit | celsius | kelvin.
        Type `str`. """

        self.temperature = None
        """ Storage temperature.
        Type `float`. """

        super(BiologicallyDerivedProductStorage, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(BiologicallyDerivedProductStorage, self).elementProperties()
        js.extend(
            [
                ("description", "description", str, "string", False, None, False),
                ("duration", "duration", period.Period, "Period", False, None, False),
                ("scale", "scale", str, "code", False, None, False),
                ("temperature", "temperature", float, "decimal", False, None, False),
            ]
        )
        return js


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
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
