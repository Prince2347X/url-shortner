from pyshorteners import Shortener
access_token = "token-here"  # get the token from https://bitly.is/accesstoken
long_url = input("Enter the long link:")
client = Shortener(api_key=access_token)
print(client.bitly.short(long_url))
