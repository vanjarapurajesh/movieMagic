from flask import Flask
import boto3
from app.routes import bp as routes_bp

# === AWS Configuration ===
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
users_table = dynamodb.Table("MovieMagic_Users")
bookings_table = dynamodb.Table("MovieMagic_Bookings")

sns = boto3.client('sns', region_name="us-east-1")
sns_topic_arn = 'arn:aws:sns:us-east-1:905418361023:MovieTicketNotifications:1ed3a6e8-ba7a-4aef-bd09-2bf67d3b25b9'

# === Flask Application Setup ===
app = Flask(__name__)
app.secret_key = 'supersecretkey'
app.register_blueprint(routes_bp)

# === Run the Flask App ===
if __name__ == '__main__':
    app.run(debug=True)
