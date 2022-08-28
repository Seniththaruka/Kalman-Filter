from firebase import firebase
from Crypto.PublicKey import RSA


ibus = firebase.FirebaseApplication('https://ibus-a5b0f-default-rtdb.firebaseio.com/', None)

result = ibus.get('/location', None)

print(result)
