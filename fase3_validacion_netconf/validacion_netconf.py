from ncclient import manager
import xml.dom.minidom

HOST = "192.168.56.103"
PORT = 830
USER = "cisco"
PASSWORD = "cisco123!"

netconf_filter = """
<filter>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname/>
  </native>
</filter>
"""

with manager.connect(
    host=HOST,
    port=PORT,
    username=USER,
    password=PASSWORD,
    hostkey_verify=False,
    device_params={"name": "csr"},
    allow_agent=False,
    look_for_keys=False
) as m:

    print("=" * 50)
    print("Conectado correctamente mediante NETCONF")
    print("=" * 50)

    respuesta = m.get_config("running", netconf_filter)

    xml = xml.dom.minidom.parseString(str(respuesta))

    print(xml.toprettyxml())
