# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/FamilyMemberHistory
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

from .. import familymemberhistory
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class FamilyMemberHistoryTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("FamilyMemberHistory", js["resourceType"])
        return familymemberhistory.FamilyMemberHistory(js)

    def testFamilyMemberHistory1(self):
        inst = self.instantiate_from("familymemberhistory-example.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a FamilyMemberHistory instance"
        )
        self.implFamilyMemberHistory1(inst)

        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory1(inst2)

    def implFamilyMemberHistory1(self, inst):
        self.assertEqual(
            force_bytes(inst.condition[0].code.coding[0].code), force_bytes("315619001")
        )
        self.assertEqual(
            force_bytes(inst.condition[0].code.coding[0].display),
            force_bytes("Myocardial Infarction"),
        )
        self.assertEqual(
            force_bytes(inst.condition[0].code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.condition[0].code.text), force_bytes("Heart Attack")
        )
        self.assertEqual(
            force_bytes(inst.condition[0].note[0].text),
            force_bytes(
                "Was fishing at the time. At least he went doing someting he loved."
            ),
        )
        self.assertEqual(force_bytes(inst.condition[0].onsetAge.code), force_bytes("a"))
        self.assertEqual(
            force_bytes(inst.condition[0].onsetAge.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.condition[0].onsetAge.unit), force_bytes("yr")
        )
        self.assertEqual(inst.condition[0].onsetAge.value, 74)
        self.assertEqual(inst.date.date, FHIRDate("2011-03-18").date)
        self.assertEqual(inst.date.as_json(), "2011-03-18")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("father"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("12345"))
        self.assertFalse(inst.notDone)
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].code), force_bytes("FTH")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].display), force_bytes("father")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RoleCode"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Father died of a heart attack aged 74</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testFamilyMemberHistory2(self):
        inst = self.instantiate_from("familymemberhistory-example-mother.json")
        self.assertIsNotNone(
            inst, "Must have instantiated a FamilyMemberHistory instance"
        )
        self.implFamilyMemberHistory2(inst)

        js = inst.as_json()
        self.assertEqual("FamilyMemberHistory", js["resourceType"])
        inst2 = familymemberhistory.FamilyMemberHistory(js)
        self.implFamilyMemberHistory2(inst2)

    def implFamilyMemberHistory2(self, inst):
        self.assertEqual(
            force_bytes(inst.condition[0].code.coding[0].code), force_bytes("371041009")
        )
        self.assertEqual(
            force_bytes(inst.condition[0].code.coding[0].display),
            force_bytes("Embolic Stroke"),
        )
        self.assertEqual(
            force_bytes(inst.condition[0].code.coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.condition[0].code.text), force_bytes("Stroke")
        )
        self.assertEqual(force_bytes(inst.condition[0].onsetAge.code), force_bytes("a"))
        self.assertEqual(
            force_bytes(inst.condition[0].onsetAge.system),
            force_bytes("http://unitsofmeasure.org"),
        )
        self.assertEqual(
            force_bytes(inst.condition[0].onsetAge.unit), force_bytes("yr")
        )
        self.assertEqual(inst.condition[0].onsetAge.value, 56)
        self.assertEqual(force_bytes(inst.id), force_bytes("mother"))
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].code), force_bytes("MTH")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].display), force_bytes("mother")
        )
        self.assertEqual(
            force_bytes(inst.relationship.coding[0].system),
            force_bytes("http://hl7.org/fhir/v3/RoleCode"),
        )
        self.assertEqual(force_bytes(inst.status), force_bytes("completed"))
        self.assertEqual(
            force_bytes(inst.text.div),
            force_bytes(
                '<div xmlns="http://www.w3.org/1999/xhtml">Mother died of a stroke aged 56</div>'
            ),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
