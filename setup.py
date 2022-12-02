import os

token = token = os.environ.get('token') #testing/production

# key = Fernet.generate_key()
key = token = os.environ.get('key')

airtablekey = token = os.environ.get('airtablekey')

devTGid = token = os.environ.get('devTGid')