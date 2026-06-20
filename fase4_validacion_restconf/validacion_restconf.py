import requests
import json

HOST = "192.168.56.103"
USER = "cisco"
PASSWORD = "cisco123!"

url = f"https://{HOST}/restconf/data/Cisco-IOS-XE-native:native/hostname"

headers = {
    "Accept": "application/yang-data+json"
}

respuesta = requests.get(
    url,
    auth=(USER, PASSWORD),
    headers=headers,
    verify=False
)

print("=" * 50)
print("Código HTTP:", respuesta.status_code)
print("=" * 50)

if respuesta.ok:
    print(json.dumps(respuesta.json(), indent=4))
else:
    print(respuesta.text)
