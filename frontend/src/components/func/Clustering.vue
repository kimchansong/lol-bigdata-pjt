<template>
  <v-contatiner fluid class="text-center">
    <v-flex>
      <span id="gap">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" @click="ChangeTOPVlaue">Top</v-btn>
          </template>
          <span>Top 라인</span>
        </v-tooltip>
      </span>
      <span id="gap">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" @click="ChangeMIDVlaue">MID</v-btn>
          </template>
          <span>Mid 라인</span>
        </v-tooltip>
      </span>
      <span id="gap">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" @click="ChangeJUNVlaue">JUNGLE</v-btn>
          </template>
          <span>정글</span>
        </v-tooltip>
      </span>
      <span id="gap">
        <v-tooltip bottom>
          <template v-slot:activator="{ on }">
            <v-btn v-on="on" @click="ChangeBOTVlaue">BOTTOM</v-btn>
          </template>
          <span>Bottom 라인</span>
        </v-tooltip>
      </span> 
      <div id="chartdiv"></div>
    </v-flex>
  </v-contatiner>
</template>

<!-- Resources -->
<script src="https://www.amcharts.com/lib/4/core.js"></script>
<script src="https://www.amcharts.com/lib/4/charts.js"></script>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
import axios from 'axios'

const apiUrl = '/api'
export default {
    data (){
      return {
        cardsPerPage: 10,
        page: 1,
        users: [],
        show: false,
        id: 1,
        info: [],
        names: []
      }
  },
  computed(){
    return this.ChangeTOPVlaue()
  },
  created(){
    this.ChangeTOPVlaue();
  },
  mounted() {

  },
  methods: {
    async ChangeTOPVlaue() {
      this.id = 1
      await axios.get(`${apiUrl}/lol-attack-info/?lane=${this.id}`).then(response => (this.info=response.data))
      let ij = 0
      for(ij = 0; ij<this.info.length; ij++){
        this.names[ij] = this.info[ij].name
      }
      console.log(this.names)
        am4core.useTheme(am4themes_animated);
      let chart = am4core.create("chartdiv", am4charts.XYChart);

      let data = [];
      let open = 100;
      let close = 120;

      console.log(this.names)
      console.log(this.names)
      for (var i = 0; i < this.names.length; i++) {
        if(this.info[i].count!=0){
          open = this.info[i].attack_range
          close = this.info[i].attack_range
          data.push({ category: this.names[i], open: open, close: close });
        }
      }

      chart.data = data;
      let categoryAxis = chart.xAxes.push(new am4charts.CategoryAxis());
      categoryAxis.renderer.grid.template.location = 0;
      categoryAxis.dataFields.category = "category";
      categoryAxis.renderer.minGridDistance = 15;
      categoryAxis.renderer.grid.template.location = 0.5;
      categoryAxis.renderer.grid.template.strokeDasharray = "1,3";
      categoryAxis.renderer.labels.template.rotation = -90;
      categoryAxis.renderer.labels.template.horizontalCenter = "left";
      categoryAxis.renderer.labels.template.location = 0.5;
      categoryAxis.renderer.inside = true;

      categoryAxis.renderer.labels.template.adapter.add("dx", function(dx, target) {
          return -target.maxRight / 2;
      })

      let valueAxis = chart.yAxes.push(new am4charts.ValueAxis());
      valueAxis.tooltip.disabled = true;
      valueAxis.renderer.ticks.template.disabled = true;
      valueAxis.renderer.axisFills.template.disabled = true;
  
      let series = chart.series.push(new am4charts.ColumnSeries());
      series.dataFields.categoryX = "category";
      series.dataFields.openValueY = "open";
      series.dataFields.valueY = "close";
      series.tooltipText = "공격사거리: {valueY.value}";
      series.sequencedInterpolation = true;
      series.fillOpacity = 0;
      series.strokeOpacity = 1;
      series.columns.template.width = 0.01;
      series.tooltip.pointerOrientation = "horizontal";

        let openBullet = series.bullets.create(am4charts.CircleBullet);
        openBullet.locationY = 1;

        let closeBullet = series.bullets.create(am4charts.CircleBullet);

        closeBullet.fill = chart.colors.getIndex(4);
        closeBullet.stroke = closeBullet.fill;

        chart.cursor = new am4charts.XYCursor();
    },
    ChangeMIDVlaue: function() {
      this.id = 3
      axios.get(`${apiUrl}/lol-attack-info/?lane=${this.id}`).then(response => (this.info=response.data))
      console.log(this.names)
    },
    ChangeJUNVlaue: function() {
      this.id = 2
      axios.get(`${apiUrl}/lol-attack-info/?lane=${this.id}`).then(response => (this.info=response.data))
      console.log(this.names)
    },
    ChangeBOTVlaue: function() {
      this.id = 4
      axios.get(`${apiUrl}/lol-attack-info/?lane=${this.id}`).then(response => (this.info=response.data))
      console.log(this.names)
    },
  }
}
</script>

<style>
#chartdiv {
  width: 100%;
  height: 500px;
}

#gap {
  padding : 10px 10px 10px 10px;
}
</style>