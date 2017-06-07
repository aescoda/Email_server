from flask import Flask
from flask_mail import Mail, Message
import os


app = Flask(__name__)

app.config['MAIL_SERVER'] = os.environ.get('MAIL_SERVER', None)
app.config['MAIL_PORT'] = os.environ.get('MAIL_PORT', None)
app.config['MAIL_USE_SSL'] = os.environ.get('MAIL_SSL', None)


mail = MAil(app)

@app.route('/email')
def email:
    message = Message('Hello', sender = os.environ.get('MAIL_USERNAME', None), recipients= alejandro.escoda.umh@gmail.com
    mail.send(message)
    return "",200

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(debug=True, port=port, host='0.0.0.0', threaded=True)

