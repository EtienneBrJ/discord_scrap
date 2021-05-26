from bs4 import BeautifulSoup
import requests

def get_crypto_price(coin):
  #Get the URL
  url = 'https://coinmarketcap.com/currencies/'+coin+'/'
  #Make a request to the website
  HTML = requests.get(url)
  #Parse the HTML
  soup = BeautifulSoup(HTML.text, 'html.parser')
  #Find the current price
  text = soup.find('div', attrs={'class':'priceValue___11gHJ'})

  return remove_html_markup(text)

def remove_html_markup(s):

  tag = False
  quote = False
  out = ""

  for c in s:
    if c == '<' and not quote:
      tag = True
    elif c == '>' and not quote:
      tag = False
    elif (c == '"' or c == "'") and tag:
      quote = not quote
    elif not tag:
      out = out + c

  return out