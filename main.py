from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        # Get the JSON data from the webhook
        data = request.json
        
        # Print the received data
        print('Received webhook data:', data)
        
        # Process the webhook data here
        # Add your custom logic to handle the data
        
        # Return a success response
        return jsonify({'status': 'success', 'message': 'Webhook received'}), 200

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(debug=True, port=5000)