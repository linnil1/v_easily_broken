<template lang="pug">
div
  Title 易碎組 Easily Broken
  Meta(name='twitter:title'       content='易碎組 Easily Broken')
  Meta(name='twitter:description' content='易碎組 Easily Broken。 蘿絲跟玖依，兩位也就是從電視機跟罐子轉生為蘿莉組成的團體')
  Meta(name='twitter:image'       content='https://pbs.twimg.com/media/FFzGFY-UUAYZdII.jpg')
  Nav.bgcolor-both.color-both
  .intro-container.bgcolor-both
    .intro
      .intro-img
        img(src="https://pbs.twimg.com/media/FFzGFY-UUAYZdII.jpg")
        .drawer.drawer-right <a href="https://twitter.com/miziquan_naiali"> 繪師 @miziquan_naiali 米自犬 </a>
      .intro-text
        p.intro-name 易碎組
        p.intro-name Easily Broken
        p 電視機跟罐子
        p 兩位轉生為蘿莉
        p 所組成的團體
        p 很喜歡貼貼
  .tweets-head 雙人 Fan Arts
  Tweets(:tweets="tweets")
  .tweets-head 同人文章
  Tweets(:tweets="tweets_articles")
  Footer
</template>

<script>
export default {
  async setup() {
    // WHY POST not work
    // Uncaught (in response) TypeError: URL.createObjectURL is not a function
    var [{ data: tweets }, { data: tweets_articles }] = await Promise.all([
        // useFetch('/api/query_kv_test/both', {method: "POST"}),
        // useFetch('/api/query_kv_test/articles', {method: "POST"})
        useFetch('/api/query_kv/both', {method: "GET"}),
        useFetch('/api/query_kv/articles', {method: "GET"})
    ])
    return {
        tweets, tweets_articles
    }
  },
}
</script>

<style lang='stylus' src="~/assets/member.styl" />
<style lang='stylus'>
.bgcolor-both
  background-color: #F3D6D2
.color-both > .nav-item
  color: #4A696E
</style>
