# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/SearchParameter
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class SearchParameter(domainresource.DomainResource):
    """ Search Parameter for a resource.

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
        """ Date this was last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.derivedFrom = None
        """ Original Definition for the search parameter.
        Type `str`. """

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
        above | type.
        List of `str` items. """

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
        uri.
        Type `str`. """

        self.url = None
        """ Logical URI to reference this search parameter (globally unique).
        Type `str`. """

        self.useContext = None
        """ Context the content is intended to support.
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
                ("derivedFrom", "derivedFrom", str, "uri", False, None, False),
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
        Type `FHIRReference` referencing `['SearchParameter']` (represented as `dict` in JSON). """

        self.expression = None
        """ Subexpression relative to main expression.
        Type `str`. """

        super(SearchParameterComponent, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(SearchParameterComponent, self).elementProperties()
        js.extend(
            [
                (
                    "definition",
                    "definition",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
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
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + ".fhirreference"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
