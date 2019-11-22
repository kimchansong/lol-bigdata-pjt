<template>
    <v-container>
        <v-layout>
            <v-flex>
                <!-- <SearchForm></SearchForm> -->
                <ChampsInfo></ChampsInfo>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import ChampsInfo from "../components/ChampsInfo.vue"
// import SearchForm from "../components/searchForm.vue"

export default {
    name: 'lolting1',
    components : {
        ChampsInfo,
        // SearchForm
    }
}
</script>
<style>
</style>
