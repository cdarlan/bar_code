from barcode import EAN13 #import o padrão de codigo de barra EAN13
from barcode.writer import ImageWriter #para gerar o cod barra em imagem .png

codigo_produtos = {
    'Feijao': '551746511111',
    'Arroz': '665789011111',
    'Macarrao': '665887111111',
    'Azeite': '998556211111'}

for produto in codigo_produtos:
    codigo = codigo_produtos[produto]
    codigo_barra = EAN13 (codigo, writer=ImageWriter())  
    codigo_barra.save(f'codigo_barra_{produto}')
    