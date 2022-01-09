<template lang="pug">
.nav
  NuxtLink.nav-item(to="/") 易碎組首頁
  NuxtLink.nav-item(to="/kyuuichi") 玖依
  NuxtLink.nav-item(to="/losmuteki") 蘿絲
</template>

<style lang='stylus'>

.nav
  display: flex
  width: 100%
  justify-content: center
  height: 55px

  .nav-item 
    margin: 16px
    box-sizing: border-box
    text-decoration: none
    position: relative

    &.router-link-active
      color: #000

    &::after
      position: absolute
      content: ""
      bottom: 0
      left: 0
      width: 100%
      height: 3px
      background: #039be5
      transform: scaleX(0)
      transform-origin: right
      transition: transform 0.5s

    &:hover::after
      transform: scaleX(1)
      transform-origin: left
</style>
