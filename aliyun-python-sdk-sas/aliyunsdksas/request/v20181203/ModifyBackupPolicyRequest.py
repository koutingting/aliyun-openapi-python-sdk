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
from aliyunsdksas.endpoint import endpoint_data

class ModifyBackupPolicyRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'ModifyBackupPolicy')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_UuidLists(self):
		return self.get_query_params().get('UuidList')

	def set_UuidLists(self, UuidLists):
		for depth1 in range(len(UuidLists)):
			if UuidLists[depth1] is not None:
				self.add_query_param('UuidList.' + str(depth1 + 1) , UuidLists[depth1])

	def get_Id(self):
		return self.get_query_params().get('Id')

	def set_Id(self,Id):
		self.add_query_param('Id',Id)

	def get_Policy(self):
		return self.get_query_params().get('Policy')

	def set_Policy(self,Policy):
		self.add_query_param('Policy',Policy)

	def get_PolicyVersion(self):
		return self.get_query_params().get('PolicyVersion')

	def set_PolicyVersion(self,PolicyVersion):
		self.add_query_param('PolicyVersion',PolicyVersion)

	def get_PolicyRegionId(self):
		return self.get_query_params().get('PolicyRegionId')

	def set_PolicyRegionId(self,PolicyRegionId):
		self.add_query_param('PolicyRegionId',PolicyRegionId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)