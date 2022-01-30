<template lang="pug">
.footer
  p 記得 點進去 twitter 按愛心
  div
    img.github(src="~/assets/GitHub-Mark-64px.png")
    a(href='https://github.com/linnil1/v_easily_broken') https://github.com/linnil1/v_easily_broken
</template>

<style lang='stylus'>
.footer
  margin-top: 20px
  padding: 10px 10px
  display: flex
  flex-direction: column
  align-items: center
  justify-content: center
  background-color: #424242
  color: #f5f5f5 
  p
    margin: 0

  div
    display: flex
    align-items: center

    .github
      width: 24px 
      height: 24px 
      margin: 0 4px
</style>

