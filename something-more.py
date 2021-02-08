from pyshorteners import Shortener
access_token = "token-here"  # get the token from https://bitly.is/accesstoken
link = input("Enter the short link to get more info:")
client = Shortener(api_key=access_token)
print(f"Original Link: {client.bitly.expand(link)}\n"  # get more info here--> https://bit.ly/shorteners-info
      f"Short Link: {link}\n"
      f"Total number of clicks = {client.bitly.total_clicks(link)}")
