from twilio.rest import Client
import database_interaction
import
# Your Account Sid and Auth Token from twilio.com/console
class Message:
    ACCOUNT_SID = 'ACb77c89f64c5ce3be57484c2b2ddf0e1d'
    AUTH_TOKEN = '8fa22daceff8e23d181efc73e1312d69'
    MOBILE_NUMBER = '+17722131082'
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    def __init__(self):
        self.body = ""
        self.recieved_from = ""
        self.to_sent = ""
    
    def fill_content(self,response):
        self.body = response['Body']
        self.recieved_from = response['From']
        self.process_message()

    def process_message(self):
        data = self.body.split("#$#$#")

        if not data[0]:
            data = data[1:] 
            location = data[0].split(',')
            no_of_people = data[1]
            database_data = {'lattitude':location[0],'longitude':location[1]}
            database_data['no_of_people'] = no_of_people
            database_data['mo_number'] = self.recieved_from
            database_interaction.insert("AffectedPeople", **database_data)

            self.inform_other_person()

    #print(message.sid)
