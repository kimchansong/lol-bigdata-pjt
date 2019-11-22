<template>
    <v-data-table
    :headers="headers"
    :items="desserts"
    class="elevation-1"
    >
    <template v-slot:item.list="{ item }">
        <v-list-item-avatar class="avatar">
            <img :src="'https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/'+ item.champName + '.png'"/>
        </v-list-item-avatar>
    </template>
      
  </v-data-table>
</template>

<script>
export default {
    data () {
        return {
            headers: [
                {
                text: 'number',
                align: 'left',
                sortable: false,
                value: 'number'
                },
                { text: 'Champ', value: 'list' },
                { text: 'ChampName', value: 'champName' },
                { text: 'counter', value:'counter' },
                { text: 'WinRate(%)', value:'winRate'}
            ],
            desserts: [
                {
                value: false,
                number: '1',
                champName: 'LeeSin',
                counter: '룰루 랄라 비데',
                winRate: '50%'
                },
                {
                value: false,
                number: '2',
                champName: 'Aatrox',
                counter: '리신',
                winRate: '40%'
                },
            ]
        }
    },    
}
</script>