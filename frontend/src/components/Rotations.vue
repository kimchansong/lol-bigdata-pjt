<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-row>
          <v-container fluid>
            <v-row>
              <v-toolbar color="orange accent-1">
                <v-toolbar-title class="title mr-6 hidden-sm-and-down">search</v-toolbar-title>
                <v-autocomplete
                >
                  <template v-slot:no-data>
                    <v-list-item>
                      <v-list-item-title>
                        search champion
                      </v-list-item-title>
                    </v-list-item>
                  </template>
                </v-autocomplete>
              </v-toolbar>

              <v-col v-for="i in 5" :key="i">
                <img
                  src="https://ddragon.leagueoflegends.com/cdn/9.16.1/img/champion/LeeSin.png"
                  style="width:50px; height:50px"
                />
              </v-col>
            </v-row>
          </v-container>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>