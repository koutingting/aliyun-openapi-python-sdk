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
from aliyunsdkoutboundbot.endpoint import endpoint_data

class CreateBatchJobsRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'OutboundBot', '2019-12-26', 'CreateBatchJobs','outboundbot')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_JobFilePath(self): # String
		return self.get_query_params().get('JobFilePath')

	def set_JobFilePath(self, JobFilePath):  # String
		self.add_query_param('JobFilePath', JobFilePath)
	def get_ScriptId(self): # String
		return self.get_query_params().get('ScriptId')

	def set_ScriptId(self, ScriptId):  # String
		self.add_query_param('ScriptId', ScriptId)
	def get_CallingNumbers(self): # RepeatList
		return self.get_query_params().get('CallingNumber')

	def set_CallingNumbers(self, CallingNumber):  # RepeatList
		for depth1 in range(len(CallingNumber)):
			self.add_query_param('CallingNumber.' + str(depth1 + 1), CallingNumber[depth1])
	def get_InstanceId(self): # String
		return self.get_query_params().get('InstanceId')

	def set_InstanceId(self, InstanceId):  # String
		self.add_query_param('InstanceId', InstanceId)
	def get_Submitted(self): # Boolean
		return self.get_query_params().get('Submitted')

	def set_Submitted(self, Submitted):  # Boolean
		self.add_query_param('Submitted', Submitted)
	def get_BatchJobName(self): # String
		return self.get_query_params().get('BatchJobName')

	def set_BatchJobName(self, BatchJobName):  # String
		self.add_query_param('BatchJobName', BatchJobName)
	def get_StrategyJson(self): # String
		return self.get_query_params().get('StrategyJson')

	def set_StrategyJson(self, StrategyJson):  # String
		self.add_query_param('StrategyJson', StrategyJson)
	def get_BatchJobDescription(self): # String
		return self.get_query_params().get('BatchJobDescription')

	def set_BatchJobDescription(self, BatchJobDescription):  # String
		self.add_query_param('BatchJobDescription', BatchJobDescription)
	def get_ScenarioId(self): # String
		return self.get_query_params().get('ScenarioId')

	def set_ScenarioId(self, ScenarioId):  # String
		self.add_query_param('ScenarioId', ScenarioId)
