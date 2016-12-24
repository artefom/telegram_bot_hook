from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

BOT_TOKEN = '308125138:AAFltHYK_wgKgSmxMzgCC60UL7Er1D14jlE'
BASE_URL = 'https://api.telegram.org/bot' + BOT_TOKEN + '/'

@app.route('/bot/set_webhook')
def set_webhook():
    url = request.args.get('url', '')
    return json.dumps(json.load(urllib2.urlopen(BASE_URL + 'setWebhook', urllib.urlencode({'url': url}))))

if __name__ == '__main__':
    app.run()
