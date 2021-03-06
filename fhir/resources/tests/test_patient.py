# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Patient
Release: R4
Version: 4.0.1
Build ID: 9346c8cc45
Last updated: 2019-11-01T09:29:23.356+11:00
"""

import io
import json
import os
import unittest

import pytest

from .. import patient
from ..fhirdate import FHIRDate
from .fixtures import force_bytes


@pytest.mark.usefixtures("base_settings")
class PatientTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("Patient", js["resourceType"])
        return patient.Patient(js)

    def testPatient1(self):
        inst = self.instantiate_from("patient-example-xds.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient1(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient1(inst2)

    def implPatient1(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Metropolis"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("USA"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("100 Main St")
        )
        self.assertEqual(force_bytes(inst.address[0].postalCode), force_bytes("44130"))
        self.assertEqual(force_bytes(inst.address[0].state), force_bytes("Il"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1956-05-27").date)
        self.assertEqual(inst.birthDate.as_json(), "1956-05-27")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("xds"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system), force_bytes("urn:oid:1.2.3.4.5")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("89765a87b")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Doe"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("John"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient2(self):
        inst = self.instantiate_from("patient-example-f001-pieter.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient2(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient2(inst2)

    def implPatient2(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.address[0].city), force_bytes("Amsterdam"))
        self.assertEqual(force_bytes(inst.address[0].country), force_bytes("NLD"))
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("Van Egmondkade 23")
        )
        self.assertEqual(
            force_bytes(inst.address[0].postalCode), force_bytes("1024 RJ")
        )
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1944-11-17").date)
        self.assertEqual(inst.birthDate.as_json(), "1944-11-17")
        self.assertEqual(
            force_bytes(inst.communication[0].language.coding[0].code),
            force_bytes("nl"),
        )
        self.assertEqual(
            force_bytes(inst.communication[0].language.coding[0].display),
            force_bytes("Dutch"),
        )
        self.assertEqual(
            force_bytes(inst.communication[0].language.coding[0].system),
            force_bytes("urn:ietf:bcp:47"),
        )
        self.assertEqual(
            force_bytes(inst.communication[0].language.text), force_bytes("Nederlands")
        )
        self.assertTrue(inst.communication[0].preferred)
        self.assertEqual(force_bytes(inst.contact[0].name.family), force_bytes("Abels"))
        self.assertEqual(
            force_bytes(inst.contact[0].name.given[0]), force_bytes("Sarah")
        )
        self.assertEqual(force_bytes(inst.contact[0].name.use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].code),
            force_bytes("C"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0131"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("mobile")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("0690383372")
        )
        self.assertFalse(inst.deceasedBoolean)
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f001"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("738472983")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("urn:oid:2.16.840.1.113883.2.4.6.3"),
        )
        self.assertEqual(force_bytes(inst.identifier[1].use), force_bytes("usual"))
        self.assertEqual(
            force_bytes(inst.maritalStatus.coding[0].code), force_bytes("M")
        )
        self.assertEqual(
            force_bytes(inst.maritalStatus.coding[0].display), force_bytes("Married")
        )
        self.assertEqual(
            force_bytes(inst.maritalStatus.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"),
        )
        self.assertEqual(force_bytes(inst.maritalStatus.text), force_bytes("Getrouwd"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertTrue(inst.multipleBirthBoolean)
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("van de Heuvel"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Pieter"))
        self.assertEqual(force_bytes(inst.name[0].suffix[0]), force_bytes("MSc"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("mobile"))
        self.assertEqual(force_bytes(inst.telecom[0].value), force_bytes("0648352638"))
        self.assertEqual(force_bytes(inst.telecom[1].system), force_bytes("email"))
        self.assertEqual(force_bytes(inst.telecom[1].use), force_bytes("home"))
        self.assertEqual(
            force_bytes(inst.telecom[1].value), force_bytes("p.heuvel@gmail.com")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient3(self):
        inst = self.instantiate_from("patient-example-d.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient3(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient3(inst2)

    def implPatient3(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1982-08-02").date)
        self.assertEqual(inst.birthDate.as_json(), "1982-08-02")
        self.assertTrue(inst.deceasedBoolean)
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("pat4"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:0.1.2.3.4.5.6.7"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123458"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Notsowell"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Sandy"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient4(self):
        inst = self.instantiate_from("patient-example-infant-twin-1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient4(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient4(inst2)

    def implPatient4(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("2017-05-15").date)
        self.assertEqual(inst.birthDate.as_json(), "2017-05-15")
        self.assertEqual(
            force_bytes(inst.contact[0].name.family), force_bytes("Organa")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].name.given[0]), force_bytes("Leia")
        )
        self.assertEqual(force_bytes(inst.contact[0].name.use), force_bytes("maiden"))
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].code),
            force_bytes("72705000"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].display),
            force_bytes("Mother"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[1].code),
            force_bytes("N"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[1].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0131"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[2].code),
            force_bytes("MTH"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[2].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-RoleCode"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("mobile")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("+31201234567")
        )
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Organa")
        )
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("infant-twin-1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://coruscanthealth.org/main-hospital/patient-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("MRN7465737865")
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].system),
            force_bytes("http://new-republic.gov/galactic-citizen-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[1].value), force_bytes("7465737865")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.multipleBirthInteger, 1)
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Solo"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Jaina"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient5(self):
        inst = self.instantiate_from("patient-example-infant-mom.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient5(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient5(inst2)

    def implPatient5(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("1995-10-12").date)
        self.assertEqual(inst.birthDate.as_json(), "1995-10-12")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("infant-mom"))
        self.assertEqual(
            force_bytes(inst.maritalStatus.coding[0].code), force_bytes("M")
        )
        self.assertEqual(
            force_bytes(inst.maritalStatus.coding[0].display), force_bytes("Married")
        )
        self.assertEqual(
            force_bytes(inst.maritalStatus.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"),
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Solo"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Leia"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.name[1].family), force_bytes("Organa"))
        self.assertEqual(force_bytes(inst.name[1].given[0]), force_bytes("Leia"))
        self.assertEqual(force_bytes(inst.name[1].use), force_bytes("maiden"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient6(self):
        inst = self.instantiate_from("patient-example-newborn.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient6(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient6(inst2)

    def implPatient6(self, inst):
        self.assertEqual(inst.birthDate.date, FHIRDate("2017-09-05").date)
        self.assertEqual(inst.birthDate.as_json(), "2017-09-05")
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Everywoman")
        )
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("newborn"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(inst.multipleBirthInteger, 2)
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient7(self):
        inst = self.instantiate_from("patient-example-infant-fetal.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient7(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient7(inst2)

    def implPatient7(self, inst):
        self.assertEqual(
            force_bytes(inst.contact[0].name.family), force_bytes("Organa")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].name.given[0]), force_bytes("Leia")
        )
        self.assertEqual(force_bytes(inst.contact[0].name.use), force_bytes("maiden"))
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].code),
            force_bytes("72705000"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].display),
            force_bytes("Mother"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[0].system),
            force_bytes("http://snomed.info/sct"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[1].code),
            force_bytes("N"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[1].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0131"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[2].code),
            force_bytes("MTH"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].relationship[0].coding[2].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-RoleCode"),
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].system), force_bytes("phone")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].use), force_bytes("mobile")
        )
        self.assertEqual(
            force_bytes(inst.contact[0].telecom[0].value), force_bytes("+31201234567")
        )
        self.assertEqual(
            force_bytes(inst.extension[0].url),
            force_bytes(
                "http://hl7.org/fhir/StructureDefinition/patient-mothersMaidenName"
            ),
        )
        self.assertEqual(
            force_bytes(inst.extension[0].valueString), force_bytes("Organa")
        )
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("infant-fetal"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://coruscanthealth.org/main-hospital/patient-identifier"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("MRN657865757378")
        )
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient8(self):
        inst = self.instantiate_from("patient-genetics-example1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient8(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient8(inst2)

    def implPatient8(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(
            force_bytes(inst.address[0].line[0]), force_bytes("2222 Home Street")
        )
        self.assertEqual(force_bytes(inst.address[0].use), force_bytes("home"))
        self.assertEqual(inst.birthDate.date, FHIRDate("1973-05-31").date)
        self.assertEqual(inst.birthDate.as_json(), "1973-05-31")
        self.assertEqual(force_bytes(inst.gender), force_bytes("female"))
        self.assertEqual(force_bytes(inst.id), force_bytes("genetics-example1"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("http://hl7.org/fhir/sid/us-ssn"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("SS")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].value), force_bytes("444222222")
        )
        self.assertEqual(
            inst.meta.lastUpdated.date, FHIRDate("2012-05-29T23:45:32Z").date
        )
        self.assertEqual(inst.meta.lastUpdated.as_json(), "2012-05-29T23:45:32Z")
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Everywoman"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Eve"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.telecom[0].system), force_bytes("phone"))
        self.assertEqual(force_bytes(inst.telecom[0].use), force_bytes("work"))
        self.assertEqual(
            force_bytes(inst.telecom[0].value), force_bytes("555-555-2003")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient9(self):
        inst = self.instantiate_from("patient-example-b.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient9(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient9(inst2)

    def implPatient9(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(force_bytes(inst.gender), force_bytes("other"))
        self.assertEqual(force_bytes(inst.id), force_bytes("pat2"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:0.1.2.3.4.5.6.7"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123456"))
        self.assertEqual(force_bytes(inst.link[0].type), force_bytes("seealso"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Donald"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Duck"))
        self.assertEqual(force_bytes(inst.name[0].given[1]), force_bytes("D"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(
            force_bytes(inst.photo[0].contentType), force_bytes("image/gif")
        )
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

    def testPatient10(self):
        inst = self.instantiate_from("patient-example-c.json")
        self.assertIsNotNone(inst, "Must have instantiated a Patient instance")
        self.implPatient10(inst)

        js = inst.as_json()
        self.assertEqual("Patient", js["resourceType"])
        inst2 = patient.Patient(js)
        self.implPatient10(inst2)

    def implPatient10(self, inst):
        self.assertTrue(inst.active)
        self.assertEqual(inst.birthDate.date, FHIRDate("1982-01-23").date)
        self.assertEqual(inst.birthDate.as_json(), "1982-01-23")
        self.assertEqual(
            inst.deceasedDateTime.date, FHIRDate("2015-02-14T13:42:00+10:00").date
        )
        self.assertEqual(inst.deceasedDateTime.as_json(), "2015-02-14T13:42:00+10:00")
        self.assertEqual(force_bytes(inst.gender), force_bytes("male"))
        self.assertEqual(force_bytes(inst.id), force_bytes("pat3"))
        self.assertEqual(
            force_bytes(inst.identifier[0].system),
            force_bytes("urn:oid:0.1.2.3.4.5.6.7"),
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].code), force_bytes("MR")
        )
        self.assertEqual(
            force_bytes(inst.identifier[0].type.coding[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v2-0203"),
        )
        self.assertEqual(force_bytes(inst.identifier[0].use), force_bytes("usual"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("123457"))
        self.assertEqual(force_bytes(inst.meta.tag[0].code), force_bytes("HTEST"))
        self.assertEqual(
            force_bytes(inst.meta.tag[0].display), force_bytes("test health data")
        )
        self.assertEqual(
            force_bytes(inst.meta.tag[0].system),
            force_bytes("http://terminology.hl7.org/CodeSystem/v3-ActReason"),
        )
        self.assertEqual(force_bytes(inst.name[0].family), force_bytes("Notsowell"))
        self.assertEqual(force_bytes(inst.name[0].given[0]), force_bytes("Simon"))
        self.assertEqual(force_bytes(inst.name[0].use), force_bytes("official"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
