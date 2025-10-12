# viber_channel_with_python

A simple Python tool to send automated messages via the Viber Public Account API.
	•	Initiate the SendViberAlert class with Viber Authentication Token and sender Id.
	•	If Sender Id is unkown first call the method get_viber_account_info and while initiating the class give a dummy sender Id.
	•	Use send_message method to send the message in channel.
	•	Or use send_viber_message function with your message and initiate need_sender_id as "yes", if sender_id is unkown.

	

	PS: - The Viber authentication token is the channel authentication token of your viber channel.
