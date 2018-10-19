from twilio.rest import Client
import database_interaction
import GoogleMapsInteraction

# Your Account Sid and Auth Token from twilio.com/console
class Message:
    ACCOUNT_SID = 'ACb77c89f64c5ce3be57484c2b2ddf0e1d'
    AUTH_TOKEN = '8fa22daceff8e23d181efc73e1312d69'
    MOBILE_NUMBER = '+17722131082'
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    seperator = "####"

    def __init__(self, body="", to_sent="", recieved_from=""):
        self.body = body
        self.recieved_from = ""
        self.to_sent = to_sent

    def fill_content(self,response):
        self.body = response['Body']
        self.recieved_from = response['From']
        self.process_message()

    def inform_other_person(self):
        emergency_contact = database_interaction.get_emergency_contact(self.recieved_from)
        self.body = database_interaction.get_name_location( self.recieved_from)
        self.to_sent = emergency_contact
        self.send_message()

    def send_message(self):
        message = Message.client.messages\
                        .create(body = self.body,
                                from_ = Message.MOBILE_NUMBER,
                                to = self.to_sent
                            )
        print(message.sid)

    def process_message(self):
        data = self.body.split(Message.seperator)
        longitude = ""
        lattitude = ""
        number_of_persons = ""
        if not data[0]:
            data = data[1:] 
            location = data[0].split(",")
            lattitude = location[0]
            longitude = location[1]
            number_of_persons = data[1]
            self.inform_other_person()
            
        else:
            location_text = data[0]
            maps = GoogleMapsInteraction.GoogleMaps
            lattitude, longitude = maps.getLatLngFromText(location_text)
            number_of_persons = data[1]
        
        database_data = {'lattitude':lattitude,'longitude':longitude}
        database_data['number_of_persons'] = number_of_persons
        database_data['mobile_number'] = self.recieved_from
        database_interaction.insert("affected_people", **database_data)

    #print(message.sid)
