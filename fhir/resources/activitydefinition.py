# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ActivityDefinition
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class ActivityDefinition(domainresource.DomainResource):
    """ The definition of a specific activity to be taken, independent of any
    particular patient or context.

    This resource allows for the definition of some activity to be performed,
    independent of a particular patient, practitioner, or other performance
    context.
    """

    resource_type = "ActivityDefinition"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.approvalDate = None
        """ When the activity definition was approved by publisher.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.author = None
        """ Who authored the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.bodySite = None
        """ What part of body to perform on.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.code = None
        """ Detail type of activity.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.contact = None
        """ Contact details for the publisher.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.copyright = None
        """ Use and/or publishing restrictions.
        Type `str`. """

        self.date = None
        """ Date last changed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.description = None
        """ Natural language description of the activity definition.
        Type `str`. """

        self.doNotPerform = None
        """ True if the activity should not be performed.
        Type `bool`. """

        self.dosage = None
        """ Detailed dosage instructions.
        List of `Dosage` items (represented as `dict` in JSON). """

        self.dynamicValue = None
        """ Dynamic aspects of the definition.
        List of `ActivityDefinitionDynamicValue` items (represented as `dict` in JSON). """

        self.editor = None
        """ Who edited the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.effectivePeriod = None
        """ When the activity definition is expected to be used.
        Type `Period` (represented as `dict` in JSON). """

        self.endorser = None
        """ Who endorsed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.experimental = None
        """ For testing purposes, not real usage.
        Type `bool`. """

        self.identifier = None
        """ Additional identifier for the activity definition.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.intent = None
        """ proposal | plan | directive | order | original-order | reflex-order
        | filler-order | instance-order | option.
        Type `str`. """

        self.jurisdiction = None
        """ Intended jurisdiction for activity definition (if applicable).
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.kind = None
        """ Kind of resource.
        Type `str`. """

        self.lastReviewDate = None
        """ When the activity definition was last reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.library = None
        """ Logic used by the activity definition.
        List of `str` items referencing `['Library']`. """

        self.location = None
        """ Where it should happen.
        Type `FHIRReference` referencing `['Location']` (represented as `dict` in JSON). """

        self.name = None
        """ Name for this activity definition (computer friendly).
        Type `str`. """

        self.observationRequirement = None
        """ What observations are required to perform this action.
        List of `FHIRReference` items referencing `['ObservationDefinition']` (represented as `dict` in JSON). """

        self.observationResultRequirement = None
        """ What observations must be produced by this action.
        List of `FHIRReference` items referencing `['ObservationDefinition']` (represented as `dict` in JSON). """

        self.participant = None
        """ Who should participate in the action.
        List of `ActivityDefinitionParticipant` items (represented as `dict` in JSON). """

        self.priority = None
        """ routine | urgent | asap | stat.
        Type `str`. """

        self.productCodeableConcept = None
        """ What's administered/supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.productReference = None
        """ What's administered/supplied.
        Type `FHIRReference` referencing `['Medication', 'Substance']` (represented as `dict` in JSON). """

        self.profile = None
        """ What profile the resource needs to conform to.
        Type `str` referencing `['StructureDefinition']`. """

        self.publisher = None
        """ Name of the publisher (organization or individual).
        Type `str`. """

        self.purpose = None
        """ Why this activity definition is defined.
        Type `str`. """

        self.quantity = None
        """ How much is administered/consumed/supplied.
        Type `Quantity` (represented as `dict` in JSON). """

        self.relatedArtifact = None
        """ Additional documentation, citations, etc..
        List of `RelatedArtifact` items (represented as `dict` in JSON). """

        self.reviewer = None
        """ Who reviewed the content.
        List of `ContactDetail` items (represented as `dict` in JSON). """

        self.specimenRequirement = None
        """ What specimens are required to perform this action.
        List of `FHIRReference` items referencing `['SpecimenDefinition']` (represented as `dict` in JSON). """

        self.status = None
        """ draft | active | retired | unknown.
        Type `str`. """

        self.subjectCodeableConcept = None
        """ Type of individual the activity definition is intended for.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.subjectReference = None
        """ Type of individual the activity definition is intended for.
        Type `FHIRReference` referencing `['Group']` (represented as `dict` in JSON). """

        self.subtitle = None
        """ Subordinate title of the activity definition.
        Type `str`. """

        self.timingAge = None
        """ When activity is to occur.
        Type `Age` (represented as `dict` in JSON). """

        self.timingDateTime = None
        """ When activity is to occur.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.timingDuration = None
        """ When activity is to occur.
        Type `Duration` (represented as `dict` in JSON). """

        self.timingPeriod = None
        """ When activity is to occur.
        Type `Period` (represented as `dict` in JSON). """

        self.timingRange = None
        """ When activity is to occur.
        Type `Range` (represented as `dict` in JSON). """

        self.timingTiming = None
        """ When activity is to occur.
        Type `Timing` (represented as `dict` in JSON). """

        self.title = None
        """ Name for this activity definition (human friendly).
        Type `str`. """

        self.topic = None
        """ E.g. Education, Treatment, Assessment, etc..
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.transform = None
        """ Transform to apply the template.
        Type `str` referencing `['StructureMap']`. """

        self.url = None
        """ Canonical identifier for this activity definition, represented as a
        URI (globally unique).
        Type `str`. """

        self.usage = None
        """ Describes the clinical usage of the activity definition.
        Type `str`. """

        self.useContext = None
        """ The context that the content is intended to support.
        List of `UsageContext` items (represented as `dict` in JSON). """

        self.version = None
        """ Business version of the activity definition.
        Type `str`. """

        super(ActivityDefinition, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(ActivityDefinition, self).elementProperties()
        js.extend(
            [
                (
                    "approvalDate",
                    "approvalDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                (
                    "author",
                    "author",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "bodySite",
                    "bodySite",
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
                ("copyright", "copyright", str, "markdown", False, None, False),
                ("date", "date", fhirdate.FHIRDate, "dateTime", False, None, False),
                ("description", "description", str, "markdown", False, None, False),
                ("doNotPerform", "doNotPerform", bool, "boolean", False, None, False),
                ("dosage", "dosage", dosage.Dosage, "Dosage", True, None, False),
                (
                    "dynamicValue",
                    "dynamicValue",
                    ActivityDefinitionDynamicValue,
                    "ActivityDefinitionDynamicValue",
                    True,
                    None,
                    False,
                ),
                (
                    "editor",
                    "editor",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "effectivePeriod",
                    "effectivePeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
                (
                    "endorser",
                    "endorser",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                ("experimental", "experimental", bool, "boolean", False, None, False),
                (
                    "identifier",
                    "identifier",
                    identifier.Identifier,
                    "Identifier",
                    True,
                    None,
                    False,
                ),
                ("intent", "intent", str, "code", False, None, False),
                (
                    "jurisdiction",
                    "jurisdiction",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("kind", "kind", str, "code", False, None, False),
                (
                    "lastReviewDate",
                    "lastReviewDate",
                    fhirdate.FHIRDate,
                    "date",
                    False,
                    None,
                    False,
                ),
                ("library", "library", str, "canonical", True, None, False),
                (
                    "location",
                    "location",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                ("name", "name", str, "string", False, None, False),
                (
                    "observationRequirement",
                    "observationRequirement",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "observationResultRequirement",
                    "observationResultRequirement",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "participant",
                    "participant",
                    ActivityDefinitionParticipant,
                    "ActivityDefinitionParticipant",
                    True,
                    None,
                    False,
                ),
                ("priority", "priority", str, "code", False, None, False),
                (
                    "productCodeableConcept",
                    "productCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "product",
                    False,
                ),
                (
                    "productReference",
                    "productReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "product",
                    False,
                ),
                ("profile", "profile", str, "canonical", False, None, False),
                ("publisher", "publisher", str, "string", False, None, False),
                ("purpose", "purpose", str, "markdown", False, None, False),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    False,
                ),
                (
                    "relatedArtifact",
                    "relatedArtifact",
                    relatedartifact.RelatedArtifact,
                    "RelatedArtifact",
                    True,
                    None,
                    False,
                ),
                (
                    "reviewer",
                    "reviewer",
                    contactdetail.ContactDetail,
                    "ContactDetail",
                    True,
                    None,
                    False,
                ),
                (
                    "specimenRequirement",
                    "specimenRequirement",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "subjectCodeableConcept",
                    "subjectCodeableConcept",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    "subject",
                    False,
                ),
                (
                    "subjectReference",
                    "subjectReference",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    "subject",
                    False,
                ),
                ("subtitle", "subtitle", str, "string", False, None, False),
                ("timingAge", "timingAge", age.Age, "Age", False, "timing", False),
                (
                    "timingDateTime",
                    "timingDateTime",
                    fhirdate.FHIRDate,
                    "dateTime",
                    False,
                    "timing",
                    False,
                ),
                (
                    "timingDuration",
                    "timingDuration",
                    duration.Duration,
                    "Duration",
                    False,
                    "timing",
                    False,
                ),
                (
                    "timingPeriod",
                    "timingPeriod",
                    period.Period,
                    "Period",
                    False,
                    "timing",
                    False,
                ),
                (
                    "timingRange",
                    "timingRange",
                    range.Range,
                    "Range",
                    False,
                    "timing",
                    False,
                ),
                (
                    "timingTiming",
                    "timingTiming",
                    timing.Timing,
                    "Timing",
                    False,
                    "timing",
                    False,
                ),
                ("title", "title", str, "string", False, None, False),
                (
                    "topic",
                    "topic",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                ("transform", "transform", str, "canonical", False, None, False),
                ("url", "url", str, "uri", False, None, False),
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
                ("version", "version", str, "string", False, None, False),
            ]
        )
        return js


class ActivityDefinitionDynamicValue(backboneelement.BackboneElement):
    """ Dynamic aspects of the definition.

    Dynamic values that will be evaluated to produce values for elements of the
    resulting resource. For example, if the dosage of a medication must be
    computed based on the patient's weight, a dynamic value would be used to
    specify an expression that calculated the weight, and the path on the
    request resource that would contain the result.
    """

    resource_type = "ActivityDefinitionDynamicValue"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.expression = None
        """ An expression that provides the dynamic value for the customization.
        Type `Expression` (represented as `dict` in JSON). """

        self.path = None
        """ The path to the element to be set dynamically.
        Type `str`. """

        super(ActivityDefinitionDynamicValue, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ActivityDefinitionDynamicValue, self).elementProperties()
        js.extend(
            [
                (
                    "expression",
                    "expression",
                    expression.Expression,
                    "Expression",
                    False,
                    None,
                    True,
                ),
                ("path", "path", str, "string", False, None, True),
            ]
        )
        return js


class ActivityDefinitionParticipant(backboneelement.BackboneElement):
    """ Who should participate in the action.

    Indicates who should participate in performing the action described.
    """

    resource_type = "ActivityDefinitionParticipant"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.role = None
        """ E.g. Nurse, Surgeon, Parent, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.type = None
        """ patient | practitioner | related-person | device.
        Type `str`. """

        super(ActivityDefinitionParticipant, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(ActivityDefinitionParticipant, self).elementProperties()
        js.extend(
            [
                (
                    "role",
                    "role",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                ("type", "type", str, "code", False, None, True),
            ]
        )
        return js


try:
    from . import age
except ImportError:
    age = sys.modules[__package__ + ".age"]
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + ".codeableconcept"]
try:
    from . import contactdetail
except ImportError:
    contactdetail = sys.modules[__package__ + ".contactdetail"]
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + ".dosage"]
try:
    from . import duration
except ImportError:
    duration = sys.modules[__package__ + ".duration"]
try:
    from . import expression
except ImportError:
    expression = sys.modules[__package__ + ".expression"]
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
    from . import period
except ImportError:
    period = sys.modules[__package__ + ".period"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
try:
    from . import range
except ImportError:
    range = sys.modules[__package__ + ".range"]
try:
    from . import relatedartifact
except ImportError:
    relatedartifact = sys.modules[__package__ + ".relatedartifact"]
try:
    from . import timing
except ImportError:
    timing = sys.modules[__package__ + ".timing"]
try:
    from . import usagecontext
except ImportError:
    usagecontext = sys.modules[__package__ + ".usagecontext"]
