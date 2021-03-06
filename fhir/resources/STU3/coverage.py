# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Coverage
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""


import sys

from . import backboneelement, domainresource


class Coverage(domainresource.DomainResource):
    """ Insurance or medical plan or a payment agreement.

    Financial instrument which may be used to reimburse or pay for health care
    products and services.
    """

    resource_type = "Coverage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.beneficiary = None
        """ Plan Beneficiary.
        Type `FHIRReference` referencing `['Patient']` (represented as `dict` in JSON). """

        self.contract = None
        """ Contract details.
        List of `FHIRReference` items referencing `['Contract']` (represented as `dict` in JSON). """

        self.dependent = None
        """ Dependent number.
        Type `str`. """

        self.grouping = None
        """ Additional coverage classifications.
        Type `CoverageGrouping` (represented as `dict` in JSON). """

        self.identifier = None
        """ The primary coverage ID.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.network = None
        """ Insurer network.
        Type `str`. """

        self.order = None
        """ Relative order of the coverage.
        Type `int`. """

        self.payor = None
        """ Identifier for the plan or agreement issuer.
        List of `FHIRReference` items referencing `['Organization'], ['Patient'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.period = None
        """ Coverage start and end dates.
        Type `Period` (represented as `dict` in JSON). """

        self.policyHolder = None
        """ Owner of the policy.
        Type `FHIRReference` referencing `['Patient'], ['RelatedPerson'], ['Organization']` (represented as `dict` in JSON). """

        self.relationship = None
        """ Beneficiary relationship to the Subscriber.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.sequence = None
        """ The plan instance or sequence counter.
        Type `str`. """

        self.status = None
        """ active | cancelled | draft | entered-in-error.
        Type `str`. """

        self.subscriber = None
        """ Subscriber to the policy.
        Type `FHIRReference` referencing `['Patient'], ['RelatedPerson']` (represented as `dict` in JSON). """

        self.subscriberId = None
        """ ID assigned to the Subscriber.
        Type `str`. """

        self.type = None
        """ Type of coverage such as medical or accident.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Coverage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Coverage, self).elementProperties()
        js.extend(
            [
                (
                    "beneficiary",
                    "beneficiary",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "contract",
                    "contract",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("dependent", "dependent", str, "string", False, None, False),
                (
                    "grouping",
                    "grouping",
                    CoverageGrouping,
                    "CoverageGrouping",
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
                ("network", "network", str, "string", False, None, False),
                ("order", "order", int, "positiveInt", False, None, False),
                (
                    "payor",
                    "payor",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
                (
                    "policyHolder",
                    "policyHolder",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "relationship",
                    "relationship",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("sequence", "sequence", str, "string", False, None, False),
                ("status", "status", str, "code", False, None, False),
                (
                    "subscriber",
                    "subscriber",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("subscriberId", "subscriberId", str, "string", False, None, False),
                (
                    "type",
                    "type",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
            ]
        )
        return js


class CoverageGrouping(backboneelement.BackboneElement):
    """ Additional coverage classifications.

    A suite of underwrite specific classifiers, for example may be used to
    identify a class of coverage or employer group, Policy, Plan.
    """

    resource_type = "CoverageGrouping"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.classDisplay = None
        """ Display text for the class.
        Type `str`. """

        self.class_fhir = None
        """ An identifier for the class.
        Type `str`. """

        self.group = None
        """ An identifier for the group.
        Type `str`. """

        self.groupDisplay = None
        """ Display text for an identifier for the group.
        Type `str`. """

        self.plan = None
        """ An identifier for the plan.
        Type `str`. """

        self.planDisplay = None
        """ Display text for the plan.
        Type `str`. """

        self.subClass = None
        """ An identifier for the subsection of the class.
        Type `str`. """

        self.subClassDisplay = None
        """ Display text for the subsection of the subclass.
        Type `str`. """

        self.subGroup = None
        """ An identifier for the subsection of the group.
        Type `str`. """

        self.subGroupDisplay = None
        """ Display text for the subsection of the group.
        Type `str`. """

        self.subPlan = None
        """ An identifier for the subsection of the plan.
        Type `str`. """

        self.subPlanDisplay = None
        """ Display text for the subsection of the plan.
        Type `str`. """

        super(CoverageGrouping, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(CoverageGrouping, self).elementProperties()
        js.extend(
            [
                ("classDisplay", "classDisplay", str, "string", False, None, False),
                ("class_fhir", "class", str, "string", False, None, False),
                ("group", "group", str, "string", False, None, False),
                ("groupDisplay", "groupDisplay", str, "string", False, None, False),
                ("plan", "plan", str, "string", False, None, False),
                ("planDisplay", "planDisplay", str, "string", False, None, False),
                ("subClass", "subClass", str, "string", False, None, False),
                (
                    "subClassDisplay",
                    "subClassDisplay",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("subGroup", "subGroup", str, "string", False, None, False),
                (
                    "subGroupDisplay",
                    "subGroupDisplay",
                    str,
                    "string",
                    False,
                    None,
                    False,
                ),
                ("subPlan", "subPlan", str, "string", False, None, False),
                ("subPlanDisplay", "subPlanDisplay", str, "string", False, None, False),
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
