# EasilyBroken

## Architecure

I save our data in worker KV,
so no traditional database is used in this project,

thus no database instance is needed to start,
the ONLY thing I should setup is a Cloudflare Worker.

![](https://raw.githubusercontent.com/linnil1/v_easily_broken/main/architecture.png)

(I know HTML, js and CSS are also saved in KV)

## Setup
```bash
yarn install
```


## Data

Here is the pipeline to save tweets data in Worker KV.

1. Create a twitter list

`data.csv`
``` csv
update,tw_type,url
f,91,https://twitter.com/adsl6658/status/1465516485590204417
t,91,https://twitter.com/zzz_2605/status/1465531552616484872
t,91,https://twitter.com/toritodori1/status/1465521877607063552
t,los,https://twitter.com/Kyuuichi0091/status/1467079202197635073
f,both,https://twitter.com/justdcfun1332/status/1467119400994340867
```

`t` for update/insert and `f` will skip

2. save tweets into json

Put your twitter token here
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

3. create a KV namespace(setup once)

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

When developing, you can separate each part if it's no available.

1. If you don't want to use kv, you can manully setup a python API

`page/*vue`
``` javascript
var { data: tweets } = await useFetch('/api/query_kv_test/91', {method: "POST"})
// var { data: tweets } = await useFetch('/api/query_kv/91', {method: "POST"})
```
`server/api/query_kv_test.ts`
``` javascript
const url = "http://localhost:8081/api" + req.url
```

2. If you don't want to fetch tweets data via twitter api, you can use example json.

`data.py#111`
``` python
# app.add_routes([web.post('/api/{tw_type}', getTweetsJson)])
app.add_routes([web.post('/api/{tw_type}', getTweetsJsonExample)])
```

3. If you don't want to use Fetch, you can initial a json named 'tweets' and remove the fetch section.

`pages/kyuuichi.vue`
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
var { data: tweets } = await useFetch('/api/query_kv/91', {method: "GET"})
// var { data: tweets } = await useFetch('/api/query_kv/91', {method: "POST"})  // not work, WHY?
```


# Documentation (文件)
https://github.com/linnil1/v_easily_broken/wiki/Documentation-%E6%96%87%E4%BB%B6


## LICENSE
MIT
