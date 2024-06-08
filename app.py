from flask import Flask, redirect, request, session, url_for
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'YOUR_REDIRECT_URI'

@app.route('/')
def home():
    return '<a href="/login">Login with Discord</a>'

@app.route('/login')
def login():
    discord_login_url = f'https://discord.com/api/oauth2/authorize?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&response_type=code&scope=identify'
    return redirect(discord_login_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'scope': 'identify'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    r = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
    r.raise_for_status()
    access_token = r.json().get('access_token')
    session['token'] = access_token
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    token = session.get('token')
    if not token:
        return redirect(url_for('login'))

    headers = {
        'Authorization': f'Bearer {token}'
    }
    r = requests.get('https://discord.com/api/users/@me', headers=headers)
    user_info = r.json()
    return f"Logged in as {user_info['username']}#{user_info['discriminator']}"

if __name__ == "__main__":
    app.run(debug=True)
