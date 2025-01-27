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
from aliyunsdkpush.endpoint import endpoint_data

class PushRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Push', '2016-08-01', 'Push')
		self.set_method('POST')

		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())

	def get_AndroidNotificationBarType(self): # Integer
		return self.get_query_params().get('AndroidNotificationBarType')

	def set_AndroidNotificationBarType(self, AndroidNotificationBarType):  # Integer
		self.add_query_param('AndroidNotificationBarType', AndroidNotificationBarType)
	def get_SmsSendPolicy(self): # Integer
		return self.get_query_params().get('SmsSendPolicy')

	def set_SmsSendPolicy(self, SmsSendPolicy):  # Integer
		self.add_query_param('SmsSendPolicy', SmsSendPolicy)
	def get_Body(self): # String
		return self.get_query_params().get('Body')

	def set_Body(self, Body):  # String
		self.add_query_param('Body', Body)
	def get_DeviceType(self): # String
		return self.get_query_params().get('DeviceType')

	def set_DeviceType(self, DeviceType):  # String
		self.add_query_param('DeviceType', DeviceType)
	def get_PushTime(self): # String
		return self.get_query_params().get('PushTime')

	def set_PushTime(self, PushTime):  # String
		self.add_query_param('PushTime', PushTime)
	def get_SendSpeed(self): # Integer
		return self.get_query_params().get('SendSpeed')

	def set_SendSpeed(self, SendSpeed):  # Integer
		self.add_query_param('SendSpeed', SendSpeed)
	def get_AndroidNotificationHuaweiChannel(self): # String
		return self.get_query_params().get('AndroidNotificationHuaweiChannel')

	def set_AndroidNotificationHuaweiChannel(self, AndroidNotificationHuaweiChannel):  # String
		self.add_query_param('AndroidNotificationHuaweiChannel', AndroidNotificationHuaweiChannel)
	def get_AndroidPopupActivity(self): # String
		return self.get_query_params().get('AndroidPopupActivity')

	def set_AndroidPopupActivity(self, AndroidPopupActivity):  # String
		self.add_query_param('AndroidPopupActivity', AndroidPopupActivity)
	def get_iOSRemindBody(self): # String
		return self.get_query_params().get('iOSRemindBody')

	def set_iOSRemindBody(self, iOSRemindBody):  # String
		self.add_query_param('iOSRemindBody', iOSRemindBody)
	def get_Trim(self): # Boolean
		return self.get_query_params().get('Trim')

	def set_Trim(self, Trim):  # Boolean
		self.add_query_param('Trim', Trim)
	def get_AndroidNotifyType(self): # String
		return self.get_query_params().get('AndroidNotifyType')

	def set_AndroidNotifyType(self, AndroidNotifyType):  # String
		self.add_query_param('AndroidNotifyType', AndroidNotifyType)
	def get_AndroidPopupTitle(self): # String
		return self.get_query_params().get('AndroidPopupTitle')

	def set_AndroidPopupTitle(self, AndroidPopupTitle):  # String
		self.add_query_param('AndroidPopupTitle', AndroidPopupTitle)
	def get_AndroidMessageHuaweiCategory(self): # String
		return self.get_query_params().get('AndroidMessageHuaweiCategory')

	def set_AndroidMessageHuaweiCategory(self, AndroidMessageHuaweiCategory):  # String
		self.add_query_param('AndroidMessageHuaweiCategory', AndroidMessageHuaweiCategory)
	def get_iOSMusic(self): # String
		return self.get_query_params().get('iOSMusic')

	def set_iOSMusic(self, iOSMusic):  # String
		self.add_query_param('iOSMusic', iOSMusic)
	def get_iOSApnsEnv(self): # String
		return self.get_query_params().get('iOSApnsEnv')

	def set_iOSApnsEnv(self, iOSApnsEnv):  # String
		self.add_query_param('iOSApnsEnv', iOSApnsEnv)
	def get_iOSMutableContent(self): # Boolean
		return self.get_query_params().get('iOSMutableContent')

	def set_iOSMutableContent(self, iOSMutableContent):  # Boolean
		self.add_query_param('iOSMutableContent', iOSMutableContent)
	def get_AndroidNotificationBarPriority(self): # Integer
		return self.get_query_params().get('AndroidNotificationBarPriority')

	def set_AndroidNotificationBarPriority(self, AndroidNotificationBarPriority):  # Integer
		self.add_query_param('AndroidNotificationBarPriority', AndroidNotificationBarPriority)
	def get_ExpireTime(self): # String
		return self.get_query_params().get('ExpireTime')

	def set_ExpireTime(self, ExpireTime):  # String
		self.add_query_param('ExpireTime', ExpireTime)
	def get_AndroidImageUrl(self): # String
		return self.get_query_params().get('AndroidImageUrl')

	def set_AndroidImageUrl(self, AndroidImageUrl):  # String
		self.add_query_param('AndroidImageUrl', AndroidImageUrl)
	def get_AndroidNotificationVivoChannel(self): # String
		return self.get_query_params().get('AndroidNotificationVivoChannel')

	def set_AndroidNotificationVivoChannel(self, AndroidNotificationVivoChannel):  # String
		self.add_query_param('AndroidNotificationVivoChannel', AndroidNotificationVivoChannel)
	def get_iOSNotificationCategory(self): # String
		return self.get_query_params().get('iOSNotificationCategory')

	def set_iOSNotificationCategory(self, iOSNotificationCategory):  # String
		self.add_query_param('iOSNotificationCategory', iOSNotificationCategory)
	def get_AndroidNotificationXiaomiChannel(self): # String
		return self.get_query_params().get('AndroidNotificationXiaomiChannel')

	def set_AndroidNotificationXiaomiChannel(self, AndroidNotificationXiaomiChannel):  # String
		self.add_query_param('AndroidNotificationXiaomiChannel', AndroidNotificationXiaomiChannel)
	def get_StoreOffline(self): # Boolean
		return self.get_query_params().get('StoreOffline')

	def set_StoreOffline(self, StoreOffline):  # Boolean
		self.add_query_param('StoreOffline', StoreOffline)
	def get_SmsParams(self): # String
		return self.get_query_params().get('SmsParams')

	def set_SmsParams(self, SmsParams):  # String
		self.add_query_param('SmsParams', SmsParams)
	def get_iOSRelevanceScore(self): # Double
		return self.get_query_params().get('iOSRelevanceScore')

	def set_iOSRelevanceScore(self, iOSRelevanceScore):  # Double
		self.add_query_param('iOSRelevanceScore', iOSRelevanceScore)
	def get_AndroidVivoPushMode(self): # Integer
		return self.get_query_params().get('AndroidVivoPushMode')

	def set_AndroidVivoPushMode(self, AndroidVivoPushMode):  # Integer
		self.add_query_param('AndroidVivoPushMode', AndroidVivoPushMode)
	def get_AndroidInboxBody(self): # String
		return self.get_query_params().get('AndroidInboxBody')

	def set_AndroidInboxBody(self, AndroidInboxBody):  # String
		self.add_query_param('AndroidInboxBody', AndroidInboxBody)
	def get_JobKey(self): # String
		return self.get_query_params().get('JobKey')

	def set_JobKey(self, JobKey):  # String
		self.add_query_param('JobKey', JobKey)
	def get_AndroidOpenUrl(self): # String
		return self.get_query_params().get('AndroidOpenUrl')

	def set_AndroidOpenUrl(self, AndroidOpenUrl):  # String
		self.add_query_param('AndroidOpenUrl', AndroidOpenUrl)
	def get_AndroidXiaoMiNotifyBody(self): # String
		return self.get_query_params().get('AndroidXiaoMiNotifyBody')

	def set_AndroidXiaoMiNotifyBody(self, AndroidXiaoMiNotifyBody):  # String
		self.add_query_param('AndroidXiaoMiNotifyBody', AndroidXiaoMiNotifyBody)
	def get_iOSSubtitle(self): # String
		return self.get_query_params().get('iOSSubtitle')

	def set_iOSSubtitle(self, iOSSubtitle):  # String
		self.add_query_param('iOSSubtitle', iOSSubtitle)
	def get_AndroidXiaomiBigPictureUrl(self): # String
		return self.get_query_params().get('AndroidXiaomiBigPictureUrl')

	def set_AndroidXiaomiBigPictureUrl(self, AndroidXiaomiBigPictureUrl):  # String
		self.add_query_param('AndroidXiaomiBigPictureUrl', AndroidXiaomiBigPictureUrl)
	def get_iOSRemind(self): # Boolean
		return self.get_query_params().get('iOSRemind')

	def set_iOSRemind(self, iOSRemind):  # Boolean
		self.add_query_param('iOSRemind', iOSRemind)
	def get_iOSNotificationThreadId(self): # String
		return self.get_query_params().get('iOSNotificationThreadId')

	def set_iOSNotificationThreadId(self, iOSNotificationThreadId):  # String
		self.add_query_param('iOSNotificationThreadId', iOSNotificationThreadId)
	def get_AndroidMusic(self): # String
		return self.get_query_params().get('AndroidMusic')

	def set_AndroidMusic(self, AndroidMusic):  # String
		self.add_query_param('AndroidMusic', AndroidMusic)
	def get_iOSNotificationCollapseId(self): # String
		return self.get_query_params().get('iOSNotificationCollapseId')

	def set_iOSNotificationCollapseId(self, iOSNotificationCollapseId):  # String
		self.add_query_param('iOSNotificationCollapseId', iOSNotificationCollapseId)
	def get_AndroidMessageHuaweiUrgency(self): # String
		return self.get_query_params().get('AndroidMessageHuaweiUrgency')

	def set_AndroidMessageHuaweiUrgency(self, AndroidMessageHuaweiUrgency):  # String
		self.add_query_param('AndroidMessageHuaweiUrgency', AndroidMessageHuaweiUrgency)
	def get_PushType(self): # String
		return self.get_query_params().get('PushType')

	def set_PushType(self, PushType):  # String
		self.add_query_param('PushType', PushType)
	def get_iOSInterruptionLevel(self): # String
		return self.get_query_params().get('iOSInterruptionLevel')

	def set_iOSInterruptionLevel(self, iOSInterruptionLevel):  # String
		self.add_query_param('iOSInterruptionLevel', iOSInterruptionLevel)
	def get_AndroidExtParameters(self): # String
		return self.get_query_params().get('AndroidExtParameters')

	def set_AndroidExtParameters(self, AndroidExtParameters):  # String
		self.add_query_param('AndroidExtParameters', AndroidExtParameters)
	def get_iOSBadge(self): # Integer
		return self.get_query_params().get('iOSBadge')

	def set_iOSBadge(self, iOSBadge):  # Integer
		self.add_query_param('iOSBadge', iOSBadge)
	def get_AndroidBigBody(self): # String
		return self.get_query_params().get('AndroidBigBody')

	def set_AndroidBigBody(self, AndroidBigBody):  # String
		self.add_query_param('AndroidBigBody', AndroidBigBody)
	def get_iOSBadgeAutoIncrement(self): # Boolean
		return self.get_query_params().get('iOSBadgeAutoIncrement')

	def set_iOSBadgeAutoIncrement(self, iOSBadgeAutoIncrement):  # Boolean
		self.add_query_param('iOSBadgeAutoIncrement', iOSBadgeAutoIncrement)
	def get_AndroidOpenType(self): # String
		return self.get_query_params().get('AndroidOpenType')

	def set_AndroidOpenType(self, AndroidOpenType):  # String
		self.add_query_param('AndroidOpenType', AndroidOpenType)
	def get_Title(self): # String
		return self.get_query_params().get('Title')

	def set_Title(self, Title):  # String
		self.add_query_param('Title', Title)
	def get_SmsDelaySecs(self): # Integer
		return self.get_query_params().get('SmsDelaySecs')

	def set_SmsDelaySecs(self, SmsDelaySecs):  # Integer
		self.add_query_param('SmsDelaySecs', SmsDelaySecs)
	def get_AndroidRenderStyle(self): # Integer
		return self.get_query_params().get('AndroidRenderStyle')

	def set_AndroidRenderStyle(self, AndroidRenderStyle):  # Integer
		self.add_query_param('AndroidRenderStyle', AndroidRenderStyle)
	def get_iOSExtParameters(self): # String
		return self.get_query_params().get('iOSExtParameters')

	def set_iOSExtParameters(self, iOSExtParameters):  # String
		self.add_query_param('iOSExtParameters', iOSExtParameters)
	def get_AndroidXiaomiImageUrl(self): # String
		return self.get_query_params().get('AndroidXiaomiImageUrl')

	def set_AndroidXiaomiImageUrl(self, AndroidXiaomiImageUrl):  # String
		self.add_query_param('AndroidXiaomiImageUrl', AndroidXiaomiImageUrl)
	def get_SmsTemplateName(self): # String
		return self.get_query_params().get('SmsTemplateName')

	def set_SmsTemplateName(self, SmsTemplateName):  # String
		self.add_query_param('SmsTemplateName', SmsTemplateName)
	def get_AndroidPopupBody(self): # String
		return self.get_query_params().get('AndroidPopupBody')

	def set_AndroidPopupBody(self, AndroidPopupBody):  # String
		self.add_query_param('AndroidPopupBody', AndroidPopupBody)
	def get_AndroidBigPictureUrl(self): # String
		return self.get_query_params().get('AndroidBigPictureUrl')

	def set_AndroidBigPictureUrl(self, AndroidBigPictureUrl):  # String
		self.add_query_param('AndroidBigPictureUrl', AndroidBigPictureUrl)
	def get_iOSSilentNotification(self): # Boolean
		return self.get_query_params().get('iOSSilentNotification')

	def set_iOSSilentNotification(self, iOSSilentNotification):  # Boolean
		self.add_query_param('iOSSilentNotification', iOSSilentNotification)
	def get_SendChannels(self): # String
		return self.get_query_params().get('SendChannels')

	def set_SendChannels(self, SendChannels):  # String
		self.add_query_param('SendChannels', SendChannels)
	def get_Target(self): # String
		return self.get_query_params().get('Target')

	def set_Target(self, Target):  # String
		self.add_query_param('Target', Target)
	def get_AndroidBigTitle(self): # String
		return self.get_query_params().get('AndroidBigTitle')

	def set_AndroidBigTitle(self, AndroidBigTitle):  # String
		self.add_query_param('AndroidBigTitle', AndroidBigTitle)
	def get_AndroidNotificationChannel(self): # String
		return self.get_query_params().get('AndroidNotificationChannel')

	def set_AndroidNotificationChannel(self, AndroidNotificationChannel):  # String
		self.add_query_param('AndroidNotificationChannel', AndroidNotificationChannel)
	def get_AndroidRemind(self): # Boolean
		return self.get_query_params().get('AndroidRemind')

	def set_AndroidRemind(self, AndroidRemind):  # Boolean
		self.add_query_param('AndroidRemind', AndroidRemind)
	def get_AndroidActivity(self): # String
		return self.get_query_params().get('AndroidActivity')

	def set_AndroidActivity(self, AndroidActivity):  # String
		self.add_query_param('AndroidActivity', AndroidActivity)
	def get_SmsSignName(self): # String
		return self.get_query_params().get('SmsSignName')

	def set_SmsSignName(self, SmsSignName):  # String
		self.add_query_param('SmsSignName', SmsSignName)
	def get_AndroidNotificationNotifyId(self): # Integer
		return self.get_query_params().get('AndroidNotificationNotifyId')

	def set_AndroidNotificationNotifyId(self, AndroidNotificationNotifyId):  # Integer
		self.add_query_param('AndroidNotificationNotifyId', AndroidNotificationNotifyId)
	def get_AppKey(self): # Long
		return self.get_query_params().get('AppKey')

	def set_AppKey(self, AppKey):  # Long
		self.add_query_param('AppKey', AppKey)
	def get_TargetValue(self): # String
		return self.get_query_params().get('TargetValue')

	def set_TargetValue(self, TargetValue):  # String
		self.add_query_param('TargetValue', TargetValue)
	def get_AndroidXiaoMiActivity(self): # String
		return self.get_query_params().get('AndroidXiaoMiActivity')

	def set_AndroidXiaoMiActivity(self, AndroidXiaoMiActivity):  # String
		self.add_query_param('AndroidXiaoMiActivity', AndroidXiaoMiActivity)
	def get_AndroidXiaoMiNotifyTitle(self): # String
		return self.get_query_params().get('AndroidXiaoMiNotifyTitle')

	def set_AndroidXiaoMiNotifyTitle(self, AndroidXiaoMiNotifyTitle):  # String
		self.add_query_param('AndroidXiaoMiNotifyTitle', AndroidXiaoMiNotifyTitle)
