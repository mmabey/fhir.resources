# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/VisionPrescription
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class VisionPrescription(domainresource.DomainResource):
    """ Prescription for vision correction products for a patient.

    An authorization for the supply of glasses and/or contact lenses to a
    patient.
    """

    resource_type = "VisionPrescription"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.dateWritten = None
        """ When prescription was authorized.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.dispense = None
        """ Vision supply authorization.
        List of `VisionPrescriptionDispense` items (represented as `dict` in JSON). """

        self.encounter = None
        """ Created during encounter / admission / stay.
        Type `FHIRReference` referencing `['Encounter']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.patient = None
        """ Who prescription is for.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.prescriber = None
        """ Who authorizes the vision product.
        Type `FHIRReference` referencing `['Practitioner']` (represented as `dict` in JSON). """

        self.reasonCodeableConcept = None
        """ Reason or indication for writing the prescription.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.reasonReference = None
        """ Reason or indication for writing the prescription.
        Type `FHIRReference` referencing `['Condition']` (represented as `dict` in JSON). """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        super(VisionPrescription, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(VisionPrescription, self).elementProperties()
        js.extend(
            [
                (
                    "dateWritten",
                    "dateWritten",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    None,
                    False,
                ),
                (
                    "dispense",
                    "dispense",
                    VisionPrescriptionDispense,
                    "VisionPrescriptionDispense",
                    True,
                    None,
                    False,
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
                    "patient",
                    "patient",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "prescriber",
                    "prescriber",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "reasonCodeableConcept",
                    "reasonCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "reason",
                    False,
                ),
                (
                    "reasonReference",
                    "reasonReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "reason",
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
            ]
        )
        return js


class VisionPrescriptionDispense(backboneelement.BackboneElement):
    """ Vision supply authorization.

    Deals with details of the dispense part of the supply specification.
    """

    resource_type = "VisionPrescriptionDispense"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.add = None
        """ Lens add.
        Type `float`. """

        self.axis = None
        """ Lens axis.
        Type `int`. """

        self.backCurve = None
        """ Contact lens back curvature.
        Type `float`. """

        self.base = None
        """ up | down | in | out.
        Type `str`. """

        self.brand = None
        """ Brand required.
        Type `str`. """

        self.color = None
        """ Color required.
        Type `str`. """

        self.cylinder = None
        """ Lens cylinder.
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
        """ Lens prism.
        Type `float`. """

        self.product = None
        """ Product to be supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sphere = None
        """ Lens sphere.
        Type `float`. """

        super(VisionPrescriptionDispense, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(VisionPrescriptionDispense, self).elementProperties()
        js.extend(
            [
                ("add", "add", float, "decimal", False, None, False),
                ("axis", "axis", int, "integer", False, None, False),
                ("backCurve", "backCurve", float, "decimal", False, None, False),
                ("base", "base", str, "code", False, None, False),
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
                ("eye", "eye", str, "code", False, None, False),
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
                ("prism", "prism", float, "decimal", False, None, False),
                (
                    "product",
                    "product",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sphere", "sphere", float, "decimal", False, None, False),
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
