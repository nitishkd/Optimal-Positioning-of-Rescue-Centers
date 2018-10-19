from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import message
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()
    recieved_message = message.Message()
    recieved_message.fill_content(request.values)
    resp.message("Thanks so much for your message. Stay Strong. We will remain in touch")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)