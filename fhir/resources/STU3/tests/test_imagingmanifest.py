# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/ImagingManifest
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import imagingmanifest
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class ImagingManifestTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("ImagingManifest", js["resourceType"])
        return imagingmanifest.ImagingManifest(js)

    def testImagingManifest1(self):
        inst = self.instantiate_from("imagingmanifest-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a ImagingManifest instance")
        self.implImagingManifest1(inst)

        js = inst.as_json()
        self.assertEqual("ImagingManifest", js["resourceType"])
        inst2 = imagingmanifest.ImagingManifest(js)
        self.implImagingManifest1(inst2)

    def implImagingManifest1(self, inst):
        self.assertEqual(
            inst.authoringTime.date, FHIRDate("2014-11-20T11:01:20-08:00").date
        )
        self.assertEqual(inst.authoringTime.as_json(), "2014-11-20T11:01:20-08:00")
        self.assertEqual(
            force_bytes(inst.description),
            force_bytes(
                "1 SC image (screen snapshot) and 2 CT images to share a chest CT exam"
            ),
        )
        self.assertEqual(force_bytes(inst.id), force_bytes("example"))
        self.assertEqual(
            force_bytes(inst.identifier.value),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092901"
            ),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[0].instance[0].sopClass),
            force_bytes("urn:oid:1.2.840.10008.5.1.4.1.1.7"),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[0].instance[0].uid),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092902"
            ),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[0].uid),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092901"
            ),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[1].instance[0].sopClass),
            force_bytes("urn:oid:1.2.840.10008.5.1.4.1.1.2"),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[1].instance[0].uid),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092903"
            ),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[1].instance[1].sopClass),
            force_bytes("urn:oid:1.2.840.10008.5.1.4.1.1.2"),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[1].instance[1].uid),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16748.2599092904"
            ),
        )
        self.assertEqual(
            force_bytes(inst.study[0].series[1].uid),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16750.2599092902"
            ),
        )
        self.assertEqual(
            force_bytes(inst.study[0].uid),
            force_bytes(
                "urn:oid:2.16.124.113543.6003.189642796.63084.16749.2599092904"
            ),
        )
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">A set of images to share accompanying an report document, including one SC image and two CT image</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
