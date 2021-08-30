# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 15:46:34 2021

@author: DELL E7440
"""


import json
from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('h9uAPFXD5H2hAq8Y1TgG_wSzjs5j0GG1tutBM5tX6Pok')
assistant = AssistantV2(
    version='2021-06-14',
    authenticator = authenticator
)

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com')

response=assistant.create_session(
    assistant_id='78da2c17-9bc3-40c2-bb82-5c1b71df54a9'
    ).get_result()

session_id=response
session_id=session_id["session_id"]
print(type(session_id))
print(session_id)

while True:
    input_text=input('enter the text:')
    

    response = assistant.message(
        assistant_id='78da2c17-9bc3-40c2-bb82-5c1b71df54a9',
        session_id=session_id,
        input={
             'message_type':'text',
            'text': input_text
        }
    ).get_result()
    print(response['output']['generic'][0]['text'])
