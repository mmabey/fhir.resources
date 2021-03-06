# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ObservationDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class ObservationDefinition(domainresource.DomainResource):
    """ Definition of an observation.

    Set of definitional characteristics for a kind of observation or
    measurement produced or consumed by an orderable health care service.
    """

    resource_type = "ObservationDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.abnormalCodedValueSet = None
        """ Value set of abnormal coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` referencing `['ValueSet']` (represented as `dict` in JSON). """

        self.category = None
        """ Category of observation.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ Type of observation (code / type).
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.criticalCodedValueSet = None
        """ Value set of critical coded values for the observations conforming
        to this ObservationDefinition.
        Type `FHIRReference` referencing `['ValueSet']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Business identifier for this ObservationDefinition instance.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.method = None
        """ Method used to produce the observation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.multipleResultsAllowed = None
        """ Multiple results allowed.
        Type `bool`. """

        self.normalCodedValueSet = None
        """ Value set of normal coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` referencing `['ValueSet']` (represented as `dict` in JSON). """

        self.permittedDataType = None
        """ Quantity | CodeableConcept | string | boolean | integer | Range |
        Ratio | SampledData | time | dateTime | Period.
        List of `str` items. """

        self.preferredReportName = None
        """ Preferred report name.
        Type `str`. """

        self.qualifiedInterval = None
        """ Qualified range for continuous and ordinal observation results.
        List of `ObservationDefinitionQualifiedInterval` items (represented as `dict` in JSON). """

        self.quantitativeDetails = None
        """ Characteristics of quantitative results.
        Type `ObservationDefinitionQuantitativeDetails` (represented as `dict` in JSON). """

        self.validCodedValueSet = None
        """ Value set of valid coded values for the observations conforming to
        this ObservationDefinition.
        Type `FHIRReference` referencing `['ValueSet']` (represented as `dict` in JSON). """

        super(ObservationDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ObservationDefinition, self).elementProperties()
        js.extend(
            [
                (
                    "abnormalCodedValueSet",
                    "abnormalCodedValueSet",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "category",
                    "category",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "code",
                    "code",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    True,
                ),
                (
                    "criticalCodedValueSet",
                    "criticalCodedValueSet",
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
                    "method",
                    "method",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "multipleResultsAllowed",
                    "multipleResultsAllowed",
                    bool,
                    "boolean",
                    False,
                    None,
                    False,
                ),
                (
                    "normalCodedValueSet",
                    "normalCodedValueSet",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "permittedDataType",
                    "permittedDataType",
                    str,
                    "code",
                    True,
                    None,
                    False,
                ),
                (
                    "preferredReportName",
                    "preferredReportName",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                (
                    "qualifiedInterval",
                    "qualifiedInterval",
                    ObservationDefinitionQualifiedInterval,
                    "ObservationDefinitionQualifiedInterval",
                    True,
                    None,
                    False,
                ),
                (
                    "quantitativeDetails",
                    "quantitativeDetails",
                    ObservationDefinitionQuantitativeDetails,
                    "ObservationDefinitionQuantitativeDetails",
                    False,
                    None,
                    False,
                ),
                (
                    "validCodedValueSet",
                    "validCodedValueSet",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class ObservationDefinitionQualifiedInterval(backboneelement.BackboneElement):
    """ Qualified range for continuous and ordinal observation results.

    Multiple  ranges of results qualified by different contexts for ordinal or
    continuous observations conforming to this ObservationDefinition.
    """

    resource_type = "ObservationDefinitionQualifiedInterval"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.age = None
        """ Applicable age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """

        self.appliesTo = None
        """ Targetted population of the range.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.category = None
        """ reference | critical | absolute.
        Type `str`. """

        self.condition = None
        """ Condition associated with the reference range.
        Type `str`. """

        self.context = None
        """ Range context qualifier.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.gender = None
        """ male | female | other | unknown.
        Type `str`. """

        self.gestationalAge = None
        """ Applicable gestational age range, if relevant.
        Type `Range` (represented as `dict` in JSON). """

        self.range = None
        """ The interval itself, for continuous or ordinal observations.
        Type `Range` (represented as `dict` in JSON). """

        super(ObservationDefinitionQualifiedInterval, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ObservationDefinitionQualifiedInterval, self).elementProperties()
        js.extend(
            [
                ("age", "age", range.Range, "Range", False, None, False),
                (
                    "appliesTo",
                    "appliesTo",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("category", "category", str, "code", False, None, False),
                ("condition", "condition", str, "string", False, None, False),
                (
                    "context",
                    "context",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("gender", "gender", str, "code", False, None, False),
                (
                    "gestationalAge",
                    "gestationalAge",
                    range.Range,
                    "Range",
                    False,
                    None,
                    False,
                ),
                ("range", "range", range.Range, "Range", False, None, False),
            ]
        )
        return js


class ObservationDefinitionQuantitativeDetails(backboneelement.BackboneElement):
    """ Characteristics of quantitative results.

    Characteristics for quantitative results of this observation.
    """

    resource_type = "ObservationDefinitionQuantitativeDetails"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.conversionFactor = None
        """ SI to Customary unit conversion factor.
        Type `float`. """

        self.customaryUnit = None
        """ Customary unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.decimalPrecision = None
        """ Decimal precision of observation quantitative results.
        Type `int`. """

        self.unit = None
        """ SI unit for quantitative results.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(ObservationDefinitionQuantitativeDetails, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ObservationDefinitionQuantitativeDetails, self).elementProperties()
        js.extend(
            [
                (
                    "conversionFactor",
                    "conversionFactor",
                    float,
                    "decimal",
                    False,
                    None,
                    False,
                ),
                (
                    "customaryUnit",
                    "customaryUnit",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "decimalPrecision",
                    "decimalPrecision",
                    int,
                    "integer",
                    False,
                    None,
                    False,
                ),
                (
                    "unit",
                    "unit",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


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
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
