from requests.sessions import session
from bs4 import BeautifulSoup
from time import sleep

out = []
user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36'

sess = session()

for i in range(1, 22):
    req = sess.get(f'https://jut.su/anime/page-{i}/',
                   headers={
                       'User-Agent': user_agent,
                   })
    print(f'Request #{i} done!')
    soup = BeautifulSoup(req.content, 'lxml')
    out.extend(['https://jut.su' + i.a['href'] for i in soup.find_all('div', attrs={'class': "all_anime_global"})])

    sleep(5)

with open('../Data/urls.txt', 'w') as f:
    f.write('\n'.join(out))
