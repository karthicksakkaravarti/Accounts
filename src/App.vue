<template>
  <v-app>
    <v-main>
             <router-view/>
    </v-main>
  </v-app>
</template>

<script>

export default {
  name: 'App',
  data: () => ({
    //
  }),
  watch: {
      $route(to,) {
          console.log(to)
          document.title = 'Accounts - ' +to.meta.title || 'Accounts';
      },
  },
};
</script>
