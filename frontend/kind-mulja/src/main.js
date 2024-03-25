import './plugins/axios'

import { createApp } from 'vue'
import { pinia } from './pinia'
import piniaPluginPersistedstate from 'pinia-plugin-persistedstate';


import App from './App.vue'
import router from './router'

const app = createApp(App)
pinia.use(piniaPluginPersistedstate);


// Vuetify
import 'vuetify/styles';
import { createVuetify } from 'vuetify';
import '@mdi/font/css/materialdesignicons.css';
import * as components from 'vuetify/components';
import * as directives from 'vuetify/directives';

const vuetify = createVuetify({
  components,
  directives,
  iconssets: {
    iconfont: 'mdi', // Use the mdi (Material Design Icons) iconset
  },
});

app.use(vuetify);

app.use(pinia);
app.use(router)

app.mount('#app')
