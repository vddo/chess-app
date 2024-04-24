import berserk

with open('./lichess.token') as f:
    token = f.read()
    f.close

lines = token.split('\n')
API_TOKEN = lines[0]

session = berserk.TokenSession(API_TOKEN)
client = berserk.Client(session=session)

print(client.account.get())