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

class DescribeImageGroupedVulListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Sas', '2018-12-03', 'DescribeImageGroupedVulList')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_IsLatest(self):
		return self.get_query_params().get('IsLatest')

	def set_IsLatest(self,IsLatest):
		self.add_query_param('IsLatest',IsLatest)

	def get_ImageTag(self):
		return self.get_query_params().get('ImageTag')

	def set_ImageTag(self,ImageTag):
		self.add_query_param('ImageTag',ImageTag)

	def get_GroupId(self):
		return self.get_query_params().get('GroupId')

	def set_GroupId(self,GroupId):
		self.add_query_param('GroupId',GroupId)

	def get_AliasName(self):
		return self.get_query_params().get('AliasName')

	def set_AliasName(self,AliasName):
		self.add_query_param('AliasName',AliasName)

	def get_PatchId(self):
		return self.get_query_params().get('PatchId')

	def set_PatchId(self,PatchId):
		self.add_query_param('PatchId',PatchId)

	def get_Name(self):
		return self.get_query_params().get('Name')

	def set_Name(self,Name):
		self.add_query_param('Name',Name)

	def get_Necessity(self):
		return self.get_query_params().get('Necessity')

	def set_Necessity(self,Necessity):
		self.add_query_param('Necessity',Necessity)

	def get_Uuids(self):
		return self.get_query_params().get('Uuids')

	def set_Uuids(self,Uuids):
		self.add_query_param('Uuids',Uuids)

	def get_RepoId(self):
		return self.get_query_params().get('RepoId')

	def set_RepoId(self,RepoId):
		self.add_query_param('RepoId',RepoId)

	def get_CveId(self):
		return self.get_query_params().get('CveId')

	def set_CveId(self,CveId):
		self.add_query_param('CveId',CveId)

	def get_RepoNamespace(self):
		return self.get_query_params().get('RepoNamespace')

	def set_RepoNamespace(self,RepoNamespace):
		self.add_query_param('RepoNamespace',RepoNamespace)

	def get_ImageDigest(self):
		return self.get_query_params().get('ImageDigest')

	def set_ImageDigest(self,ImageDigest):
		self.add_query_param('ImageDigest',ImageDigest)

	def get_PageSize(self):
		return self.get_query_params().get('PageSize')

	def set_PageSize(self,PageSize):
		self.add_query_param('PageSize',PageSize)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_CurrentPage(self):
		return self.get_query_params().get('CurrentPage')

	def set_CurrentPage(self,CurrentPage):
		self.add_query_param('CurrentPage',CurrentPage)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_RepoName(self):
		return self.get_query_params().get('RepoName')

	def set_RepoName(self,RepoName):
		self.add_query_param('RepoName',RepoName)

	def get_RepoInstanceId(self):
		return self.get_query_params().get('RepoInstanceId')

	def set_RepoInstanceId(self,RepoInstanceId):
		self.add_query_param('RepoInstanceId',RepoInstanceId)

	def get_ImageLayer(self):
		return self.get_query_params().get('ImageLayer')

	def set_ImageLayer(self,ImageLayer):
		self.add_query_param('ImageLayer',ImageLayer)

	def get_RepoRegionId(self):
		return self.get_query_params().get('RepoRegionId')

	def set_RepoRegionId(self,RepoRegionId):
		self.add_query_param('RepoRegionId',RepoRegionId)