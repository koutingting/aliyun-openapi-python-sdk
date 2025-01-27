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

from aliyunsdkcore.request import RoaRequest
from aliyunsdkedas.endpoint import endpoint_data

class AddMockRuleRequest(RoaRequest):

	def __init__(self):
		RoaRequest.__init__(self, 'Edas', '2017-08-01', 'AddMockRule','Edas')
		self.set_uri_pattern('/pop/sp/api/mock/addMockRule')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ScMockItemJson(self): # String
		return self.get_query_params().get('ScMockItemJson')

	def set_ScMockItemJson(self, ScMockItemJson):  # String
		self.add_query_param('ScMockItemJson', ScMockItemJson)
	def get_DubboMockItemJson(self): # String
		return self.get_query_params().get('DubboMockItemJson')

	def set_DubboMockItemJson(self, DubboMockItemJson):  # String
		self.add_query_param('DubboMockItemJson', DubboMockItemJson)
	def get_ExtraJson(self): # String
		return self.get_query_params().get('ExtraJson')

	def set_ExtraJson(self, ExtraJson):  # String
		self.add_query_param('ExtraJson', ExtraJson)
	def get_ProviderAppId(self): # String
		return self.get_query_params().get('ProviderAppId')

	def set_ProviderAppId(self, ProviderAppId):  # String
		self.add_query_param('ProviderAppId', ProviderAppId)
	def get_Source(self): # String
		return self.get_query_params().get('Source')

	def set_Source(self, Source):  # String
		self.add_query_param('Source', Source)
	def get_Enable(self): # Boolean
		return self.get_query_params().get('Enable')

	def set_Enable(self, Enable):  # Boolean
		self.add_query_param('Enable', Enable)
	def get_ProviderAppName(self): # String
		return self.get_query_params().get('ProviderAppName')

	def set_ProviderAppName(self, ProviderAppName):  # String
		self.add_query_param('ProviderAppName', ProviderAppName)
	def get_Name(self): # String
		return self.get_query_params().get('Name')

	def set_Name(self, Name):  # String
		self.add_query_param('Name', Name)
	def get_Namespace(self): # String
		return self.get_query_params().get('Namespace')

	def set_Namespace(self, Namespace):  # String
		self.add_query_param('Namespace', Namespace)
	def get_ConsumerAppsJson(self): # String
		return self.get_query_params().get('ConsumerAppsJson')

	def set_ConsumerAppsJson(self, ConsumerAppsJson):  # String
		self.add_query_param('ConsumerAppsJson', ConsumerAppsJson)
	def get_MockType(self): # Long
		return self.get_query_params().get('MockType')

	def set_MockType(self, MockType):  # Long
		self.add_query_param('MockType', MockType)
	def get_Region(self): # String
		return self.get_query_params().get('Region')

	def set_Region(self, Region):  # String
		self.add_query_param('Region', Region)
