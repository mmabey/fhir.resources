# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Location
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Location(domainresource.DomainResource):
    """ Details and position information for a physical place.

    Details and position information for a physical place where services are
    provided and resources and participants may be stored, found, contained, or
    accommodated.
    """

    resource_type = "Location"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.address = None
        """ Physical location.
        Type `Address` (represented as `dict` in JSON). """

        self.alias = None
        """ A list of alternate names that the location is known as, or was
        known as, in the past.
        List of `str` items. """

        self.availabilityExceptions = None
        """ Description of availability exceptions.
        Type `str`. """

        self.description = None
        """ Additional details about the location that could be displayed as
        further information to identify the location beyond its name.
        Type `str`. """

        self.endpoint = None
        """ Technical endpoints providing access to services operated for the
        location.
        List of `FHIRReference` items referencing `['Endpoint']` (represented as `dict` in JSON). """

        self.hoursOfOperation = None
        """ What days/times during a week is this location usually open.
        List of `LocationHoursOfOperation` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Unique code or number identifying the location to its users.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.managingOrganization = None
        """ Organization responsible for provisioning and upkeep.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.mode = None
        """ instance | kind.
        Type `str`. """

        self.name = None
        """ Name of the location as used by humans.
        Type `str`. """

        self.operationalStatus = None
        """ The operational status of the location (typically only for a
        bed/room).
        Type `Coding` (represented as `dict` in JSON). """

        self.partOf = None
        """ Another Location this one is physically a part of.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.physicalType = None
        """ Physical form of the location.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.position = None
        """ The absolute geographic location.
        Type `LocationPosition` (represented as `dict` in JSON). """

        self.status = None
        """ active | suspended | inactive.
        Type `str`. """

        self.telecom = None
        """ Contact details of the location.
        List of `ContactPoint` items (represented as `dict` in JSON). """

        self.type = None
        """ Type of function performed.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        super(Location, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Location, self).elementProperties()
        js.extend(
            [
                ("address", "address", address.Address, "Address", False, None, False),
                ("alias", "alias", str, "string", True, None, False),
                (
                    "availabilityExceptions",
                    "availabilityExceptions",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "endpoint",
                    "endpoint",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "hoursOfOperation",
                    "hoursOfOperation",
                    LocationHoursOfOperation,
                    "LocationHoursOfOperation",
                    True,
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
                    "managingOrganization",
                    "managingOrganization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("mode", "mode", str, "code", False, None, False),
                ("name", "name", str, "string", False, None, False),
                (
                    "operationalStatus",
                    "operationalStatus",
                    coding.Coding,
                    "Coding",
                    False,
                    None,
                    False,
                ),
                (
                    "partOf",
                    "partOf",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "physicalType",
                    "physicalType",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "position",
                    "position",
                    LocationPosition,
                    "LocationPosition",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, False),
                (
                    "telecom",
                    "telecom",
                    contactpoint.ContactPoint,
                    "ContactPoint",
                    True,
                    None,
                    False,
                ),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class LocationHoursOfOperation(backboneelement.BackboneElement):
    """ What days/times during a week is this location usually open.
    """

    resource_type = "LocationHoursOfOperation"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.allDay = None
        """ The Location is open all day.
        Type `bool`. """

        self.closingTime = None
        """ Time that the Location closes.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.daysOfWeek = None
        """ mon | tue | wed | thu | fri | sat | sun.
        List of `str` items. """

        self.openingTime = None
        """ Time that the Location opens.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(LocationHoursOfOperation, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LocationHoursOfOperation, self).elementProperties()
        js.extend(
            [
                ("allDay", "allDay", bool, "boolean", False, None, False),
                (
                    "closingTime",
                    "closingTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    None,
                    False,
                ),
                ("daysOfWeek", "daysOfWeek", str, "code", True, None, False),
                (
                    "openingTime",
                    "openingTime",
                    fhirdate.FHIRDate,
                    "time",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class LocationPosition(backboneelement.BackboneElement):
    """ The absolute geographic location.

    The absolute geographic location of the Location, expressed using the WGS84
    datum (This is the same co-ordinate system used in KML).
    """

    resource_type = "LocationPosition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.altitude = None
        """ Altitude with WGS84 datum.
        Type `float`. """

        self.latitude = None
        """ Latitude with WGS84 datum.
        Type `float`. """

        self.longitude = None
        """ Longitude with WGS84 datum.
        Type `float`. """

        super(LocationPosition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LocationPosition, self).elementProperties()
        js.extend(
            [
                ("altitude", "altitude", float, "decimal", False, None, False),
                ("latitude", "latitude", float, "decimal", False, None, True),
                ("longitude", "longitude", float, "decimal", False, None, True),
            ]
        )
        return js


try:
    from . import address
except ImportError:
    address = sys.modules[__package__ + ".address"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import coding
except ImportError:
    coding = sys.modules[__package__ + ".coding"]
try:
    from . import contactpoint
except ImportError:
    contactpoint = sys.modules[__package__ + ".contactpoint"]
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
