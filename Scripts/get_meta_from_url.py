from requests.sessions import session
import re
from time import sleep
import bs4
import csv
from fake_useragent import UserAgent

user_agent = UserAgent()
all_genres = {}
all_themes = {}
all_years = {}
genres_count = 0
themes_count = 0
years_count = 0
regexp_title = r'Смотреть (.*) все серии.*'
regexp_original = r'.*: (.*)'
regexp_clear = r' и '
regexp_img = r".*: url\('(.*)'\).*"

sess = session()

with open('../Data/urls.txt', 'r') as f:
    urls = list(map(str.rstrip, f.readlines()))


def save_img(url, id):
    img = sess.get(url, headers={'User-Agent': user_agent.random}).content
    with open(f'../Data/images/{id}.jpg', 'wb') as f:
        f.write(img)


def add_to_log(**kwargs):
    if 'error' not in kwargs:
        message = f"""Request #{kwargs['id']} done!
Name RU: {kwargs['name']}
Genres: {', '.join(kwargs['genres'])}
Themes: {', '.join(kwargs['themes'])}
Years: {', '.join(kwargs['years'])}
Original name: {kwargs['orig_name']}
Image URL: {kwargs['img_url']}
Description: {kwargs['description']}

------------------------------------------

"""
    else:
        message = f"""ERRRRRRROOOOOOOOORRRRRRRR!1!111!! - {kwargs['id']}:{kwargs['error']}

------------------------------------------

"""
    with open('../Data/log.txt', 'a', encoding='utf-8') as f:
        f.write(message)


def add_to_csv(id, ru_name, genres_ids, themes_ids, years_ids, orig_name, description):
    with open('../Data/data.csv', 'a', encoding='utf-8', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(
            [id, ru_name, ' '.join(genres_ids), ' '.join(themes_ids), ' '.join(years_ids), orig_name, description])


def get_genres_ids(genres):
    global genres_count
    out = []
    for genre in genres:
        if genre not in all_genres:
            all_genres[genre] = str(genres_count)
            genres_count += 1
        out.append(all_genres[genre])
    return out


def get_themes_ids(themes):
    global themes_count
    out = []
    for theme in themes:
        if theme not in all_themes:
            all_themes[theme] = str(themes_count)
            themes_count += 1
        out.append(all_themes[theme])
    return out


def get_years_ids(years):
    global years_count
    out = []
    for year in years:
        if year not in all_years:
            all_years[year] = str(years_count)
            years_count += 1
        out.append(all_years[year])
    return out


for id, url in enumerate(urls):
    try:
        req = sess.get(url, headers={'User-Agent': user_agent.random})
        soup = bs4.BeautifulSoup(req.content, 'lxml')

        data_bad = soup.find('div',
                             attrs={'class': ('under_video_additional', 'the_hildi')}
                             ).text.replace('Аниме ', '').strip().split('.')
        data = {}
        for param in data_bad:
            if 'Жанр' in param:
                data['жанр'] = param
            elif 'Год' in param:
                data['годы'] = param
            elif 'Тем' in param:
                data['темы'] = param
            elif 'названи' in param:
                data['название'] = param

        genres_bad = re.sub(regexp_clear, ', ', data['жанр'])
        years_bad = data['годы']
        if 'темы' in data:
            themes_bad = re.sub(regexp_clear, ', ', data['темы'])
            themes = themes_bad[themes_bad.index(':') + 2:].split(', ')
        else:
            themes = '-'

        genres = genres_bad[genres_bad.index(':') + 2:].split(', ')
        years = years_bad[years_bad.index(':') + 2:].split(', ')
        orig_name = re.findall(regexp_original, data['название'])[0]
        name_ru = re.findall(regexp_title, soup.title.text)[0]
        description = ''.join([(str(i) if type(i) != bs4.element.Tag else i.text) for i in
                               soup.find('p', attrs={'class': ('under_video', 'the_hildi')}).span if i.name != 'i'])
        img_url = re.findall(regexp_img, soup.find('div', {'class': 'all_anime_title'})['style'])[0]

        add_to_csv(id, name_ru, get_genres_ids(genres), get_themes_ids(themes), get_years_ids(years), orig_name,
                   description)
        sleep(4)

        save_img(img_url, id)

        sleep(4)
    except Exception as e:
        add_to_log(error=e, id=id)
        continue
    else:
        add_to_log(id=id, name=name_ru, genres=genres, themes=themes, years=years, orig_name=orig_name,
                   img_url=img_url, description=description)
    finally:
        print(f"Request #{id} done!")

with open('../Data/genres.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for i in all_genres.items():
        writer.writerow((i[0], int(i[1])))

with open('../Data/themes.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for i in all_themes.items():
        writer.writerow((i[0], int(i[1])))

with open('../Data/years.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for i in all_years.items():
        writer.writerow((int(i[0]), int(i[1])))
