const app = Vue.createApp({})

app.component('normal-article', {
  props: [
    'titel',
    'schrijver',
    'datum',
    'samenvatting'
  ],
  template: `
    <div class="normal-article">
        <div class="content">
            <h4>{{titel}}</h4>
            <h5>Door <span class="info">{{schrijver}}</span> op <span class="info">{{datum}}</span></h5>
            <p>{{samenvatting}}</p>
        </div>
    </div>
  `
})

app.component('banner-article', {
  props: [
    'titel',
    'schrijver',
    'datum',
    'samenvatting'
  ],
  template: `
    <div class="banner-article">
        <div class="content">
            <h3 class="article-title">{{titel}}</h3>
            <h5>Door <span class="info">{{schrijver}}</span> op <span class="info">{{datum}}</span></h5>
            <p>{{samenvatting}}</p>
            <button class="meerlezen">Meer lezen</button>
        </div>
    </div>
  `
})

const vm = app.mount("body")