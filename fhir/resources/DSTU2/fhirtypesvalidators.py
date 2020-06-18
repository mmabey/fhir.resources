# _*_ coding: utf-8 _*_
"""Validators for ``pydantic`` Custom DataType"""
import importlib
from pathlib import Path
from typing import Union

from pydantic.class_validators import make_generic_validator
from pydantic.types import StrBytes

from .fhirabstractmodel import FHIRAbstractModel

__author__ = "Md Nazrul Islam<email2nazrul@gmail.com>"

MODEL_CLASSES = {
    "Element": (None, ".element"),
    "Resource": (None, ".resource"),
    "DomainResource": (None, ".domainresource"),
    "BackboneElement": (None, ".backboneelement"),
    "Extension": (None, ".extension"),
    "Meta": (None, ".meta"),
    "Narrative": (None, ".narrative"),
    "Address": (None, ".address"),
    "Period": (None, ".period"),
    "Attachment": (None, ".attachment"),
    "CodeableConcept": (None, ".codeableconcept"),
    "Coding": (None, ".coding"),
    "ContactPoint": (None, ".contactpoint"),
    "HumanName": (None, ".humanname"),
    "Identifier": (None, ".identifier"),
    "Reference": (None, ".reference"),
    "Quantity": (None, ".quantity"),
    "Range": (None, ".range"),
    "Ratio": (None, ".ratio"),
    "Signature": (None, ".signature"),
    "Timing": (None, ".timing"),
    "TimingRepeat": (None, ".timing"),
    "Duration": (None, ".duration"),
    "Age": (None, ".age"),
    "Count": (None, ".count"),
    "Money": (None, ".money"),
    "Distance": (None, ".distance"),
    "SampledData": (None, ".sampleddata"),
    "Annotation": (None, ".annotation"),
    "Media": (None, ".media"),
    "Basic": (None, ".basic"),
    "Binary": (None, ".binary"),
    "BodySite": (None, ".bodysite"),
    "Flag": (None, ".flag"),
    "Location": (None, ".location"),
    "LocationPosition": (None, ".location"),
    "Slot": (None, ".slot"),
    "Schedule": (None, ".schedule"),
    "Account": (None, ".account"),
    "AllergyIntolerance": (None, ".allergyintolerance"),
    "AllergyIntoleranceReaction": (None, ".allergyintolerance"),
    "Appointment": (None, ".appointment"),
    "AppointmentParticipant": (None, ".appointment"),
    "AppointmentResponse": (None, ".appointmentresponse"),
    "AuditEvent": (None, ".auditevent"),
    "AuditEventEvent": (None, ".auditevent"),
    "AuditEventObject": (None, ".auditevent"),
    "AuditEventObjectDetail": (None, ".auditevent"),
    "AuditEventParticipant": (None, ".auditevent"),
    "AuditEventParticipantNetwork": (None, ".auditevent"),
    "AuditEventSource": (None, ".auditevent"),
}


def get_fhir_model_class(model_name: str) -> FHIRAbstractModel:
    """
    """
    global MODEL_CLASSES
    klass, module_name = MODEL_CLASSES[model_name]
    if klass is not None:
        return klass
    module = importlib.import_module(module_name, package=__package__)
    klass = getattr(module, model_name)
    MODEL_CLASSES[model_name] = (klass, module_name)
    return klass


def run_validator_for_fhir_type(model_type_cls, v, values, config, field):
    """ """
    cls = get_fhir_model_class(model_type_cls.__resource_type__)
    for validator in model_type_cls.__get_validators__():
        func = make_generic_validator(validator)
        v = func(cls, v, values, config, field)
    return v


def fhir_model_validator(
    model_name: str, v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    """ """
    model_class = get_fhir_model_class(model_name)
    if isinstance(v, (str, bytes)):
        v = model_class.parse_raw(v)
    elif isinstance(v, Path):
        v = model_class.parse_file(v)
    elif isinstance(v, dict):
        v = model_class.parse_obj(v)
    if not isinstance(v, FHIRAbstractModel):
        raise ValueError()
    if model_name != v.resource_type:
        raise ValueError
    return v


def element_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):

    return fhir_model_validator("Element", v)


def resource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):

    return fhir_model_validator("Resource", v)


def domainresource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):

    return fhir_model_validator("DomainResource", v)


def backboneelement_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BackboneElement", v)


def extension_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Extension", v)


def meta_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Meta", v)


def narrative_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Narrative", v)


def address_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Address", v)


def period_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Period", v)


def attachment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Attachment", v)


def codeableconcept_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("CodeableConcept", v)


def coding_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Coding", v)


def contactpoint_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("ContactPoint", v)


def humanname_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("HumanName", v)


def identifier_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Identifier", v)


def reference_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Reference", v)


def quantity_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Quantity", v)


def range_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Range", v)


def ratio_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Ratio", v)


def signature_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Signature", v)


def timing_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Timing", v)


def timingrepeat_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("TimingRepeat", v)


def duration_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Duration", v)


def age_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Age", v)


def count_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Count", v)


def money_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Money", v)


def distance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Distance", v)


def sampleddata_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("SampledData", v)


def annotation_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Annotation", v)


def media_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Media", v)


def basic_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Basic", v)


def binary_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Binary", v)


def bodysite_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("BodySite", v)


def flag_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Flag", v)


def location_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Location", v)


def locationposition_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("LocationPosition", v)


def slot_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Slot", v)


def schedule_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Slot", v)


def account_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Account", v)


def allergyintolerance_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AllergyIntolerance", v)


def allergyintolerancereaction_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AllergyIntoleranceReaction", v)


def appointment_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("Appointment", v)


def appointmentparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentParticipant", v)


def appointmentresponse_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AppointmentResponse", v)


def auditevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEvent", v)


def auditeventevent_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventEvent", v)


def auditeventobject_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventObject", v)


def auditeventobjectdetail_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventObjectDetail", v)


def auditeventparticipant_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventParticipant", v)


def auditeventparticipantnetwork_validator(
    v: Union[StrBytes, dict, Path, FHIRAbstractModel]
):
    return fhir_model_validator("AuditEventParticipantNetwork", v)


def auditeventsource_validator(v: Union[StrBytes, dict, Path, FHIRAbstractModel]):
    return fhir_model_validator("AuditEventSource", v)


__all__ = [
    "element_validator",
    "resource_validator",
    "domainresource_validator",
    "backboneelement_validator",
    "extension_validator",
    "meta_validator",
    "narrative_validator",
    "address_validator",
    "period_validator",
    "attachment_validator",
    "codeableconcept_validator",
    "coding_validator",
    "contactpoint_validator",
    "humanname_validator",
    "identifier_validator",
    "reference_validator",
    "quantity_validator",
    "range_validator",
    "ratio_validator",
    "signature_validator",
    "timing_validator",
    "timingrepeat_validator",
    "duration_validator",
    "age_validator",
    "count_validator",
    "money_validator",
    "distance_validator",
    "sampleddata_validator",
    "annotation_validator",
    "media_validator",
    "basic_validator",
    "binary_validator",
    "bodysite_validator",
    "flag_validator",
    "location_validator",
    "locationposition_validator",
    "slot_validator",
    "schedule_validator",
    "account_validator",
    "allergyintolerance_validator",
    "allergyintolerancereaction_validator",
    "appointment_validator",
    "appointmentparticipant_validator",
    "appointmentresponse_validator",
    "auditevent_validator",
    "auditeventevent_validator",
    "auditeventobjectdetail_validator",
    "auditeventparticipantnetwork_validator",
    "auditeventsource_validator",
]