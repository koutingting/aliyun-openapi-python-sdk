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
from aliyunsdkdcdn.endpoint import endpoint_data

class CreateDcdnSLSRealTimeLogDeliveryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'dcdn', '2018-01-15', 'CreateDcdnSLSRealTimeLogDelivery')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_SLSLogStore(self):
		return self.get_body_params().get('SLSLogStore')

	def set_SLSLogStore(self,SLSLogStore):
		self.add_body_params('SLSLogStore', SLSLogStore)

	def get_SLSProject(self):
		return self.get_body_params().get('SLSProject')

	def set_SLSProject(self,SLSProject):
		self.add_body_params('SLSProject', SLSProject)

	def get_BusinessType(self):
		return self.get_body_params().get('BusinessType')

	def set_BusinessType(self,BusinessType):
		self.add_body_params('BusinessType', BusinessType)

	def get_SLSRegion(self):
		return self.get_body_params().get('SLSRegion')

	def set_SLSRegion(self,SLSRegion):
		self.add_body_params('SLSRegion', SLSRegion)

	def get_ProjectName(self):
		return self.get_body_params().get('ProjectName')

	def set_ProjectName(self,ProjectName):
		self.add_body_params('ProjectName', ProjectName)

	def get_DomainName(self):
		return self.get_body_params().get('DomainName')

	def set_DomainName(self,DomainName):
		self.add_body_params('DomainName', DomainName)

	def get_SamplingRate(self):
		return self.get_body_params().get('SamplingRate')

	def set_SamplingRate(self,SamplingRate):
		self.add_body_params('SamplingRate', SamplingRate)

	def get_DataCenter(self):
		return self.get_body_params().get('DataCenter')

	def set_DataCenter(self,DataCenter):
		self.add_body_params('DataCenter', DataCenter)

	def get_OwnerId(self):
		return self.get_query_params().get('OwnerId')

	def set_OwnerId(self,OwnerId):
		self.add_query_param('OwnerId',OwnerId)