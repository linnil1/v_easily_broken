# EasilyBroken

## Setup
```bash
yarn install
```


## Data
I save our data in worker KV, so no database is used in this project

Here is the pipeline

1. Create a twitter list

``` csv
tw_type,url
91,https://twitter.com/adsl6658/status/1465516485590204417
91,https://twitter.com/zzz_2605/status/1465531552616484872
91,https://twitter.com/toritodori1/status/1465521877607063552
los,https://twitter.com/Kyuuichi0091/status/1467079202197635073
both,https://twitter.com/justdcfun1332/status/1467119400994340867
```

2. save tweets into json

Set your twitter token here
`twitter_secret.py`
``` python
secret = {
    'access_token': "",
    'access_token_secret': "",
    'bearer_token': "",
}
```

And fetch the tweets
`python3 data.py fetch`

3. create a namespace(setup once)

Create a namespace
``` bash
wrangler kv:namespace create easily_broken
```

And write down the id and binding name in `wrangler.toml`
``` toml
[[kv_namespaces]]
binding = "easily_broken"
id = "2cb0c22e60f74dba90e4156ec8050e61"
```

3. Push data to KV
```
wrangler kv:key put --binding easily_broken 91 "$(python3 data.py export 91)"
wrangler kv:key put --binding easily_broken los "$(python3 data.py export los)"
wrangler kv:key put --binding easily_broken both "$(python3 data.py export both)"
wrangler kv:key put --binding easily_broken articles "$(python3 data.py export articles)"
```

## Development

```bash
yarn dev                # port 3000
python3 data.py server  # port 8081
```

Though you can change this

1. If you don't want to use twitter api
`data.py#111`
``` python
# app.add_routes([web.post('/api/{tw_type}', getTweetsJson)])
app.add_routes([web.post('/api/{tw_type}', getTweetsJsonExample)])
```

2. If you don't want to use kv
`page/*vue`
``` javascript
var { data: tweets } = await useFetch('/api/query_kv_test/91', {method: "POST"})
// var { data: tweets } = await useFetch('/api/query_kv/91', {method: "POST"})
```
`server/api/query_kv_test.ts`
``` javascript
const url = "http://localhost:8081/api" + req.url
```

3. If you don't want to use Fetch
`page/*vue`
``` javascript
// async setup() {
async setup_remove_this_function() {
```


## Production

Build the application for production:

```bash
yarn build
wrangler publish
```

Note, `GET` works, `POST` not work, WHY?
``` javascript
var { data: tweets } = await useFetch('/api/query_kv_test/91', {method: "GET"})
// var { data: tweets } = await useFetch('/api/query_kv/91', {method: "POST"})
```


# 文件
因為內容不夠長，所以沒寫在 medium 上

[Nuxt](https://v3.nuxtjs.org/) 是 建立在 Vue 之上更方便的 Framework

他除了把你常用的工具 e.g. vue-router, vuex 包好以外，還有一項很致命的優勢: Server-rendering

1. Server-Rendering

可以參考這篇文件 https://nuxtjs.org/docs/concepts/nuxt-lifecycle/，就是在說明跟 原來的 SPA (單頁網站) 不一樣的是，我們的網頁會在 server 端處理好後 (比如先跑完 created, fetch, mounted)，才傳給你，除了增加速度外(在伺服器直接 query)，更重要的是 meta tag 可以根據你的 url 跳正確的給你，所以 SEO 會比較好 (單頁的你不管給什麼 url 都只會回傳同一份檔案，你看到不同內容是因為 javascript 幫你 render 對的頁面。

設定 meta 也很簡單，就是 Vue component 裡面多一個 header 的 object
``` javascript
  head: {
    title: '玖依 -- 易碎組 Easily Broken',
    meta: [
      {
        hid: 'description',
        content: '玖依 -- 易碎組 Easily Broken'
      }
    ],
    // script: [{ src: "https://platform.twitter.com/widgets.js"}]
  },
```

2. Vue-router

在這個 project 中，我沒有用到過於複雜的 url，只用到這三個
```
/
/kyuuichi
/losmuteki
```

分別對應到，pages 資料夾的這三個，(所以即使我沒有 vue-router 的概念根本沒有關係)

```
/app # ls pages
index.vue      kyuuichi.vue   losmuteki.vue
```

3. Server-Side

在這個 project 中，我把所有資料塞進 cloudflare KV (key-value)，所以並沒有傳統的資料庫，我只需要有一個 js 可以把 json 資料從 KV 拿出來

在 Nuxt 中，只要將這行放在 `server/api/query_kv` 就能從 `/api/query_kv` 拿取資料ㄌ

``` typescript
export default async (req, res) => {
  const value = await easily_broken.get(req.url.slice(1), {type: "json"});
  return value;
}
```

4. Data Fetching

有了後端，有了前端(Vue 部分跳過，很多人講得很好)，我們需要一個程式，可以執行 fetch 無論是在 clinet (瀏覽器)端 或者 server 端

這時候 Nuxt 提供了 useFetch 你輕鬆的拿取資料，也是一樣寫在 Vue object 裡
``` javascript
  async setup() {
    const [{ data: tweets }, { data: tweets_articles }] = await Promise.all([
        useFetch('/api/query_kv/both', {method: "GET"}),
        useFetch('/api/query_kv/articles', {method: "GET"})
    ])
    return {
        tweets, tweets_articles
    }
  },
```


## LICENSE
MIT
