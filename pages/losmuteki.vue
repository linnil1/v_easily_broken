<template lang="pug">
div
  Nav.bgcolor-los.color-los
  .intro-container.bgcolor-los
    .intro
      .intro-text
        p.intro-name 蘿絲
        p 生日： 6 / 25
        p 前世：罐子
        p 設定：機娘蘿莉
        p 個性：天才酵素
        p 二創 tag：#蘿絲毋拿去 
        p twitter: <a href="https://twitter.com/LosMuteki"> LosMuteki </a>
      .intro-img
        img(src="https://pbs.twimg.com/media/FFwcAckVUAA9H3-.jpg")
        .drawer.drawer-left <a href="https://twitter.com/Kyuuichi0091"> 繪師 @kyuuichi0091 九壹 </a>
  .tweets-head Fan Arts
  Tweets(:tweets="tweets")
  Footer
</template>

<script>
export default {
  async setup() {
    // const { data: tweets } = await useFetch('/api/query_kv/los', {method: "POST"})
    const { data: tweets } = await useFetch('/api/query_kv/los', {method: "GET"})
    return {
      tweets
    }
  },
  head: {
    title: '蘿絲 -- 易碎組 Easily Broken',
    meta: [
      {
        hid: 'description',
        content: '蘿絲 -- 易碎組 Easily Broken'
      }
    ],
  },
}
</script>
<style lang='stylus' src="~/assets/member.styl" />
<style lang='stylus'>
.drawer-left
  right: 100%
.bgcolor-los
  background-color: #707299
.color-los > .nav-item
  color: #e0f7fa
</style>
