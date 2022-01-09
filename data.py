import os
import sys
import csv
import json
import datetime
from pprint import pprint


path_data_json = "data.json"
cors_header = {
    'Access-Control-Allow-Origin': "http://localhost:3000",
}


def query(url):
    api = tweepy.Client(**secret)
    data = api.get_tweet(url.split('/')[-1],
        expansions=["author_id", "attachments.media_keys"],
        user_fields=["profile_image_url"],
        tweet_fields=["created_at", "entities"],
        media_fields=["url"])

    return {
        'query_url': url,
        'user_name': data.includes['users'][0].data['name'],
        'user_id': data.includes['users'][0].data['username'],
        'user_image': data.includes['users'][0].data['profile_image_url'],
        'text': data.data.text,
        'image': [img.data['url'] for img in data.includes['media']],
        'url': data.data.entities['urls'][0]['url'],
        'create_at': data.data.created_at.isoformat(),
    }


def updateDB(tw_type, url, force=False):
    data = {}
    if not os.path.exists(path_data_json):
        json.dump({}, open(path_data_json, 'w'))
    else:
        data = json.load(open(path_data_json))

    if tw_type not in data:
        data[tw_type] = []

    url_map = {d.get('query_url'): i for i, d in enumerate(data[tw_type])}
    if url in url_map and not force:
        print(f"Skip {url}")
        return 

    if url in url_map:
        print(f"Update {url}")
        data[tw_type][url_map[url]] = query(url)
    else:
        print(f"insert {url}")
        data[tw_type].append(query(url))
    json.dump(data, open(path_data_json, 'w'))


def getTweets(tw_type):
    if tw_type:
        data = json.load(open(path_data_json)).get(tw_type, [])
    else:
        data = []
    if data:
        data = sorted(data, key=lambda i: i['create_at'])
    return data


async def getTweetsJson(request):
    name = request.match_info.get('tw_type', "")
    data = getTweets(name)
    return web.json_response(data, headers=cors_header)


async def getTweetsJsonExample(request):
    data = [
        {'create_at': datetime.datetime(2021, 11, 30, 3, 2, 12, tzinfo=datetime.timezone.utc).isoformat(),
         'image': ['https://pbs.twimg.com/media/FFaPX47acAA66ix.png'],
         'text': '【廢】\n不知道啦 如果九壹是蘿莉之類的 https://t.co/6X6RGhHPWI',
         'url': 'https://t.co/6X6RGhHPWI',
         'user_id': 'adsl6658',
         'user_image': 'https://pbs.twimg.com/profile_images/1453399851886993415/p-dXd5rQ_normal.jpg',
         'user_name': 'LOS'},
        {'create_at': datetime.datetime(2021, 11, 30, 4, 2, 5, tzinfo=datetime.timezone.utc).isoformat(),
         'image': ['https://pbs.twimg.com/media/FFadHRhaQAA2OJy.png'],
         'text': '91不要討厭我 https://t.co/KE5ssopoEO https://t.co/aNJLjKkGDW',
         'url': 'https://t.co/KE5ssopoEO',
         'user_id': 'zzz_2605',
         'user_image': 'https://pbs.twimg.com/profile_images/1457965328458469376/ilqVrjsT_normal.jpg',
         'user_name': '歷曆歷🪐現在要多畫畫'},
        {'create_at': datetime.datetime(2021, 11, 30, 16, 35, 44, tzinfo=datetime.timezone.utc).isoformat(),
         'image': ['https://pbs.twimg.com/media/FFdJrIaaQAAby4r.jpg'],
         'text': '大家有畫過的都是共犯我們裡面見QwQ\n'
                 '#玖要在依起 https://t.co/aWLSmym41r https://t.co/SpMIQZC2Y7',
         'url': 'https://t.co/aWLSmym41r',
         'user_id': 'miziquan_naiali',
         'user_image': 'https://pbs.twimg.com/profile_images/1413456490518614019/cYZGVUrX_normal.jpg',
         'user_name': '米自犬'},
    ]
    return web.json_response(data, headers=cors_header)


if __name__ == "__main__":
    if sys.argv[1] == "fetch":
        from twitter_secret import secret
        import tweepy
        reader = csv.DictReader(open("data.csv"))
        for i in reader:
            updateDB(i['tw_type'], i['url'])
    elif sys.argv[1] == "server":
        from aiohttp import web
        app = web.Application()
        app.add_routes([web.post('/api/{tw_type}', getTweetsJson)])
        # app.add_routes([web.post('/api/{tw_type}', getTweetsJsonExample)])
        web.run_app(app, port=8081)
    elif sys.argv[1] == "export":
        data = getTweets(sys.argv[2])
        print(json.dumps(data))
    else:
        print("Error")
