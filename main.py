from flask import Flask, request, jsonify
import asyncio
from shazam import get_song_info
import json
import glob
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    # Get list of webhook data files
    files = sorted(glob.glob('webhook_data_*.txt'))
    
    if not files:
        return "No webhook data files found"
        
    # Read the most recent file
    with open(files[-1], 'r') as f:
        content = f.read()
        
    return f"Latest webhook data:\n\n{content}"

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Get the JSON data from the webhook
        data = request.json
        
        # Print the received data
        print('Received webhook data:', data)
        
        # Save webhook data to a text file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'webhook_data_{timestamp}.txt'
        
        with open(filename, 'w') as f:
            # Write payload and account data from body
            if 'body' in data and 'payload' in data['body']:
                payload = data['body']['payload']
                account = payload.get('account', {})
                # Extract payload fields
                payload_id = payload.get('id')
                message_id = payload.get('message_id')
                msg_type = payload.get('type')
                attachment = payload.get('attachment')
                text = payload.get('text')
                date = payload.get('date')
                can_delete = payload.get('can_delete')
                can_reaction = payload.get('can_reaction')
                is_auto_response = payload.get('is_auto_response')
                social_user_id = payload.get('social_user_id')
                msg_from = payload.get('from')
                reactions = payload.get('reactions')
                account_id = payload.get('account_id')
                conversation_id = payload.get('conversation_id')

                # Extract account fields
                acc_id = account.get('id')
                identifier = account.get('identifier')
                name = account.get('name')
                login_required = account.get('login_required')
                can_send_direct = account.get('can_send_direct')
                can_send_comment = account.get('can_send_comment')
                can_send_post = account.get('can_send_post')
                relogin_reason = account.get('relogin_reason')
                created_at = account.get('created_at')
                acc_type = account.get('type')
                profile_url = account.get('profile_url')
                info = account.get('info')
                automation_status = account.get('automation_status')
                acc_social_user_id = account.get('social_user_id')

                # Write variables line by line
                f.write(f"Payload ID: {payload_id}\n")
                f.write(f"Message ID: {message_id}\n")
                f.write(f"Message Type: {msg_type}\n")
                f.write(f"Attachment: {attachment}\n")
                f.write(f"Text: {text}\n")
                f.write(f"Date: {date}\n")
                f.write(f"Can Delete: {can_delete}\n")
                f.write(f"Can Reaction: {can_reaction}\n")
                f.write(f"Is Auto Response: {is_auto_response}\n")
                f.write(f"Social User ID: {social_user_id}\n")
                f.write(f"From: {msg_from}\n")
                f.write(f"Reactions: {reactions}\n")
                f.write(f"Account ID: {account_id}\n")
                f.write(f"Conversation ID: {conversation_id}\n")
                f.write("\nAccount Information:\n")
                f.write(f"Account ID: {acc_id}\n")
                f.write(f"Identifier: {identifier}\n")
                f.write(f"Name: {name}\n")
                f.write(f"Login Required: {login_required}\n")
                f.write(f"Can Send Direct: {can_send_direct}\n")
                f.write(f"Can Send Comment: {can_send_comment}\n")
                f.write(f"Can Send Post: {can_send_post}\n")
                f.write(f"Relogin Reason: {relogin_reason}\n")
                f.write(f"Created At: {created_at}\n")
                f.write(f"Account Type: {acc_type}\n")
                f.write(f"Profile URL: {profile_url}\n")
                f.write(f"Info: {info}\n")
                f.write(f"Automation Status: {automation_status}\n")
                f.write(f"Account Social User ID: {acc_social_user_id}\n")

            
        # Return a success response
        return jsonify({
            'status': 'success',
            'message': 'Webhook received and saved',
            'filename': filename
        }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)