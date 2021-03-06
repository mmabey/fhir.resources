#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 1.0.2.7202 on 2019-05-14.
#  2019, SMART Health IT.


import io
import json
import os
import unittest

from . import nutritionorder
from .fhirdate import FHIRDate


class NutritionOrderTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get("FHIR_UNITTEST_DATADIR") or ""
        with io.open(os.path.join(datadir, filename), "r", encoding="utf-8") as handle:
            js = json.load(handle)
            self.assertEqual("NutritionOrder", js["resourceType"])
        return nutritionorder.NutritionOrder(js)

    def testNutritionOrder1(self):
        inst = self.instantiate_from("nutritionorder-example-enteralbolus.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder1(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder1(inst2)

    def implNutritionOrder1(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.enteralFormula.additiveProductName, "Acme Lipid Additive")
        self.assertEqual(inst.enteralFormula.additiveType.coding[0].code, "lipid")
        self.assertEqual(
            inst.enteralFormula.additiveType.coding[0].display,
            "Modular lipid enteral formula component",
        )
        self.assertEqual(
            inst.enteralFormula.additiveType.coding[0].system,
            "http://hl7.org/fhir/entformula-additive",
        )
        self.assertEqual(
            inst.enteralFormula.administrationInstruction, "240 mls every 4hrs "
        )
        self.assertEqual(inst.enteralFormula.administration[0].quantity.code, "mL")
        self.assertEqual(
            inst.enteralFormula.administration[0].quantity.system,
            "http://unitsofmeasure.org",
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].quantity.unit, "milliliters"
        )
        self.assertEqual(inst.enteralFormula.administration[0].quantity.value, 240)
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17T16:00:00Z").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17T16:00:00Z",
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.frequency, 1
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.period, 4
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.periodUnits, "h"
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaProductName, "Acme High Protein Formula"
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaType.coding[0].code, "659311000124118"
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaType.coding[0].display,
            "Adult high protein formula",
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaType.coding[0].system,
            "http://usextension/snomed.info/sct",
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.code, "cal/mL")
        self.assertEqual(
            inst.enteralFormula.caloricDensity.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(
            inst.enteralFormula.caloricDensity.unit, "calories per milliliter"
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.value, 1.5)
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.code, "mL/d")
        self.assertEqual(
            inst.enteralFormula.maxVolumeToDeliver.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.unit, "milliliter/day")
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.value, 1440)
        self.assertEqual(inst.enteralFormula.routeofAdministration.coding[0].code, "GT")
        self.assertEqual(
            inst.enteralFormula.routeofAdministration.coding[0].display,
            "Instillation, gastrostomy tube",
        )
        self.assertEqual(
            inst.enteralFormula.routeofAdministration.coding[0].system,
            "http://hl7.org/fhir/v3/RouteOfAdministration",
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].code, "227493005")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].display, "Cashew Nut")
        self.assertEqual(
            inst.excludeFoodModifier[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].version, "20140730")
        self.assertEqual(inst.foodPreferenceModifier[0].coding[0].code, "dairy-free")
        self.assertEqual(
            inst.foodPreferenceModifier[0].coding[0].system, "http://hl7.org/fhir/diet"
        )
        self.assertEqual(inst.id, "enteralbolus")
        self.assertEqual(
            inst.identifier[0].system, "http://www.acme.org/nutritionorders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder2(self):
        inst = self.instantiate_from("nutritionorder-example-texture-modified.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder2(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder2(inst2)

    def implNutritionOrder2(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.id, "texturemodified")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.oralDiet.texture[0].foodType.coding[0].code, "28647000")
        self.assertEqual(inst.oralDiet.texture[0].foodType.coding[0].display, "Meat")
        self.assertEqual(
            inst.oralDiet.texture[0].foodType.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(
            inst.oralDiet.texture[0].foodType.text, "Regular, Chopped Meat"
        )
        self.assertEqual(inst.oralDiet.texture[0].modifier.coding[0].code, "228049004")
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.coding[0].display, "Chopped food"
        )
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.text, "Regular, Chopped Meat"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[0].code, "435801000124108")
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].display, "Texture modified diet"
        )
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[1].code, "1010")
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].display, "Texture modified diet"
        )
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[0].text, "Texture modified diet")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder3(self):
        inst = self.instantiate_from("nutritionorder-example-fiberrestricteddiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder3(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder3(inst2)

    def implNutritionOrder3(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].code, "227493005")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].display, "Cashew Nut")
        self.assertEqual(
            inst.excludeFoodModifier[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].version, "20140730")
        self.assertEqual(inst.foodPreferenceModifier[0].coding[0].code, "dairy-free")
        self.assertEqual(
            inst.foodPreferenceModifier[0].coding[0].system, "http://hl7.org/fhir/diet"
        )
        self.assertEqual(inst.id, "fiberrestricteddiet")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.oralDiet.nutrient[0].amount.code, "g")
        self.assertEqual(
            inst.oralDiet.nutrient[0].amount.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.oralDiet.nutrient[0].amount.unit, "grams")
        self.assertEqual(inst.oralDiet.nutrient[0].amount.value, 50)
        self.assertEqual(inst.oralDiet.nutrient[0].modifier.coding[0].code, "256674009")
        self.assertEqual(inst.oralDiet.nutrient[0].modifier.coding[0].display, "Fat")
        self.assertEqual(
            inst.oralDiet.nutrient[0].modifier.coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.oralDiet.type[0].coding[0].code, "15108003")
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].display, "Restricted fiber diet"
        )
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[1].code, "1000")
        self.assertEqual(inst.oralDiet.type[0].coding[1].display, "Fiber restricted")
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[0].text, "Fiber restricted diet")
        self.assertEqual(inst.oralDiet.type[1].coding[0].code, "16208003")
        self.assertEqual(inst.oralDiet.type[1].coding[0].display, "Low fat diet")
        self.assertEqual(
            inst.oralDiet.type[1].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[1].coding[1].code, "1100")
        self.assertEqual(inst.oralDiet.type[1].coding[1].display, "Low Fat")
        self.assertEqual(
            inst.oralDiet.type[1].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[1].text, "Low fat diet")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder4(self):
        inst = self.instantiate_from("nutritionorder-example-energysupplement.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder4(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder4(inst2)

    def implNutritionOrder4(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].code, "227493005")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].display, "Cashew Nut")
        self.assertEqual(
            inst.excludeFoodModifier[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].version, "20140730")
        self.assertEqual(inst.foodPreferenceModifier[0].coding[0].code, "kosher")
        self.assertEqual(
            inst.foodPreferenceModifier[0].coding[0].system, "http://hl7.org/fhir/diet"
        )
        self.assertEqual(inst.id, "energysupplement")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.supplement[0].productName, "Ensure")
        self.assertEqual(inst.supplement[0].quantity.unit, "8 oz can")
        self.assertEqual(inst.supplement[0].quantity.value, 1)
        self.assertEqual(
            inst.supplement[0].schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.supplement[0].schedule[0].repeat.boundsPeriod.start.as_json(),
            "2015-02-10",
        )
        self.assertEqual(inst.supplement[0].schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.supplement[0].schedule[0].repeat.period, 1)
        self.assertEqual(inst.supplement[0].schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.supplement[0].type.coding[0].code, "442971000124100")
        self.assertEqual(
            inst.supplement[0].type.coding[0].display, "Adult high energy formula"
        )
        self.assertEqual(
            inst.supplement[0].type.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.supplement[0].type.coding[1].code, "1010")
        self.assertEqual(
            inst.supplement[0].type.coding[1].display, "Adult high energy drink"
        )
        self.assertEqual(
            inst.supplement[0].type.coding[1].system,
            "http://goodhealthhospital.org/supplement-type-codes",
        )
        self.assertEqual(inst.supplement[0].type.text, "Adult high energy drink")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder5(self):
        inst = self.instantiate_from("nutritionorder-example-renaldiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder5(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder5(inst2)

    def implNutritionOrder5(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].code, "227493005")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].display, "Cashew Nut")
        self.assertEqual(
            inst.excludeFoodModifier[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].version, "20140730")
        self.assertEqual(inst.foodPreferenceModifier[0].coding[0].code, "dairy-free")
        self.assertEqual(
            inst.foodPreferenceModifier[0].coding[0].system, "http://hl7.org/fhir/diet"
        )
        self.assertEqual(inst.id, "renaldiet")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.oralDiet.nutrient[0].amount.code, "g")
        self.assertEqual(
            inst.oralDiet.nutrient[0].amount.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.oralDiet.nutrient[0].amount.unit, "grams")
        self.assertEqual(inst.oralDiet.nutrient[0].amount.value, 2)
        self.assertEqual(inst.oralDiet.nutrient[0].modifier.coding[0].code, "39972003")
        self.assertEqual(inst.oralDiet.nutrient[0].modifier.coding[0].display, "Sodium")
        self.assertEqual(
            inst.oralDiet.nutrient[0].modifier.coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(inst.oralDiet.nutrient[1].amount.code, "mg")
        self.assertEqual(
            inst.oralDiet.nutrient[1].amount.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.oralDiet.nutrient[1].amount.unit, "milligrams")
        self.assertEqual(inst.oralDiet.nutrient[1].amount.value, 1000)
        self.assertEqual(inst.oralDiet.nutrient[1].modifier.coding[0].code, "30820000")
        self.assertEqual(
            inst.oralDiet.nutrient[1].modifier.coding[0].display, "Phosphorus"
        )
        self.assertEqual(
            inst.oralDiet.nutrient[1].modifier.coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(inst.oralDiet.nutrient[2].amount.code, "g")
        self.assertEqual(
            inst.oralDiet.nutrient[2].amount.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.oralDiet.nutrient[2].amount.unit, "grams")
        self.assertEqual(inst.oralDiet.nutrient[2].amount.value, 2)
        self.assertEqual(inst.oralDiet.nutrient[2].modifier.coding[0].code, "88480006")
        self.assertEqual(
            inst.oralDiet.nutrient[2].modifier.coding[0].display, "Potassium"
        )
        self.assertEqual(
            inst.oralDiet.nutrient[2].modifier.coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.oralDiet.type[0].coding[0].code, "33489005")
        self.assertEqual(inst.oralDiet.type[0].coding[0].display, "Renal diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[1].code, "1050")
        self.assertEqual(inst.oralDiet.type[0].coding[1].display, "Renal")
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[0].text, "Renal Diet")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder6(self):
        inst = self.instantiate_from("nutritionorder-example-infantenteral.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder6(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder6(inst2)

    def implNutritionOrder6(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(
            inst.enteralFormula.additiveProductName, "Acme High Carbohydrate Additive"
        )
        self.assertEqual(
            inst.enteralFormula.additiveType.coding[0].code, "carbohydrate"
        )
        self.assertEqual(
            inst.enteralFormula.additiveType.coding[0].display,
            "Modular carbohydrate enteral formula component",
        )
        self.assertEqual(
            inst.enteralFormula.additiveType.coding[0].system,
            "http://hl7.org/fhir/entformula-additive",
        )
        self.assertEqual(
            inst.enteralFormula.administrationInstruction,
            "Add high calorie high carbohydrate additive to increase cal/oz from 24 cal/oz to 27 cal/oz.",
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].quantity.code, "[foz_us]"
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].quantity.system,
            "http://unitsofmeasure.org",
        )
        self.assertEqual(inst.enteralFormula.administration[0].quantity.unit, "ounces")
        self.assertEqual(inst.enteralFormula.administration[0].quantity.value, 4)
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.date,
            FHIRDate("2014-09-17").date,
        )
        self.assertEqual(
            inst.enteralFormula.administration[
                0
            ].schedule.repeat.boundsPeriod.start.as_json(),
            "2014-09-17",
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.frequency, 1
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.period, 3
        )
        self.assertEqual(
            inst.enteralFormula.administration[0].schedule.repeat.periodUnits, "h"
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaProductName, "Acme Infant Formula + Iron"
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaType.coding[0].code, "412414007"
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaType.coding[0].display,
            "infant formula + iron",
        )
        self.assertEqual(
            inst.enteralFormula.baseFormulaType.coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.code, "cal/[foz_us]")
        self.assertEqual(
            inst.enteralFormula.caloricDensity.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.enteralFormula.caloricDensity.unit, "calories per ounce")
        self.assertEqual(inst.enteralFormula.caloricDensity.value, 20)
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.code, "[foz_us]")
        self.assertEqual(
            inst.enteralFormula.maxVolumeToDeliver.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.unit, "ounces")
        self.assertEqual(inst.enteralFormula.maxVolumeToDeliver.value, 32)
        self.assertEqual(inst.enteralFormula.routeofAdministration.coding[0].code, "PO")
        self.assertEqual(
            inst.enteralFormula.routeofAdministration.coding[0].display, "Swallow, oral"
        )
        self.assertEqual(
            inst.enteralFormula.routeofAdministration.coding[0].system,
            "http://hl7.org/fhir/v3/RouteOfAdministration",
        )
        self.assertTrue(
            inst.enteralFormula.routeofAdministration.coding[0].userSelected
        )
        self.assertEqual(inst.id, "infantenteral")
        self.assertEqual(
            inst.identifier[0].system, "http://www.acme.org/nutritionorders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder7(self):
        inst = self.instantiate_from("nutritionorder-example-proteinsupplement.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder7(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder7(inst2)

    def implNutritionOrder7(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.id, "proteinsupplement")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.status, "active")
        self.assertEqual(
            inst.supplement[0].instruction,
            "Beneprotein 1 scoop TID with meal.starting on  2015-02-10",
        )
        self.assertEqual(inst.supplement[0].productName, "Beneprotein")
        self.assertEqual(inst.supplement[0].quantity.code, "{scoop}")
        self.assertEqual(
            inst.supplement[0].quantity.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.supplement[0].quantity.unit, "scoop")
        self.assertEqual(inst.supplement[0].quantity.value, 1)
        self.assertEqual(
            inst.supplement[0].schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.supplement[0].schedule[0].repeat.boundsPeriod.start.as_json(),
            "2015-02-10",
        )
        self.assertEqual(inst.supplement[0].schedule[0].repeat.when, "C")
        self.assertEqual(inst.supplement[0].type.coding[0].code, "442991000124104")
        self.assertEqual(
            inst.supplement[0].type.coding[0].display, "Adult high protein formula"
        )
        self.assertEqual(
            inst.supplement[0].type.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.supplement[0].type.coding[1].code, "1000")
        self.assertEqual(
            inst.supplement[0].type.coding[1].display, "High Protein Powder"
        )
        self.assertEqual(
            inst.supplement[0].type.coding[1].system,
            "http://goodhealthhospital.org/supplement-type-codes",
        )
        self.assertEqual(inst.supplement[0].type.text, "High Protein Powder")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder8(self):
        inst = self.instantiate_from("nutritionorder-example-pureeddiet-simple.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder8(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder8(inst2)

    def implNutritionOrder8(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.id, "pureeddiet-simple")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].coding[0].code, "439021000124105"
        )
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].coding[0].display,
            "Dietary liquid consistency - nectar thick liquid",
        )
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].text, "Nectar thick liquids"
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.oralDiet.texture[0].modifier.coding[0].code, "228055009")
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.coding[0].display, "Liquidized food"
        )
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.texture[0].modifier.text, "Pureed")
        self.assertEqual(inst.oralDiet.type[0].coding[0].code, "226211001")
        self.assertEqual(inst.oralDiet.type[0].coding[0].display, "Pureed diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[1].code, "1010")
        self.assertEqual(inst.oralDiet.type[0].coding[1].display, "Pureed diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[0].text, "Pureed diet")
        self.assertEqual(inst.status, "active")
        self.assertEqual(
            inst.supplement[0].instruction, "Ensure Pudding at breakfast, lunch, supper"
        )
        self.assertEqual(
            inst.supplement[0].productName, "Ensure Pudding 4 oz container"
        )
        self.assertEqual(inst.supplement[0].type.coding[0].code, "442971000124100")
        self.assertEqual(
            inst.supplement[0].type.coding[0].display, "Adult high energy formula"
        )
        self.assertEqual(
            inst.supplement[0].type.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.supplement[0].type.coding[1].code, "1040")
        self.assertEqual(
            inst.supplement[0].type.coding[1].display, "Adult high energy pudding"
        )
        self.assertEqual(
            inst.supplement[0].type.coding[1].system,
            "http://goodhealthhospital.org/supplement-type-codes",
        )
        self.assertEqual(inst.supplement[0].type.text, "Adult high energy pudding")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder9(self):
        inst = self.instantiate_from("nutritionorder-example-pureeddiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder9(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder9(inst2)

    def implNutritionOrder9(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].code, "227493005")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].display, "Cashew Nut")
        self.assertEqual(
            inst.excludeFoodModifier[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].version, "20140730")
        self.assertEqual(inst.foodPreferenceModifier[0].coding[0].code, "dairy-free")
        self.assertEqual(
            inst.foodPreferenceModifier[0].coding[0].system, "http://hl7.org/fhir/diet"
        )
        self.assertEqual(inst.id, "pureeddiet")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].coding[0].code, "439021000124105"
        )
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].coding[0].display,
            "Dietary liquid consistency - nectar thick liquid",
        )
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.oralDiet.fluidConsistencyType[0].text, "Nectar thick liquids"
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.oralDiet.texture[0].modifier.coding[0].code, "228055009")
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.coding[0].display, "Liquidized food"
        )
        self.assertEqual(
            inst.oralDiet.texture[0].modifier.coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.texture[0].modifier.text, "Pureed")
        self.assertEqual(inst.oralDiet.type[0].coding[0].code, "226211001")
        self.assertEqual(inst.oralDiet.type[0].coding[0].display, "Pureed diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[1].code, "1010")
        self.assertEqual(inst.oralDiet.type[0].coding[1].display, "Pureed diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[0].text, "Pureed diet")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")

    def testNutritionOrder10(self):
        inst = self.instantiate_from("nutritionorder-example-diabeticdiet.json")
        self.assertIsNotNone(inst, "Must have instantiated a NutritionOrder instance")
        self.implNutritionOrder10(inst)

        js = inst.as_json()
        self.assertEqual("NutritionOrder", js["resourceType"])
        inst2 = nutritionorder.NutritionOrder(js)
        self.implNutritionOrder10(inst2)

    def implNutritionOrder10(self, inst):
        self.assertEqual(inst.dateTime.date, FHIRDate("2014-09-17").date)
        self.assertEqual(inst.dateTime.as_json(), "2014-09-17")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].code, "227493005")
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].display, "Cashew Nut")
        self.assertEqual(
            inst.excludeFoodModifier[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.excludeFoodModifier[0].coding[0].version, "20140730")
        self.assertEqual(inst.foodPreferenceModifier[0].coding[0].code, "dairy-free")
        self.assertEqual(
            inst.foodPreferenceModifier[0].coding[0].system, "http://hl7.org/fhir/diet"
        )
        self.assertEqual(inst.id, "diabeticdiet")
        self.assertEqual(
            inst.identifier[0].system, "http://goodhealthhospital.org/nutrition-orders"
        )
        self.assertEqual(inst.identifier[0].value, "123")
        self.assertEqual(inst.oralDiet.nutrient[0].amount.code, "g")
        self.assertEqual(
            inst.oralDiet.nutrient[0].amount.system, "http://unitsofmeasure.org"
        )
        self.assertEqual(inst.oralDiet.nutrient[0].amount.unit, "grams")
        self.assertEqual(inst.oralDiet.nutrient[0].amount.value, 75)
        self.assertEqual(inst.oralDiet.nutrient[0].modifier.coding[0].code, "2331003")
        self.assertEqual(
            inst.oralDiet.nutrient[0].modifier.coding[0].display, "Carbohydrate"
        )
        self.assertEqual(
            inst.oralDiet.nutrient[0].modifier.coding[0].system,
            "http://snomed.info/sct",
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.date,
            FHIRDate("2015-02-10").date,
        )
        self.assertEqual(
            inst.oralDiet.schedule[0].repeat.boundsPeriod.start.as_json(), "2015-02-10"
        )
        self.assertEqual(inst.oralDiet.schedule[0].repeat.frequency, 3)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.period, 1)
        self.assertEqual(inst.oralDiet.schedule[0].repeat.periodUnits, "d")
        self.assertEqual(inst.oralDiet.type[0].coding[0].code, "160670007")
        self.assertEqual(inst.oralDiet.type[0].coding[0].display, "Diabetic diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[0].system, "http://snomed.info/sct"
        )
        self.assertEqual(inst.oralDiet.type[0].coding[1].code, "1030")
        self.assertEqual(inst.oralDiet.type[0].coding[1].display, "DD - Diabetic diet")
        self.assertEqual(
            inst.oralDiet.type[0].coding[1].system,
            "http://goodhealthhospital.org/diet-type-codes",
        )
        self.assertEqual(inst.oralDiet.type[0].text, "DD - Diabetic diet")
        self.assertEqual(inst.status, "active")
        self.assertEqual(inst.text.status, "generated")
