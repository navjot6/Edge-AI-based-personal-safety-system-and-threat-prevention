from twilio.rest import Client
from database import get_db_connection

account_sid = "AC211ccacca597b0da98deb663df76b6f7"
auth_token = "aa50cf5bbd1e800afcc1d1fbc50e566e"
twilio_number = "+19342026474"
receiver_number = "+91XXXXXX3156`"

client = Client(account_sid, auth_token)
def send_alert(message):
    client.messages.create(
        body=message,
        from_=twilio_number,
        to=receiver_number
    )

    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO alerts(message) VALUES(%s)", (message,))
    db.commit()
    cursor.close()
    db.close()
