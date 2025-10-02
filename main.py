static_params = {
            "viber_auth_token": "get_api_key_using_channel_developers_option"
            "sender_id": "If sender ID is not known, make need_sender_id as Yes; can make sender and reciever id as same if in same channel."
            "need_sender_id": "No"
        }
        
def send_viber_message(static_params):
    try:
        viber_channel_bot = SendViberAlert(viber_auth_token=static_params["viber_auth_token"], sender_id=static_params["sender_id"])
        super_admin_id = ""
        if static_params["need_sender_id"] == "yes":
            account_info = viber_channel_bot.get_viber_account_info()
            if account_info and account_info.get("status") == 0:
                for member in account_info['members']:
                    if (member.get('role') == "superadmin"):
                        super_admin_id = member.get('id')
                        print(f"  - Name: {member.get('name')}, Role: {member.get('role')}")
                        print("SuperAdmin id is", member.get('id'))
                viber_channel_bot = SendViberAlert(viber_auth_token=static_params["viber_auth_token"], sender_id=super_admin_id)
            else:
                return "Could not send Viber bot as superadmin Id could not be found", super_admin_id, False
            
#        message = make_viber_message(csv_file_name="final_data_report.csv")
        message = "Hello from Viber Automation" # Can make your custom message as string
        viber_channel_bot.send_message(message_content=message)
        return "Message sent", super_admin_id, True

    except Exception as e:
        print(f"Got exception in send_viber_message as: {str(e)}")
        return f"Got exception in send_viber_message as: {str(e)}", super_admin_id, False
