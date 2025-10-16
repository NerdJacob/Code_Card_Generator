import PIL
from PIL import Image, ImageDraw, ImageFont
import qrcode
import os

list_of = 'FAKE_CODE '
codes = list_of.split(' ')
itteration = 1
folder = os.path.dirname(__file__)

def make_QR_code(code):
    qr_code = qrcode.make(f'https://store.pokemongo.com/offer-redemption?passcode={code}')
    qr_code = qr_code.resize((248,248))
    return qr_code

def add_to_card(code):
    qr_code = make_QR_code(code)
    card = Image.new('RGB', (500, 250), (0,0,0)) # full card, black    
    frame = Image.new('RGB', (498, 248), (255,255,255)) # white space
    #card.paste(frame,(1,1)) # past in the white space, leaving only the thin border
    card_body = Image.open(f"{folder}/card_template.png", 'r')
    card.paste(card_body,(1,1))
    card.paste(qr_code,(250,1))
    writing = ImageDraw.Draw(card)
    font = ImageFont.load_default(size=25)
    text_color = (0,0,0)
    #writing.text((20,20),f'{code}\n\n1 Premium Battle Pass\n1 Incubator\n1 Star Piece\n1 Lure',text_color,font=font)
    writing.text((20,100),f'{code}',text_color,font=font)
    return card

for code in codes:
    card = add_to_card(code)
    card.save(f'{folder}/code_cards/card{itteration:03}.png')
    itteration += 1
print('Cards created.')
