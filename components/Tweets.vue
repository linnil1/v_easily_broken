<template lang="pug">
.tweets
  template(v-for="tweet in tweets")
    a.tweet(v-for="img in tweet.image" :href="tweet.url")
      .author
        img.author-thunmnail(:src="tweet.user_image")
        p {{ tweet.user_name }}
      .main
        .main-img-div
          img.main-img(:src="img")
          // This not work for Firefox
          // iframe.main-img(v-if="tweet.video" :src="tweet.video" frameborder="0")
          // img.main-img(v-else :src="img")
        p.main-text {{ tweet.text }}
      img.twitter-logo(src="~/assets/twitter_logo.svg")
</template>

<script>
export default {
  props: {
    tweets: Array
  }
}
</script>
<style lang='stylus'>
.tweets
  display: flex
  flex-wrap: wrap
  justify-content: center

.tweet
  // mobile
  //   height: auto
  // mobile
  @media screen and (min-width: 600px)
    height: 400px
  // desktop
  @media screen and (min-width: 992px)
    height: 600px
  margin: 5px 5px
  padding: 12px 16px 4px 16px

  border: solid #1DA1F2 1px
  border-radius: 12px
  box-sizing: border-box
  display: flex
  flex-direction: column
  align-items: center
  position: relative

  text-decoration: none
  color: #000

  &:hover
    border: solid #1565c0 1px

  .author
    display: flex
    flex-direction: row
    align-items: center

    .author-thunmnail
      border-radius: 100%
      height: 48px
      width: 48px
      margin-right: 8px

  .main
    overflow: hidden
    .main-img-div
      margin-top: 12px
      max-width: 90vw
      position: relative

      .main-img
        max-height: 100%
        max-width: 100%

      iframe
        height: 100%

    // mobile
    @media not screen and (min-width: 600px)
      .main-img-div
        width: 90vw
    // tablet
    @media screen and (min-width: 600px)
      .main-img-div
        height: 200px
    // desktop
    @media screen and (min-width: 992px)
      .main-img-div
        height: 400px

    .main-text
      margin: 0
      padding: 8px
      width: 0
      min-width: 100%
  
  .twitter-logo
    position: absolute
    right: 8px
    bottom: 8px
    height: 25px
    width: 25px
</style>
