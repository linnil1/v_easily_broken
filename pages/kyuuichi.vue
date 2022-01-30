<template lang="pug">
div
  Title 玖依 -- 易碎組 Easily Broken
  Meta(name='twitter:title'       content='玖依 -- 易碎組 Easily Broken')
  Meta(name='twitter:description' content='玖依 -- 易碎組 Easily Broken。從映像管電視機轉生成的蘿莉')
  Meta(name='twitter:image'       content='https://pbs.twimg.com/media/FFdJrIaaQAAby4r.jpg')
  Nav.bgcolor-91.color-91
  .intro-container.bgcolor-91
    .intro
      .intro-img
        img(src="https://pbs.twimg.com/media/FFdJrIaaQAAby4r.jpg")
        .drawer.drawer-right <a href="https://twitter.com/miziquan_naiali"> 繪師 @miziquan_naiali 米自犬 </a>
      .intro-text
        p.intro-name 玖依
        p 生日： 4 / 19
        p 前世：電視機
        p 設定：電視蘿莉
        p 個性：傲嬌、愛大家
        p 二創 tag：#玖要在依起 
        p twitter: <a href="https://twitter.com/Kyuuichi0091"> Kyuuichi0091 </a>
  .tweets-head Fan Arts
  Tweets(:tweets="tweets")
  Footer
</template>

<script>
export default {
  data() {
    return {
      tweets: [
        {
          "create_at": "2021-11-30T16:35:44+00:00",
          "image": ["https://pbs.twimg.com/media/FFdJrIaaQAAby4r.jpg"],
          "text": "大家有畫過的都是共犯我們裡面見QwQ\n#玖要在依起 https://t.co/aWLSmym41r https://t.co/SpMIQZC2Y7",
          "url": "https://t.co/aWLSmym41r",
          "user_id": "miziquan_naiali",
          "user_image": "https://pbs.twimg.com/profile_images/1413456490518614019/cYZGVUrX_normal.jpg",
          "user_name": "米自犬"
        },
        {
          "create_at": "2021-12-04T10:31:53+00:00",
          "image": ["https://pbs.twimg.com/media/FFwcAckVUAA9H3-.jpg"],
          "text": "對\nLos不是傲嬌ㄌㄌㄎ\n是傲嬌ㄌㄌ((\n\n我不會畫ㄌㄌ但是我覺得我好棒(･ω´･ )(((\n#蘿絲毋拿去 https://t.co/dvxNShL1W0",
          "url": "https://t.co/dvxNShL1W0",
          "user_id": "Kyuuichi0091",
          "user_image": "https://pbs.twimg.com/profile_images/1377648916678680578/rlSyYbT1_normal.jpg",
          "user_name": "📺九壹🔧✨"
        },
        {
          "create_at": "2021-12-04T22:51:42+00:00",
          "image": ["https://pbs.twimg.com/media/FFzGFY-UUAYZdII.jpg"],
          "text": "互相送作堆 🥳\n\n#玖要在依起 #蘿絲毋拿去 https://t.co/oTse4CbVNT ",
          "url": "https://t.co/oTse4CbVNT",
          "user_id": "miziquan_naiali",
          "user_image": "https://pbs.twimg.com/profile_images/1413456490518614019/cYZGVUrX_normal.jpg",
          "user_name": "米自犬"
        },
      ]
  }}, 
  async setup() {
    // var { data: tweets } = await useFetch('/api/query_kv/91', {method: "POST"})
    var { data: tweets } = await useFetch('/api/query_kv/91', {method: "GET"})
    return {
      tweets
    }
  },
}
</script>
<style lang='stylus' src="~/assets/member.styl" />
<style lang='stylus'>
.drawer-right
  right: 0

.bgcolor-91
  background-color: #E6D2B7
.color-91 > .nav-item
  color: #F47F79
</style>
