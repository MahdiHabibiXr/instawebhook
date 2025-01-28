from flask import Flask, request, jsonify
import asyncio
from shazam import get_song_info

app = Flask(__name__)

@app.route("/")
def home():
    # Get list of webhook data files
    import glob
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
        data = request.json  # Get the raw JSON data
        
        # Handle both single object and list formats
        if isinstance(data, list):
            data = data[0]  # Get first item if it's a list
        
        # Extract the required fields
        webhook_type = data.get('type')
        user_id = data.get('user_id') 
        payload = data.get('payload')
        social_user = data.get('body', {}).get('socialUser')
        
        # Print the extracted data
        print('Webhook type:', webhook_type)
        print('User ID:', user_id)
        print('Payload:', payload)
        print('Social User:', social_user)
        
        # Save extracted data to a text file
        import json
        from datetime import datetime
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'webhook_data_{timestamp}.txt'
        
        extracted_data = {
            'type': webhook_type,
            'user_id': user_id,
            'payload': payload,
            'socialUser': social_user
        }
        
        with open(filename, 'w') as f:
            json.dump(extracted_data, f, indent=2)
            
        # Return a success response with extracted data
        return jsonify({
            'status': 'success',
            'message': 'Webhook data extracted and saved',
            'filename': filename,
            'extracted_data': extracted_data
        }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)