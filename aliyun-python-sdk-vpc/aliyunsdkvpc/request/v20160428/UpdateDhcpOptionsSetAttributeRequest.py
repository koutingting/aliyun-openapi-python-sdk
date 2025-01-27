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
from aliyunsdkvpc.endpoint import endpoint_data

class UpdateDhcpOptionsSetAttributeRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Vpc', '2016-04-28', 'UpdateDhcpOptionsSetAttribute','vpc')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_BootFileName(self): # String
		return self.get_query_params().get('BootFileName')

	def set_BootFileName(self, BootFileName):  # String
		self.add_query_param('BootFileName', BootFileName)
	def get_ResourceOwnerId(self): # Long
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self, ResourceOwnerId):  # Long
		self.add_query_param('ResourceOwnerId', ResourceOwnerId)
	def get_ClientToken(self): # String
		return self.get_query_params().get('ClientToken')

	def set_ClientToken(self, ClientToken):  # String
		self.add_query_param('ClientToken', ClientToken)
	def get_TFTPServerName(self): # String
		return self.get_query_params().get('TFTPServerName')

	def set_TFTPServerName(self, TFTPServerName):  # String
		self.add_query_param('TFTPServerName', TFTPServerName)
	def get_DomainNameServers(self): # String
		return self.get_query_params().get('DomainNameServers')

	def set_DomainNameServers(self, DomainNameServers):  # String
		self.add_query_param('DomainNameServers', DomainNameServers)
	def get_DhcpOptionsSetDescription(self): # String
		return self.get_query_params().get('DhcpOptionsSetDescription')

	def set_DhcpOptionsSetDescription(self, DhcpOptionsSetDescription):  # String
		self.add_query_param('DhcpOptionsSetDescription', DhcpOptionsSetDescription)
	def get_DryRun(self): # Boolean
		return self.get_query_params().get('DryRun')

	def set_DryRun(self, DryRun):  # Boolean
		self.add_query_param('DryRun', DryRun)
	def get_DhcpOptionsSetId(self): # String
		return self.get_query_params().get('DhcpOptionsSetId')

	def set_DhcpOptionsSetId(self, DhcpOptionsSetId):  # String
		self.add_query_param('DhcpOptionsSetId', DhcpOptionsSetId)
	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_DomainName(self): # String
		return self.get_query_params().get('DomainName')

	def set_DomainName(self, DomainName):  # String
		self.add_query_param('DomainName', DomainName)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_DhcpOptionsSetName(self): # String
		return self.get_query_params().get('DhcpOptionsSetName')

	def set_DhcpOptionsSetName(self, DhcpOptionsSetName):  # String
		self.add_query_param('DhcpOptionsSetName', DhcpOptionsSetName)
