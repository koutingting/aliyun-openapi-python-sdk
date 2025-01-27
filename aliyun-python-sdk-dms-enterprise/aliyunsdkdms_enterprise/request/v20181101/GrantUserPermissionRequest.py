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
from aliyunsdkdms_enterprise.endpoint import endpoint_data

class GrantUserPermissionRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dms-enterprise', '2018-11-01', 'GrantUserPermission','dms-enterprise')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_PermTypes(self): # String
		return self.get_query_params().get('PermTypes')

	def set_PermTypes(self, PermTypes):  # String
		self.add_query_param('PermTypes', PermTypes)
	def get_DsType(self): # String
		return self.get_query_params().get('DsType')

	def set_DsType(self, DsType):  # String
		self.add_query_param('DsType', DsType)
	def get_ExpireDate(self): # String
		return self.get_query_params().get('ExpireDate')

	def set_ExpireDate(self, ExpireDate):  # String
		self.add_query_param('ExpireDate', ExpireDate)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_Tid(self): # Long
		return self.get_query_params().get('Tid')

	def set_Tid(self, Tid):  # Long
		self.add_query_param('Tid', Tid)
	def get_InstanceId(self): # Long
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # Long
		self.add_query_param('InstanceId', InstanceId)
	def get_DbId(self): # String
		return self.get_query_params().get('DbId')

	def set_DbId(self, DbId):  # String
		self.add_query_param('DbId', DbId)
	def get_TableId(self): # String
		return self.get_query_params().get('TableId')

	def set_TableId(self, TableId):  # String
		self.add_query_param('TableId', TableId)
	def get_Logic(self): # Boolean
		return self.get_query_params().get('Logic')

	def set_Logic(self, Logic):  # Boolean
		self.add_query_param('Logic', Logic)
	def get_TableName(self): # String
		return self.get_query_params().get('TableName')

	def set_TableName(self, TableName):  # String
		self.add_query_param('TableName', TableName)
