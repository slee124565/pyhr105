
import os
import json
import click
from cryptography.fernet import Fernet
import logging.config as logging_config
from hr105 import config

logging_config.dictConfig(config.logging_config)
GMAIL_MSG_FOLDER = os.getenv('GMAIL_MSG_FOLDER', '.gmail')


class KeyManager:
    key_file = 'secret.key'
    secret_file = 'secret'
    def generate_key(self):
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as fh:
            fh.write(key)

    def load_key(self):
        return open(self.key_file, 'rb').read()

    def encrypt_data(self, data):
        f = Fernet(self.load_key())
        return f.encrypt(data.encode())

    def decrypt_data(self, encrypted):
        f = Fernet(self.load_key())
        return f.decrypt(encrypted).decode()

    def save_secret(self, secret):
        with open(self.secret_file, 'wb') as fh:
            fh.write(self.encrypt_data(secret))

    def load_secret(self):
        with open(self.secret_file, 'r') as fh:
            secret = self.decrypt_data(fh.read())
        return secret

@click.group()
def hr105cli():
    """
    HR105 CLI Group Command.
    """
    pass

@click.command(name='login')
@click.argument('username')
@click.argument('password')
def hr105_login(username, password):
    # key management
    _mgt = KeyManager()
    if not os.path.exists(_mgt.key_file):
        _mgt.generate_key()
    if not os.path.exists(_mgt.secret_file):
        _mgt.save_secret(json.dumps({'username': f'{username}', 'password':f'{password}'}))

    # 登入邏輯
    pass


# Adding commands to the group
hr105cli.add_command(hr105_login)

if __name__ == '__main__':
    hr105cli()
