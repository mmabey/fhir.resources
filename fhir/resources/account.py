# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Account
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class Account(domainresource.DomainResource):
    """ Tracks balance, charges, for patient or cost center.

    A financial tool for tracking value accrued for a particular purpose.  In
    the healthcare field, used to track charges for a patient, cost centers,
    etc.
    """

    resource_type = "Account"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.coverage = None
        """ The party(s) that are responsible for covering the payment of this
        account, and what order should they be applied to the account.
        List of `AccountCoverage` items (represented as `dict` in JSON). """

        self.description = None
        """ Explanation of purpose/use.
        Type `str`. """

        self.guarantor = None
        """ The parties ultimately responsible for balancing the Account.
        List of `AccountGuarantor` items (represented as `dict` in JSON). """

        self.identifier = None
        """ Account number.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.name = None
        """ Human-readable label.
        Type `str`. """

        self.owner = None
        """ Entity managing the Account.
        Type `FHIRReference` referencing `['Organization']` (represented as `dict` in JSON). """

        self.partOf = None
        """ Reference to a parent Account.
        Type `FHIRReference` referencing `['Account']` (represented as `dict` in JSON). """

        self.servicePeriod = None
        """ Transaction window.
        Type `Period` (represented as `dict` in JSON). """

        self.status = None
        """ active | inactive | entered-in-error | on-hold | unknown.
        Type `str`. """

        self.subject = None
        """ The entity that caused the expenses.
        List of `FHIRReference` items referencing `['Patient', 'Device', 'Practitioner', 'PractitionerRole', 'Location', 'HealthcareService', 'Organization']` (represented as `dict` in JSON). """

        self.type = None
        """ E.g. patient, expense, depreciation.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(Account, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(Account, self).elementProperties()
        js.extend(
            [
                (
                    "coverage",
                    "coverage",
                    AccountCoverage,
                    "AccountCoverage",
                    True,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
                (
                    "guarantor",
                    "guarantor",
                    AccountGuarantor,
                    "AccountGuarantor",
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
                ("name", "name", str, "string", False, None, False),
                (
                    "owner",
                    "owner",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "servicePeriod",
                    "servicePeriod",
                    period.Period,
                    "Period",
                    False,
                    None,
                    False,
                ),
                ("status", "status", str, "code", False, None, True),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
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


class AccountCoverage(backboneelement.BackboneElement):
    """ The party(s) that are responsible for covering the payment of this account,
    and what order should they be applied to the account.
    """

    resource_type = "AccountCoverage"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.coverage = None
        """ The party(s), such as insurances, that may contribute to the
        payment of this account.
        Type `FHIRReference` referencing `['Coverage']` (represented as `dict` in JSON). """

        self.priority = None
        """ The priority of the coverage in the context of this account.
        Type `int`. """

        super(AccountCoverage, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AccountCoverage, self).elementProperties()
        js.extend(
            [
                (
                    "coverage",
                    "coverage",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("priority", "priority", int, "positiveInt", False, None, False),
            ]
        )
        return js


class AccountGuarantor(backboneelement.BackboneElement):
    """ The parties ultimately responsible for balancing the Account.

    The parties responsible for balancing the account if other payment options
    fall short.
    """

    resource_type = "AccountGuarantor"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.onHold = None
        """ Credit or other hold applied.
        Type `bool`. """

        self.party = None
        """ Responsible entity.
        Type `FHIRReference` referencing `['Patient', 'RelatedPerson', 'Organization']` (represented as `dict` in JSON). """

        self.period = None
        """ Guarantee account during.
        Type `Period` (represented as `dict` in JSON). """

        super(AccountGuarantor, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(AccountGuarantor, self).elementProperties()
        js.extend(
            [
                ("onHold", "onHold", bool, "boolean", False, None, False),
                (
                    "party",
                    "party",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    True,
                ),
                ("period", "period", period.Period, "Period", False, None, False),
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
