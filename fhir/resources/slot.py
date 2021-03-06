# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Slot
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import domainresource


class Slot(domainresource.DomainResource):
    """ A slot of time on a schedule that may be available for booking appointments.
    """

    resource_type = "Slot"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.appointmentType = None
        """ The style of appointment or patient that may be booked in the slot
        (not service type).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.comment = None
        """ Comments on the slot to describe any extended information. Such as
        custom constraints on the slot.
        Type `str`. """

        self.end = None
        """ Date/Time that the slot is to conclude.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.identifier = None
        """ External Ids for this item.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.overbooked = None
        """ This slot has already been overbooked, appointments are unlikely to
        be accepted for this time.
        Type `bool`. """

        self.schedule = None
        """ The schedule resource that this slot defines an interval of status
        information.
        Type `FHIRReference` referencing `['Schedule']` (represented as `dict` in JSON). """

        self.serviceCategory = None
        """ A broad categorization of the service that is to be performed
        during this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.serviceType = None
        """ The type of appointments that can be booked into this slot (ideally
        this would be an identifiable service - which is at a location,
        rather than the location itself). If provided then this overrides
        the value provided on the availability resource.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.specialty = None
        """ The specialty of a practitioner that would be required to perform
        the service requested in this appointment.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.start = None
        """ Date/Time that the slot is to begin.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.status = None
        """ busy | free | busy-unavailable | busy-tentative | entered-in-error.
        Type `str`. """

        super(Slot, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Slot, self).elementProperties()
        js.extend(
            [
                (
                    "appointmentType",
                    "appointmentType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("comment", "comment", str, "string", False, None, False),
                ("end", "end", fhirdate.FHIRDate, "instant", False, None, True),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("overbooked", "overbooked", bool, "boolean", False, None, False),
                (
                    "schedule",
                    "schedule",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                (
                    "serviceCategory",
                    "serviceCategory",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "serviceType",
                    "serviceType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "specialty",
                    "specialty",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("start", "start", fhirdate.FHIRDate, "instant", False, None, True),
                ("status", "status", str, "code", False, None, True),
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
