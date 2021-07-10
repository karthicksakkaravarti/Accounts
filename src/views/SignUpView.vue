<template>
  <div class="home">
    <CreateAccount />
  </div>
</template>

<script>
// @ is an alias to /src
import CreateAccount from '@/components/CreateAccount'

export default {
  name: 'Home',
  components: {
    CreateAccount
  }
}
</script>
