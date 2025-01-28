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
                
                output = {
                    'payload': {
                        'id': payload.get('id'),
                        'message_id': payload.get('message_id'),
                        'type': payload.get('type'),
                        'attachment': payload.get('attachment'),
                        'text': payload.get('text'),
                        'date': payload.get('date'),
                        'can_delete': payload.get('can_delete'),
                        'can_reaction': payload.get('can_reaction'),
                        'is_auto_response': payload.get('is_auto_response'),
                        'social_user_id': payload.get('social_user_id'),
                        'from': payload.get('from'),
                        'reactions': payload.get('reactions'),
                        'account_id': payload.get('account_id'),
                        'conversation_id': payload.get('conversation_id')
                    },
                    'account': {
                        'id': account.get('id'),
                        'identifier': account.get('identifier'), 
                        'name': account.get('name'),
                        'login_required': account.get('login_required'),
                        'can_send_direct': account.get('can_send_direct'),
                        'can_send_comment': account.get('can_send_comment'),
                        'can_send_post': account.get('can_send_post'),
                        'relogin_reason': account.get('relogin_reason'),
                        'created_at': account.get('created_at'),
                        'type': account.get('type'),
                        'profile_url': account.get('profile_url'),
                        'info': account.get('info'),
                        'automation_status': account.get('automation_status'),
                        'social_user_id': account.get('social_user_id')
                    }
                }
                f.write(json.dumps(output, indent=2))

            
        # Return a success response
        return jsonify({
            'status': 'success',
            'message': 'Webhook received and saved',
            'filename': filename
        }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)