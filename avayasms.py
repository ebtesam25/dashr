
sid = 'AC400001a05f6b9e61eee1478bab95562c'
authToken = '319f970ef9f14f87b5739459a91acddc'


from datetime import date
from zang.exceptions.zang_exception import ZangException
from zang.configuration.configuration import Configuration
from zang.connectors.connector_factory import ConnectorFactory
from credentials import sid, authToken

url = 'https://api-us.cpaas.avayacloud.com/v2'

configuration = Configuration(sid, authToken, url=url)
smsMessagesConnector = ConnectorFactory(configuration).smsMessagesConnector
mmsMessagesConnector = ConnectorFactory(configuration).mmsMessagesConnector
# send sms message

def sendSms(tonum, text):

    try:
        smsMessage = smsMessagesConnector.sendSmsMessage(
            # to='1(571) 490-1702',
            to = tonum,
            # body='Hello from Avaya Engage 2021',
            body = text,
            from_='1(618) 620-0301',
            statusCallback='callback.url')
        view = vars(smsMessage)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
    except ZangException as e:
        print("in exception")
        print(e)
        
    
    
# send mms message

def sendMms(tonum, text, media):

    try:
        mmsMessage = mmsMessagesConnector.sendMmsMessage(
            # to='1(571) 490-1702',
            to = tonum,
            # mediaUrl="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Avaya_Logo.svg/1200px-Avaya_Logo.svg.png",
            mediaUrl = media,
            # body='Hello from Avaya Engage 2021',
            body = text,
            from_='1(618) 620-0301',
            statusCallback='callback.url')
        view = vars(mmsMessage)
        print('\n')
        for item in view:
            print (item , ' : ' , view[item])
    except ZangException as e:
        print("in exception")
        print(e)



# # view sms message
# try:
#     smsMessage = smsMessagesConnector.viewSmsMessage(smsMessage.sid)
#     print(smsMessage.status)
# except ZangException as e:
#     print(e)


##TESTING
##sendSms('15714901702', 'testing dashacam')

