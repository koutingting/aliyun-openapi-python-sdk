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
from aliyunsdkdas.endpoint import endpoint_data

class GetPartitionsHeatmapRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'DAS', '2020-01-16', 'GetPartitionsHeatmap')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_skipAuth(self): # String
		return self.get_query_params().get('skipAuth')

	def set_skipAuth(self, skipAuth):  # String
		self.add_query_param('skipAuth', skipAuth)
	def get_signature(self): # String
		return self.get_query_params().get('signature')

	def set_signature(self, signature):  # String
		self.add_query_param('signature', signature)
	def get_Type(self): # String
		return self.get_query_params().get('Type')

	def set_Type(self, Type):  # String
		self.add_query_param('Type', Type)
	def get_UserId(self): # String
		return self.get_query_params().get('UserId')

	def set_UserId(self, UserId):  # String
		self.add_query_param('UserId', UserId)
	def get_Uid(self): # String
		return self.get_query_params().get('Uid')

	def set_Uid(self, Uid):  # String
		self.add_query_param('Uid', Uid)
	def get_ConsoleContext(self): # String
		return self.get_query_params().get('ConsoleContext')

	def set_ConsoleContext(self, ConsoleContext):  # String
		self.add_query_param('ConsoleContext', ConsoleContext)
	def get_accessKey(self): # String
		return self.get_query_params().get('accessKey')

	def set_accessKey(self, accessKey):  # String
		self.add_query_param('accessKey', accessKey)
	def get_timestamp(self): # String
		return self.get_query_params().get('timestamp')

	def set_timestamp(self, timestamp):  # String
		self.add_query_param('timestamp', timestamp)
	def get_TimeRange(self): # String
		return self.get_query_params().get('TimeRange')

	def set_TimeRange(self, TimeRange):  # String
		self.add_query_param('TimeRange', TimeRange)
	def get___context(self): # String
		return self.get_query_params().get('__context')

	def set___context(self, __context):  # String
		self.add_query_param('__context', __context)
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
