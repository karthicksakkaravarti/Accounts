<template>
  <v-app>
    
    <v-main>
             <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import { UtilityMixin } from "./mixins/utility";

export default {
  mixins: [UtilityMixin],
  name: 'App',
  data: () => ({
    //
  }),
  watch: {
      $route(to,) {
          document.title = 'Accounts - ' +to.meta.title || 'Accounts';
      },
  },
};
</script>
