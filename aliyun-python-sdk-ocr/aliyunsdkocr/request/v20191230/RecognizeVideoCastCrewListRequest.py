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
from aliyunsdkocr.endpoint import endpoint_data
import json

class RecognizeVideoCastCrewListRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'ocr', '2019-12-30', 'RecognizeVideoCastCrewList','ocr')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_Params(self): # Array
		return self.get_body_params().get('Params')

	def set_Params(self, Params):  # Array
		self.add_body_params("Params", json.dumps(Params))
	def get_RegisterUrl(self): # String
		return self.get_body_params().get('RegisterUrl')

	def set_RegisterUrl(self, RegisterUrl):  # String
		self.add_body_params('RegisterUrl', RegisterUrl)
	def get_VideoUrl(self): # String
		return self.get_body_params().get('VideoUrl')

	def set_VideoUrl(self, VideoUrl):  # String
		self.add_body_params('VideoUrl', VideoUrl)
