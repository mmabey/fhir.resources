# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class SearchParameter(domainresource.DomainResource):
    """ Search parameter for a resource.

    A search parameter that defines a named search item that can be used to
    search/filter on a resource.
    """

    resource_type = "SearchParameter"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.base = None
        """ The resource type(s) this search parameter applies to.
        List of `str` items. """

        self.chain = None
        """ Chained names supported.
        List of `str` items. """

        self.code = None
        """ Code used in URL.
        Type `str`. """

        self.comparator = None
        """ eq | ne | gt | lt | ge | le | sa | eb | ap.
        List of `str` items. """

        self.component = None
        """ For Composite resources to define the parts.
        List of `SearchParameterComponent` items (represented as `dict` in JSON). """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.derivedFrom = None
        """ Original definition for the search parameter.
        Type `str` referencing `['SearchParameter']`. """

        self.description = None
        """ Natural language description of the search parameter.
        Type `str`. """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.expression = None
        """ FHIRPath expression that extracts the values.
        Type `str`. """

        self.jurisdiction = None
        """ Intended jurisdiction for search parameter (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.modifier = None
        """ missing | exact | contains | not | text | in | not-in | below |
        above | type | identifier | ofType.
        List of `str` items. """

        self.multipleAnd = None
        """ Allow multiple parameters (and).
        Type `bool`. """

        self.multipleOr = None
        """ Allow multiple values per parameter (or).
        Type `bool`. """

        self.name = None
        """ Name for this search parameter (computer friendly).
        Type `str`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this search parameter is defined.
        Type `str`. """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.target = None
        """ Types of resource (if a resource reference).
        List of `str` items. """

        self.type = None
        """ number | date | string | token | reference | composite | quantity |
        uri | special.
        Type `str`. """

        self.url = None
        """ Canonical identifier for this search parameter, represented as a
        URI (globally unique).
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the search parameter.
        Type `str`. """

        self.xpath = None
        """ XPath that extracts the values.
        Type `str`. """

        self.xpathUsage = None
        """ normal | phonetic | nearby | distance | other.
        Type `str`. """

        super(SearchParameter, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameter, self).elementProperties()
        js.extend(
            [
                ("base", "base", str, "code", True, None, True),
                ("chain", "chain", str, "string", True, None, False),
                ("code", "code", str, "code", False, None, True),
                ("comparator", "comparator", str, "code", True, None, False),
                (
                    "component",
                    "component",
                    SearchParameterComponent,
                    "SearchParameterComponent",
                    True,
                    None,
                    False,
                ),
                (
                    "contact",
                    "contact",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("derivedFrom", "derivedFrom", str, "canonical", False, None, False),
                ("description", "description", str, "markdown", False, None, True),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                ("expression", "expression", str, "string", False, None, False),
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("modifier", "modifier", str, "code", True, None, False),
                ("multipleAnd", "multipleAnd", bool, "boolean", False, None, False),
                ("multipleOr", "multipleOr", bool, "boolean", False, None, False),
                ("name", "name", str, "string", False, None, True),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                ("status", "status", str, "code", False, None, True),
                ("target", "target", str, "code", True, None, False),
                ("type", "type", str, "code", False, None, True),
                ("url", "url", str, "uri", False, None, True),
                (
                    "useContext",
                    "useContext",
                    usagecontext.UsageContext,
                    "UsageContext",
                    True,
                    None,
                    False,
                ),
                ("version", "version", str, "string", False, None, False),
                ("xpath", "xpath", str, "string", False, None, False),
                ("xpathUsage", "xpathUsage", str, "code", False, None, False),
            ]
        )
        return js


class SearchParameterComponent(backboneelement.BackboneElement):
    """ For Composite resources to define the parts.

    Used to define the parts of a composite search parameter.
    """

    resource_type = "SearchParameterComponent"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.definition = None
        """ Defines how the part works.
        Type `str` referencing `['SearchParameter']`. """

        self.expression = None
        """ Subexpression relative to main expression.
        Type `str`. """

        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend(
            [
                ("definition", "definition", str, "canonical", False, None, True),
                ("expression", "expression", str, "string", False, None, True),
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
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
