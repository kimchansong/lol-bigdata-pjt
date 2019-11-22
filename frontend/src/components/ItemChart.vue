<template>
    <div id="chartdiv2"></div>	
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import * as am4maps from "@amcharts/amcharts4/maps";
import am4geodata_usaAlbersLow from "@amcharts/amcharts4-geodata/usaAlbersLow";
import axios from "axios";
const apiUrl = "/api"

export default {
    name: "Analysis",
    components:{
        // pickandban
    },
    mounted() {
        this.drawChart()
    },
    data:() =>({
        banPick:[],
        banNPinck:[],
        info:[],
        char_name:[],
        item:[],
        item_name:[]
    }),
    methods: {
        async drawChart() {
            await axios.get(`${apiUrl}/lol-item-chart-list/?char_id=`+this.key)
            .then(response => (this.item=response.data))

            await axios.get(`${apiUrl}/lol-item-name-list/`)
            .then(response => (this.item_name=response.data))

            var chart = am4core.create("chartdiv2", am4charts.XYChart);
            chart.data = [];
            var total_cnt = 0
            for(let i=0; i<this.item.length; i++){
                total_cnt+=this.item[i].item_cnt
            }
            for(let i=0; i<this.item.length; i++){
                var tem_id2 = this.item[i].item_id
                var cnt = this.item[i].item_cnt
                if(tem_id2 != 0){
                    for(let j=0; j<this.item_name.length; j++){
                        if(tem_id2==this.item_name[j].key){
                            var cnt = 1*((cnt/total_cnt)*10000).toFixed(1)
                            if(cnt>=100)
                                cnt=100
                            chart.data.push({year:this.item_name[j].name, income:cnt, expenses:cnt})
                        }
                    }
                }
            }

            // console.log(chart.data)

            //create category axis for years
            var categoryAxis = chart.yAxes.push(new am4charts.CategoryAxis());
            categoryAxis.dataFields.category = "year";
            categoryAxis.stroke=am4core.color("gray");
            categoryAxis.renderer.inversed = true;
            categoryAxis.renderer.grid.template.location = 0;

            //create value axis for income and expenses
            var valueAxis = chart.xAxes.push(new am4charts.ValueAxis());
            valueAxis.renderer.opposite = true;


            //create columns
            var series = chart.series.push(new am4charts.ColumnSeries());
            series.dataFields.categoryY = "year";
            series.dataFields.valueX = "income";
            series.name = "Pick(%)";
            series.columns.template.fillOpacity = 1;
            series.columns.template.strokeOpacity = 0;
            series.tooltipText = "{categoryY}: {valueX.value}(%)";

            //create line
            // var lineSeries = chart.series.push(new am4charts.LineSeries());
            // lineSeries.dataFields.categoryY = "year";
            // lineSeries.dataFields.valueX = "expenses";
            // lineSeries.name = "Expenses";
            // lineSeries.strokeWidth = 3;
            // lineSeries.tooltipText = "Expenses in {categoryY}: {valueX.value}";

            //add bullets
            // var circleBullet = lineSeries.bullets.push(new am4charts.CircleBullet());
            // circleBullet.circle.fill = am4core.color("#fff");
            // circleBullet.circle.strokeWidth = 2;

            //add chart cursor
            chart.cursor = new am4charts.XYCursor();
            chart.cursor.behavior = "zoomY";

            //add legend
            chart.legend = new am4charts.Legend();
        
        }
    }
}
</script>

<style>
#chartdiv2 {
  width: 100%;
  height: 2400px;
}
</style>
