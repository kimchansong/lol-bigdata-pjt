<template lang="html">
  <!-- <v-app id="app"> -->
  <div>

    <lolgating/>

  </div>
  <!-- </v-app> -->
</template>

<script>
import Search from "../components/func/search"
import ChampsInfo from "../components/ChampsInfo"
import lolgating from "../components/LolgatingStart"

export default {
  components: {
    lolgating
  },
  data() {
    return {
      id: 1,
      url : ""
    }
  },

}
</script>

<style scoped>

</style>
