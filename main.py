from flask import Flask, request, jsonify

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
        data = request.json
        
        # Print the received data
        print('Received webhook data:', data)
        
        # Save webhook data to a text file
        import json
        from datetime import datetime
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'webhook_data_{timestamp}.txt'
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
        # Return a success response
        return jsonify({
            'status': 'success', 
            'message': 'Webhook received and saved',
            'filename': filename
        }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)