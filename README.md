# viber_channel_with_python

A simple Python tool to send automated messages via the Viber Public Account API. <br>
	•	Initiate the SendViberAlert class with Viber Authentication Token and sender Id. <br>
	•	If Sender Id is unkown first call the method get_viber_account_info and while initiating the class give a dummy sender Id. <br>
	•	Use send_message method to send the message in channel. <br> <br>
	•	Or use send_viber_message function with your message and initiate need_sender_id as "yes", if sender_id is unkown.
	
•	In case of having a proxy, pass proxies = {"https": "http://proxy_ip"} and pass it while calling requests.post method.

	
	
	PS: - The Viber authentication token is the channel authentication token of your viber channel.
