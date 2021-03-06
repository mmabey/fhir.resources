# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/BodyStructure
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class BodyStructure(domainresource.DomainResource):
    """ Specific and identified anatomical structure.

    Record details about an anatomical structure.  This resource may be used
    when a coded concept does not provide the necessary detail needed for the
    use case.
    """

    resource_type = "BodyStructure"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this record is in active use.
        Type `bool`. """

        self.description = None
        """ Text description.
        Type `str`. """

        self.identifier = None
        """ Bodystructure identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.image = None
        """ Attached images.
        List of `Attachment` items (represented as `dict` in JSON). """

        self.location = None
        """ Body site.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.locationQualifier = None
        """ Body site modifier.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.morphology = None
        """ Kind of Structure.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.patient = None
        """ Who this is about.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        super(BodyStructure, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(BodyStructure, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, "boolean", False, None, False),
                ("description", "description", str, "string", False, None, False),
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
                    "image",
                    "image",
                    attachment.Attachment,
                    "Attachment",
                    True,
                    None,
                    False,
                ),
                (
                    "location",
                    "location",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "locationQualifier",
                    "locationQualifier",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "morphology",
                    "morphology",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
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
                    True,
                ),
            ]
        )
        return js


try:
    from . import attachment
except ImportError:
    attachment = sys.modules[__package__ + ".attachment"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + ".identifier"]
