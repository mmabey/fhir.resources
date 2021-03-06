# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Linkage
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Linkage(domainresource.DomainResource):
    """ Links records for 'same' item.

    Identifies two or more records (resource instances) that refer to the same
    real-world "occurrence".
    """

    resource_type = "Linkage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.active = None
        """ Whether this linkage assertion is active or not.
        Type `bool`. """

        self.author = None
        """ Who is responsible for linkages.
        Type `FHIRReference` referencing `['Practitioner', 'PractitionerRole', 'Organization']` (represented as `dict` in JSON). """

        self.item = None
        """ Item to be linked.
        List of `LinkageItem` items (represented as `dict` in JSON). """

        super(Linkage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Linkage, self).elementProperties()
        js.extend(
            [
                ("active", "active", bool, "boolean", False, None, False),
                (
                    "author",
                    "author",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("item", "item", LinkageItem, "LinkageItem", True, None, True),
            ]
        )
        return js


class LinkageItem(backboneelement.BackboneElement):
    """ Item to be linked.

    Identifies which record considered as the reference to the same real-world
    occurrence as well as how the items should be evaluated within the
    collection of linked items.
    """

    resource_type = "LinkageItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.resource = None
        """ Resource being linked.
        Type `FHIRReference` referencing `['Resource']` (represented as `dict` in JSON). """

        self.type = None
        """ source | alternate | historical.
        Type `str`. """

        super(LinkageItem, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(LinkageItem, self).elementProperties()
        js.extend(
            [
                (
                    "resource",
                    "resource",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
