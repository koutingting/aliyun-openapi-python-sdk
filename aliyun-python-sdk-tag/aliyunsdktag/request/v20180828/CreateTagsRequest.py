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
from aliyunsdktag.endpoint import endpoint_data

class CreateTagsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Tag', '2018-08-28', 'CreateTags','tag')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_ResourceOwnerAccount(self): # String
		return self.get_query_params().get('ResourceOwnerAccount')

	def set_ResourceOwnerAccount(self, ResourceOwnerAccount):  # String
		self.add_query_param('ResourceOwnerAccount', ResourceOwnerAccount)
	def get_OwnerAccount(self): # String
		return self.get_query_params().get('OwnerAccount')

	def set_OwnerAccount(self, OwnerAccount):  # String
		self.add_query_param('OwnerAccount', OwnerAccount)
	def get_OwnerId(self): # Long
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self, OwnerId):  # Long
		self.add_query_param('OwnerId', OwnerId)
	def get_TagKeyValueParamLists(self): # RepeatList
		return self.get_query_params().get('TagKeyValueParamList')

	def set_TagKeyValueParamLists(self, TagKeyValueParamList):  # RepeatList
		for depth1 in range(len(TagKeyValueParamList)):
			if TagKeyValueParamList[depth1].get('Key') is not None:
				self.add_query_param('TagKeyValueParamList.' + str(depth1 + 1) + '.Key', TagKeyValueParamList[depth1].get('Key'))
			if TagKeyValueParamList[depth1].get('TagValueParamList') is not None:
				for depth2 in range(len(TagKeyValueParamList[depth1].get('TagValueParamList'))):
					if TagKeyValueParamList[depth1].get('TagValueParamList')[depth2].get('Value') is not None:
						self.add_query_param('TagKeyValueParamList.' + str(depth1 + 1) + str(depth2 + 1) + '.Value', TagKeyValueParamList[depth1].get('TagValueParamList')[depth2].get('Value'))
					if TagKeyValueParamList[depth1].get('TagValueParamList')[depth2].get('Description') is not None:
						self.add_query_param('TagKeyValueParamList.' + str(depth1 + 1) + str(depth2 + 1) + '.Description', TagKeyValueParamList[depth1].get('TagValueParamList')[depth2].get('Description'))
			if TagKeyValueParamList[depth1].get('Description') is not None:
				self.add_query_param('TagKeyValueParamList.' + str(depth1 + 1) + '.Description', TagKeyValueParamList[depth1].get('Description'))
