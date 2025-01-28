from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Hamravesh!"

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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)