# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/MedicinalProductPackaged
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""


import sys

from . import backboneelement, domainresource


class MedicinalProductPackaged(domainresource.DomainResource):
    """ A medicinal product in a container or package.
    """

    resource_type = "MedicinalProductPackaged"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.batchIdentifier = None
        """ Batch numbering.
        List of `MedicinalProductPackagedBatchIdentifier` items (represented as `dict` in JSON). """

        self.description = None
        """ Textual description.
        Type `str`. """

        self.identifier = None
        """ Unique identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.legalStatusOfSupply = None
        """ The legal status of supply of the medicinal product as classified
        by the regulator.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of this Package Item.
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        self.marketingAuthorization = None
        """ Manufacturer of this Package Item.
        Type `FHIRReference` referencing `['MedicinalProductAuthorization']` (represented as `dict` in JSON). """

        self.marketingStatus = None
        """ Marketing information.
        List of `MarketingStatus` items (represented as `dict` in JSON). """

        self.packageItem = None
        """ A packaging item, as a contained for medicine, possibly with other
        packaging items within.
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """

        self.subject = None
        """ The product with this is a pack for.
        List of `FHIRReference` items referencing `['MedicinalProduct']` (represented as `dict` in JSON). """

        super(MedicinalProductPackaged, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicinalProductPackaged, self).elementProperties()
        js.extend(
            [
                (
                    "batchIdentifier",
                    "batchIdentifier",
                    MedicinalProductPackagedBatchIdentifier,
                    "MedicinalProductPackagedBatchIdentifier",
                    True,
                    None,
                    False,
                ),
                ("description", "description", str, "string", False, None, False),
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
                    "legalStatusOfSupply",
                    "legalStatusOfSupply",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    False,
                    None,
                    False,
                ),
                (
                    "manufacturer",
                    "manufacturer",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "marketingAuthorization",
                    "marketingAuthorization",
                    fhirreference.FHIRReference,
                    "Reference",
                    False,
                    None,
                    False,
                ),
                (
                    "marketingStatus",
                    "marketingStatus",
                    marketingstatus.MarketingStatus,
                    "MarketingStatus",
                    True,
                    None,
                    False,
                ),
                (
                    "packageItem",
                    "packageItem",
                    MedicinalProductPackagedPackageItem,
                    "MedicinalProductPackagedPackageItem",
                    True,
                    None,
                    True,
                ),
                (
                    "subject",
                    "subject",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
            ]
        )
        return js


class MedicinalProductPackagedBatchIdentifier(backboneelement.BackboneElement):
    """ Batch numbering.
    """

    resource_type = "MedicinalProductPackagedBatchIdentifier"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.immediatePackaging = None
        """ A number appearing on the immediate packaging (and not the outer
        packaging).
        Type `Identifier` (represented as `dict` in JSON). """

        self.outerPackaging = None
        """ A number appearing on the outer packaging of a specific batch.
        Type `Identifier` (represented as `dict` in JSON). """

        super(MedicinalProductPackagedBatchIdentifier, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductPackagedBatchIdentifier, self).elementProperties()
        js.extend(
            [
                (
                    "immediatePackaging",
                    "immediatePackaging",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    False,
                ),
                (
                    "outerPackaging",
                    "outerPackaging",
                    identifier.Identifier,
                    "Identifier",
                    False,
                    None,
                    True,
                ),
            ]
        )
        return js


class MedicinalProductPackagedPackageItem(backboneelement.BackboneElement):
    """ A packaging item, as a contained for medicine, possibly with other
    packaging items within.
    """

    resource_type = "MedicinalProductPackagedPackageItem"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.alternateMaterial = None
        """ A possible alternate material for the packaging.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.device = None
        """ A device accompanying a medicinal product.
        List of `FHIRReference` items referencing `['DeviceDefinition']` (represented as `dict` in JSON). """

        self.identifier = None
        """ Including possibly Data Carrier Identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.manufacturedItem = None
        """ The manufactured item as contained in the packaged medicinal
        product.
        List of `FHIRReference` items referencing `['MedicinalProductManufactured']` (represented as `dict` in JSON). """

        self.manufacturer = None
        """ Manufacturer of this Package Item.
        List of `FHIRReference` items referencing `['Organization']` (represented as `dict` in JSON). """

        self.material = None
        """ Material type of the package item.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.otherCharacteristics = None
        """ Other codeable characteristics.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.packageItem = None
        """ Allows containers within containers.
        List of `MedicinalProductPackagedPackageItem` items (represented as `dict` in JSON). """

        self.physicalCharacteristics = None
        """ Dimensions, color etc..
        Type `ProdCharacteristic` (represented as `dict` in JSON). """

        self.quantity = None
        """ The quantity of this package in the medicinal product, at the
        current level of packaging. The outermost is always 1.
        Type `Quantity` (represented as `dict` in JSON). """

        self.shelfLifeStorage = None
        """ Shelf Life and storage information.
        List of `ProductShelfLife` items (represented as `dict` in JSON). """

        self.type = None
        """ The physical type of the container of the medicine.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicinalProductPackagedPackageItem, self).__init__(
            jsondict=jsondict, strict=strict
        )

    def elementProperties(self):
        js = super(MedicinalProductPackagedPackageItem, self).elementProperties()
        js.extend(
            [
                (
                    "alternateMaterial",
                    "alternateMaterial",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "device",
                    "device",
                    fhirreference.FHIRReference,
                    "Reference",
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
                    "manufacturedItem",
                    "manufacturedItem",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "manufacturer",
                    "manufacturer",
                    fhirreference.FHIRReference,
                    "Reference",
                    True,
                    None,
                    False,
                ),
                (
                    "material",
                    "material",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "otherCharacteristics",
                    "otherCharacteristics",
                    codeableconcept.CodeableConcept,
                    "CodeableConcept",
                    True,
                    None,
                    False,
                ),
                (
                    "packageItem",
                    "packageItem",
                    MedicinalProductPackagedPackageItem,
                    "MedicinalProductPackagedPackageItem",
                    True,
                    None,
                    False,
                ),
                (
                    "physicalCharacteristics",
                    "physicalCharacteristics",
                    prodcharacteristic.ProdCharacteristic,
                    "ProdCharacteristic",
                    False,
                    None,
                    False,
                ),
                (
                    "quantity",
                    "quantity",
                    quantity.Quantity,
                    "Quantity",
                    False,
                    None,
                    True,
                ),
                (
                    "shelfLifeStorage",
                    "shelfLifeStorage",
                    productshelflife.ProductShelfLife,
                    "ProductShelfLife",
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
                    True,
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
    from . import marketingstatus
except ImportError:
    marketingstatus = sys.modules[__package__ + ".marketingstatus"]
try:
    from . import prodcharacteristic
except ImportError:
    prodcharacteristic = sys.modules[__package__ + ".prodcharacteristic"]
try:
    from . import productshelflife
except ImportError:
    productshelflife = sys.modules[__package__ + ".productshelflife"]
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + ".quantity"]
