# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkdataworks_public.endpoint import endpoint_data

class UpdateTableModelInfoRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dataworks-public', '2020-05-18', 'UpdateTableModelInfo')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_SecondLevelThemeId(self): # Long
		return self.get_query_params().get('SecondLevelThemeId')

	def set_SecondLevelThemeId(self, SecondLevelThemeId):  # Long
		self.add_query_param('SecondLevelThemeId', SecondLevelThemeId)
	def get_TableGuid(self): # String
		return self.get_query_params().get('TableGuid')

	def set_TableGuid(self, TableGuid):  # String
		self.add_query_param('TableGuid', TableGuid)
	def get_LevelId(self): # Long
		return self.get_query_params().get('LevelId')

	def set_LevelId(self, LevelId):  # Long
		self.add_query_param('LevelId', LevelId)
	def get_LevelType(self): # Integer
		return self.get_query_params().get('LevelType')

	def set_LevelType(self, LevelType):  # Integer
		self.add_query_param('LevelType', LevelType)
	def get_FirstLevelThemeId(self): # Long
		return self.get_query_params().get('FirstLevelThemeId')

	def set_FirstLevelThemeId(self, FirstLevelThemeId):  # Long
		self.add_query_param('FirstLevelThemeId', FirstLevelThemeId)
