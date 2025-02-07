import requests
from bs4 import BeautifulSoup

def search_artist_popularity(artist_name=None):
    if artist_name is None or artist_name == "":
        return {
            '百度': '不知名',
            '小红书': '不知名'
        }

    # Baidu search
    baidu_url = f"https://www.baidu.com/s?wd={artist_name}"
    baidu_response = requests.get(baidu_url)
    baidu_soup = BeautifulSoup(baidu_response.text, 'html.parser')
    baidu_results = len(baidu_soup.find_all('div', class_='result'))  # Count search results

    # Xiaohongshu search
    xiaohongshu_url = f"https://www.xiaohongshu.com/search_result?keyword={artist_name}"
    xiaohongshu_response = requests.get(xiaohongshu_url)
    xiaohongshu_soup = BeautifulSoup(xiaohongshu_response.text, 'html.parser')
    xiaohongshu_results = len(xiaohongshu_soup.find_all('div', class_='note-item'))  # Count search results

    # Determine popularity based on search results
    baidu_popularity = '小有名气' if baidu_results > 10000 else '不知名'
    xiaohongshu_popularity = '小有名气' if xiaohongshu_results > 500 else '不知名'

    return {
        '百度': baidu_popularity,
        '小红书': xiaohongshu_popularity
    }