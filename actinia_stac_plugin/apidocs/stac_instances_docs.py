#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Copyright (c) 2021 mundialis GmbH & Co. KG

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.


Documentation for STAC module api endpoints
"""

__author__ = "Jorge Herrera"
__copyright__ = "2018-2021 mundialis GmbH & Co. KG"
__license__ = "GPLv3"


from actinia_stac_plugin.apidocs.schemas import AddInstaceModel


stacinstances_get_docs = {
    "tags": ["STAC"],
    "description": "Get a list of STAC Instances. " "Minimum required user role: user.",
    "parameters": [],
    "responses": {
        "200": {"description": "This response returns a list of STAC Instances"}
    },
}

stacinstances_post_docs = {
    "tags": ["STAC"],
    "description": "Add a new STAC instances to the user",
    "parameters": [
        {
            "in": "body",
            "name": "Adding Instance",
            "type": "object",
            "schema": AddInstaceModel,
            "description": "the Instance ID where the Collection will be stored",
            "required": True,
        }
    ],
    "responses": {
        "200": {
            "description": "This response returns a message with the Instance successfully added"
        }
    },
}