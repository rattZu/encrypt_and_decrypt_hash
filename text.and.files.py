import requests
from bs4 import BeautifulSoup





#########################################################################################################
url = 'https://br.freepik.com/vetores-premium/logo-cf_29998204.htm' 
#########################################################################################################






headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


response = requests.get(url, headers=headers)
if response.status_code != 200:
    raise Exception(f'Falha na solicitação: {response.status_code}')


soup = BeautifulSoup(response.text, 'html.parser')


texts = [element.get_text(strip=True) for element in soup.find_all(['h1', 'h2', 'h3', 'p'])]
images = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs]


with open('output.html', 'w', encoding='utf-8') as file:
    file.write('<!DOCTYPE html>\n')
    file.write('<html lang="en">\n')
    file.write('<head>\n')
    file.write('<meta charset="UTF-8">\n')
    file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    file.write('<title>Extracted Content</title>\n')
    file.write('<style>\n')
    file.write('body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }\n')
    file.write('header { background-color: #333; color: #fff; padding: 15px; text-align: center; }\n')
    file.write('.container { max-width: 1200px; margin: auto; padding: 20px; }\n')
    file.write('.grid-container { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 15px; }\n')
    file.write('.grid-item { background: #fff; border: 1px solid #ddd; padding: 15px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); }\n')
    file.write('img { max-width: 100%; height: auto; border-radius: 8px; }\n')
    file.write('.close-btn { position: fixed; top: 20px; right: 20px; padding: 10px 20px; background-color: #f44336; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px; }\n')
    file.write('</style>\n')
    file.write('</head>\n')
    file.write('<body>\n')
    file.write('<header>\n')
    file.write('<h1>Extracted Content from Cokidoo</h1>\n')
    file.write('</header>\n')
    file.write('<button class="close-btn" onclick="window.close()">Close</button>\n')
    file.write('<div class="container">\n')
    file.write('<div class="grid-container">\n')


    for text in texts:
        file.write(f'<div class="grid-item"><p>{text}</p></div>\n')


    for img_url in images:
        if not img_url.startswith('http'):
            img_url = requests.compat.urljoin(url, img_url)  
        file.write(f'<div class="grid-item"><img src="{img_url}" alt="Extracted Image"></div>\n')

    file.write('</div>\n')
    file.write('</div>\n')
    file.write('</body>\n')
    file.write('</html>\n')

print('HTML file created successfully:: output.html')
