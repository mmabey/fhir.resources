# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/NamingSystem
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class NamingSystem(domainresource.DomainResource):
    """ System of unique identification.

    A curated namespace that issues unique symbols within that namespace for
    the identification of concepts, people, devices, etc.  Represents a
    "System" used within the Identifier and Coding data types.
    """

    resource_type = "NamingSystem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the naming system.
        Type `str`. """

        self.jurisdiction = None
        """ Intended jurisdiction for naming system (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.kind = None
        """ codesystem | identifier | root.
        Type `str`. """

        self.name = None
        """ Name for this naming system (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.responsible = None
        """ Who maintains system namespace?.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.type = None
        """ e.g. driver,  provider,  patient, bank etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.uniqueId = None
        """ Unique identifiers used for system.
        List of `NamingSystemUniqueId` items (represented as `dict` in JSON). """

        self.usage = None
        """ How/where is it used.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        super(NamingSystem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NamingSystem, self).elementProperties()
        js.extend(
            [
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, True),
                ("description", "description", str, "markdown", False, None, False),
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("kind", "kind", str, "code", False, None, True),
                ("name", "name", str, "string", False, None, True),
                ("publisher", "publisher", str, "string", False, None, False),
                ("responsible", "responsible", str, "string", False, None, False),
                ("status", "status", str, "code", False, None, True),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "uniqueId",
                    "uniqueId",
                    NamingSystemUniqueId,
                    "NamingSystemUniqueId",
                    True,
                    None,
                    True,
                ),
                ("usage", "usage", str, "string", False, None, False),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class NamingSystemUniqueId(backboneelement.BackboneElement):
    """ Unique identifiers used for system.

    Indicates how the system may be identified when referenced in electronic
    exchange.
    """

    resource_type = "NamingSystemUniqueId"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.comment = None
        """ Notes about identifier usage.
        Type `str`. """

        self.period = None
        """ When is identifier valid?.
        Type `Period` (represented as `dict` in JSON). """

        self.preferred = None
        """ Is this the id that should be used for this type.
        Type `bool`. """

        self.type = None
        """ oid | uuid | uri | other.
        Type `str`. """

        self.value = None
        """ The unique identifier.
        Type `str`. """

        super(NamingSystemUniqueId, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(NamingSystemUniqueId, self).elementProperties()
        js.extend(
            [
                ("comment", "comment", str, "string", False, None, False),
                ("period", "period", period.Period, "Period", False, None, False),
                ("preferred", "preferred", bool, "boolean", False, None, False),
                ("type", "type", str, "code", False, None, True),
                ("value", "value", str, "string", False, None, True),
            ]
        )
        return js


try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + ".fhirdate"]
try:
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
