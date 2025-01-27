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
from aliyunsdkquickbi_public.endpoint import endpoint_data

class AddShareReportRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'quickbi-public', '2022-01-01', 'AddShareReport','quickbi')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_AuthPoint(self):
		return self.get_query_params().get('AuthPoint')

	def set_AuthPoint(self,AuthPoint):
		self.add_query_param('AuthPoint',AuthPoint)

	def get_ExpireDate(self):
		return self.get_query_params().get('ExpireDate')

	def set_ExpireDate(self,ExpireDate):
		self.add_query_param('ExpireDate',ExpireDate)

	def get_ShareToType(self):
		return self.get_query_params().get('ShareToType')

	def set_ShareToType(self,ShareToType):
		self.add_query_param('ShareToType',ShareToType)

	def get_WorksId(self):
		return self.get_query_params().get('WorksId')

	def set_WorksId(self,WorksId):
		self.add_query_param('WorksId',WorksId)

	def get_ShareToId(self):
		return self.get_query_params().get('ShareToId')

	def set_ShareToId(self,ShareToId):
		self.add_query_param('ShareToId',ShareToId)