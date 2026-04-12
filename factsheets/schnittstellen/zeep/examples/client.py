import zeep
import os

wsdl_path = os.path.join(os.path.dirname(__file__), 'service.wsdl')
client = zeep.Client(wsdl=wsdl_path)

# In einer echten Umgebung würde man hier einen Call absetzen
# client.service.GetLastTradePrice(tickerSymbol='AAPL')

print("Zeep client initialized successfully with WSDL.")
