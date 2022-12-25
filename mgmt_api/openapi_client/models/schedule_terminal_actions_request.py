# coding: utf-8

"""
    Management API

    Configure and manage your Adyen company and merchant accounts, stores, and payment terminals. ## Authentication Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.  To access the live endpoints, you need to generate a new API key in your live Customer Area. ## Versioning  Management API handles versioning as part of the endpoint URL. For example, to send a request to version 1 of the `/companies/{companyId}/webhooks` endpoint, use:  ```text https://management-test.adyen.com/v1/companies/{companyId}/webhooks ```  ## Going live  To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:  ```text https://management-live.adyen.com/v1 ```  # noqa: E501

    The version of the OpenAPI document: 1
    Contact: developer-experience@adyen.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr
from openapi_client.models.schedule_terminal_actions_request_action_details import ScheduleTerminalActionsRequestActionDetails

class ScheduleTerminalActionsRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    action_details: Optional[ScheduleTerminalActionsRequestActionDetails] = Field(None, alias="actionDetails")
    scheduled_at: Optional[StrictStr] = Field(None, alias="scheduledAt", description="The date and time when the action should happen.  Format: [RFC 3339](https://www.rfc-editor.org/rfc/rfc3339), but without the **Z** before the time offset. For example, **2021-11-15T12:16:21+01:00**  The action is sent with the first [maintenance call](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api#when-actions-take-effect) after the specified date and time in the time zone of the terminal.  An empty value causes the action to be sent as soon as possible: at the next maintenance call.")
    store_id: Optional[StrictStr] = Field(None, alias="storeId", description="The unique ID of the [store](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores). If present, all terminals in the `terminalIds` list must be assigned to this store.")
    terminal_ids: Optional[List[StrictStr]] = Field(None, alias="terminalIds", description="A list of unique IDs of the terminals to apply the action to. You can extract the IDs from the [GET `/terminals`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/terminals) response. Maximum length: 100 IDs.")
    __properties = ["actionDetails", "scheduledAt", "storeId", "terminalIds"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ScheduleTerminalActionsRequest:
        """Create an instance of ScheduleTerminalActionsRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of action_details
        if self.action_details:
            _dict['actionDetails'] = self.action_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ScheduleTerminalActionsRequest:
        """Create an instance of ScheduleTerminalActionsRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ScheduleTerminalActionsRequest.parse_obj(obj)

        _obj = ScheduleTerminalActionsRequest.parse_obj({
            "action_details": ScheduleTerminalActionsRequestActionDetails.from_dict(obj.get("actionDetails")) if obj.get("actionDetails") is not None else None,
            "scheduled_at": obj.get("scheduledAt"),
            "store_id": obj.get("storeId"),
            "terminal_ids": obj.get("terminalIds")
        })
        return _obj

