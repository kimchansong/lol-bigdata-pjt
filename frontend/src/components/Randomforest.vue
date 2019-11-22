<template>
  <v-container>
    <v-layout>
      <v-flex>
        <v-row>
          <v-container class="p-0"><v-btn @click="make_chart()"><b>정확도{{this.info.accuracy}}</b></v-btn>
            <div id="chartdiv" style="height:360px!important;color:white!important"></div>
          </v-container>
        </v-row>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<!-- <script src="//www.amcharts.com/lib/4/core.js"></script>
<script src="//www.amcharts.com/lib/4/charts.js"></script> -->
<!-- <script src="//www.amcharts.com/lib/4/themes/animated.js"></script> -->
<script>
import axios from "axios"
const apiUrl = "/api"
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import * as am4maps from "@amcharts/amcharts4/maps";
import am4geodata_usaAlbersLow from "@amcharts/amcharts4-geodata/usaAlbersLow";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";

export default {

  data() {
    return{
      info : {},
    }
  },
  methods: {
    async create_chart() {

      await axios.get(`${apiUrl}/lol-win-variable/`)
      .then(response => (this.info=response.data))
        console.log(this.info)
    },
    make_chart(){
          am4core.useTheme(am4themes_animated);

          /* Create chart instance */
          var chart = am4core.create("chartdiv", am4charts.XYChart);
          chart.paddingRight = 0;

          /* Add data */

          chart.data = [
          ];
          for(var i in this.info.newhead) {
            console.log(i)
              chart.data.push({
                category: this.info.newhead[i],
                value: this.info.std[i]*100,
                target: this.info.importances[i]*100
              })
            }


          /* Create axes */
          var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
          categoryAxis.dataFields.category = "category";
          categoryAxis.renderer.minGridDistance = 5;
          categoryAxis.renderer.grid.template.disabled = true;

          var valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
          valueAxis.renderer.minGridDistance = 30;
          valueAxis.renderer.grid.template.disabled = true;
          valueAxis.min = 0;
          valueAxis.max = 50;
          valueAxis.strictMinMax = true;
          valueAxis.renderer.labels.template.adapter.add("text", function(text) {
            return text + "%";
          });

          /* Create ranges */
          function createRange(axis, from, to, color) {
            var range = axis.axisRanges.create();
            range.value = from;
            range.endValue = to;
            range.axisFill.fill = color;
            range.axisFill.fillOpacity = 0.8;
            range.label.disabled = true;
          }

          createRange(valueAxis, 0, 10, am4core.color("#336666"));
          createRange(valueAxis, 10, 30, am4core.color("#333366"));
          createRange(valueAxis, 30, 60, am4core.color("#330066"));
          createRange(valueAxis, 60, 80, am4core.color("#f6d32b"));
          createRange(valueAxis, 80, 100, am4core.color("#fb7116"));

          /* Create series */
          var series = chart.series.push(new am4charts.ColumnSeries());
          series.dataFields.valueX = "value";
          series.dataFields.categoryY = "category";
          series.columns.template.fill = am4core.color("#000");
          series.columns.template.stroke = am4core.color("#fff");
          series.columns.template.strokeWidth = 1;
          series.columns.template.strokeOpacity = 0.5;
          // series.columns.template.height = am4core.percent(80);

          var series2 = chart.series.push(new am4charts.LineSeries());
          series2.dataFields.valueX = "target";
          series2.dataFields.categoryY = "category";
          series2.strokeWidth = 1;

          var bullet = series2.bullets.push(new am4charts.Bullet());
          bullet.layout = "absolute";
          var line = bullet.createChild(am4core.Line);
          line.x1 = 0;
          line.y1 = -15;
          line.x2 = 0;
          line.y2 = 15;
          line.stroke = am4core.color("#000");
          line.strokeWidth = 1;


    }

  },
  created() {
    this.create_chart();
  },


}
</script>
<style>


</style>
