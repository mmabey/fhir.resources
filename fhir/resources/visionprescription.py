# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the provision of glasses and/or contact lenses to a
    patient.
    """

    resource_type = "VisionPrescription"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.created = None
        """ Response creation date.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business Identifier for vision prescription.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.lensSpecification = None
        """ Vision lens authorization.
        List of `VisionPrescriptionLensSpecification` items (represented as `dict` in JSON). """

        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.prescriber = None
        """ Who authorized the vision prescription.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend(
            [
                (
                    "created",
                    "created",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    True,
                ),
                (
                    "dateWritten",
                    "dateWritten",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    True,
                ),
                (
                    "encounter",
                    "encounter",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "lensSpecification",
                    "lensSpecification",
                    VisionPrescriptionLensSpecification,
                    "VisionPrescriptionLensSpecification",
                    True,
                    None,
                    True,
                ),
                (
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "prescriber",
                    "prescriber",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("status", "status", str, "code", False, None, True),
            ]
        )
        return js


class VisionPrescriptionLensSpecification(backboneelement.BackboneElement):
    """ Vision lens authorization.

    Contain the details of  the individual lens specifications and serves as
    the authorization for the fullfillment by certified professionals.
    """

    resource_type = "VisionPrescriptionLensSpecification"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.add = None
        """ Added power for multifocal levels.
        Type `float`. """

        self.axis = None
        """ Lens meridian which contain no power for astigmatism.
        Type `int`. """

        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """

        self.brand = None
        """ Brand required.
        Type `str`. """

        self.color = None
        """ Color required.
        Type `str`. """

        self.cylinder = None
        """ Lens power for astigmatism.
        Type `float`. """

        self.diameter = None
        """ Contact lens diameter.
        Type `float`. """

        self.duration = None
        """ Lens wear duration.
        Type `Quantity` (represented as `dict` in JSON). """

        self.eye = None
        """ right | left.
        Type `str`. """

        self.note = None
        """ Notes for coatings.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.power = None
        """ Contact lens power.
        Type `float`. """

        self.prism = None
        """ Eye alignment compensation.
        List of `VisionPrescriptionLensSpecificationPrism` items (represented as `dict` in JSON). """

        self.product = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sphere = None
        """ Power of the lens.
        Type `float`. """

        super(VisionPrescriptionLensSpecification, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecification, self).elementProperties()
        js.extend(
            [
                ("add", "add", float, "decimal", False, None, False),
                ("axis", "axis", int, "integer", False, None, False),
                ("backCurve", "backCurve", float, "decimal", False, None, False),
                ("brand", "brand", str, "string", False, None, False),
                ("color", "color", str, "string", False, None, False),
                ("cylinder", "cylinder", float, "decimal", False, None, False),
                ("diameter", "diameter", float, "decimal", False, None, False),
                (
                    "duration",
                    "duration",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                ("eye", "eye", str, "code", False, None, True),
                (
                    "note",
                    "note",
                    annotation.Annotation,
                    "Annotation",
                    True,
                    None,
                    False,
                ),
                ("power", "power", float, "decimal", False, None, False),
                (
                    "prism",
                    "prism",
                    VisionPrescriptionLensSpecificationPrism,
                    "VisionPrescriptionLensSpecificationPrism",
                    True,
                    None,
                    False,
                ),
                (
                    "product",
                    "product",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                ("sphere", "sphere", float, "decimal", False, None, False),
            ]
        )
        return js


class VisionPrescriptionLensSpecificationPrism(backboneelement.BackboneElement):
    """ Eye alignment compensation.

    Allows for adjustment on two axis.
    """

    resource_type = "VisionPrescriptionLensSpecificationPrism"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.amount = None
        """ Amount of adjustment.
        Type `float`. """

        self.base = None
        """ up | down | in | out.
        Type `str`. """

        super(VisionPrescriptionLensSpecificationPrism, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(VisionPrescriptionLensSpecificationPrism, self).elementProperties()
        js.extend(
            [
                ("amount", "amount", float, "decimal", False, None, True),
                ("base", "base", str, "code", False, None, True),
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
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
