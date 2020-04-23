import Vue from 'vue'
import App from './App.vue'
import BuildingUpload from './BuildingUpload.vue'
import Buildings from './Buildings.vue'
import Readings from './Readings.vue'
import ReadingGraph from './ReadingGraph.vue'
import VModal from 'vue-js-modal'
import VueGraph from 'vue-graph'

Vue.use(VModal)
Vue.use(VueGraph)

Vue.component("BuildingUpload", BuildingUpload)
Vue.component("Buildings", Buildings)
Vue.component("Readings", Readings)
Vue.component("ReadingGraph", ReadingGraph)


new Vue({
  el: '#app',
  render: h => h(App)
})
