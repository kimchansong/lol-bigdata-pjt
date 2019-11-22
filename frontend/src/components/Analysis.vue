<template>
    <div id="chartdiv1"></div>	
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
        this.dataInfo()
        this.drawChart()
    },
    data:() =>({
        banPick:[],
        banNPinck:[],
        info:[],
        char_name:[]
    }),
    methods: {
        async dataInfo() {
            await axios.get(`${apiUrl}/lol-pickban-list/?char_id=`+this.key)
            .then(response => (this.info=response.data))
            for(let i=0; i<this.info.length; i++){
                var name = this.info[i].name
                var ban_cnt = this.info[i].bancount
                var pick_cnt = this.info[i].pickcount

                this.banPick.push({name:name, ban_cnt:ban_cnt, pick_cnt:pick_cnt})
            }
            
        },
        async drawChart() {
            await axios.get(`${apiUrl}/lol-pickban-list/`)
            .then(response => (this.info=response.data))
            let mainContainer = am4core.create("chartdiv1", am4core.Container);
            mainContainer.width = am4core.percent(100);
            mainContainer.height = am4core.percent(100);
            mainContainer.layout = "horizontal";

            let usData = []
            for(let i=0; i<this.info.length; i++){
                if(this.info[i].id>0){
                    await axios.get(`${apiUrl}/lol-champion-list/?key=`+this.info[i].id)
                    .then(response => (this.char_name=response.data))
                    
                    var name = this.char_name[0].name
                    var ban_cnt = ((this.info[i].bancount/60000)*100).toFixed(2)
                    var pick_cnt = ((this.info[i].pickcount/60000)*100).toFixed(2)
                    if(name!=0)
                        usData.push({age:name, male:ban_cnt, female:pick_cnt})
                }
            }

            // console.log(usData)

            let maleChart = mainContainer.createChild(am4charts.XYChart);
            maleChart.paddingRight = 0;
            maleChart.data = JSON.parse(JSON.stringify(usData));

            // Create axes
            let maleCategoryAxis = maleChart.yAxes.push(new am4charts.CategoryAxis());
            maleCategoryAxis.dataFields.category = "age";
            maleCategoryAxis.stroke=am4core.color("gray");
            maleCategoryAxis.renderer.grid.template.location = 0;
            maleCategoryAxis.renderer.minGridDistance = 15;

            let maleValueAxis = maleChart.xAxes.push(new am4charts.ValueAxis());
            maleValueAxis.renderer.inversed = true;
            maleValueAxis.min = 0;
            maleValueAxis.max = 50;
            let maleSeries = maleChart.series.push(new am4charts.ColumnSeries());
            maleSeries.dataFields.valueX = "male";
            // maleSeries.dataFields.valueXShow = "percent";
            maleSeries.calculatePercent = true;
            maleSeries.dataFields.categoryY = "age";
            maleSeries.interpolationDuration = 1;
            maleSeries.columns.template.tooltipText = "Ban %, {categoryY}: {valueX} %";
            //maleSeries.sequencedInterpolation = true;


            let femaleChart = mainContainer.createChild(am4charts.XYChart);
            femaleChart.paddingLeft = 0;
            femaleChart.data = JSON.parse(JSON.stringify(usData));

            // Create axes
            let femaleCategoryAxis = femaleChart.yAxes.push(new am4charts.CategoryAxis());
            femaleCategoryAxis.renderer.opposite = true;
            femaleCategoryAxis.dataFields.category = "age";
            femaleCategoryAxis.stroke=am4core.color("gray");
            femaleCategoryAxis.renderer.grid.template.location = 0;
            femaleCategoryAxis.renderer.minGridDistance = 15;

            let femaleValueAxis = femaleChart.xAxes.push(new am4charts.ValueAxis());
            femaleValueAxis.min = 0;
            femaleValueAxis.max = 50;
            // femaleValueAxis.strictMinMax = true;
            // femaleValueAxis.numberFormatter = new am4core.NumberFormatter();
            // femaleValueAxis.numberFormatter.numberFormat = "#.#'%'";
            // femaleValueAxis.renderer.minLabelPosition = 1;

            // Create series
            let femaleSeries = femaleChart.series.push(new am4charts.ColumnSeries());
            femaleSeries.dataFields.valueX = "female";
            // femaleSeries.dataFields.valueXShow = "percent";
            femaleSeries.calculatePercent = true;
            femaleSeries.fill = femaleChart.colors.getIndex(4);
            femaleSeries.stroke = femaleSeries.fill;
            femaleSeries.sequencedInterpolation = true;
            femaleSeries.columns.template.tooltipText = "Pick %, {categoryY}: {valueX} %";
            femaleSeries.dataFields.categoryY = "age";
            femaleSeries.interpolationDuration = 1;


            // label.fill = am4core.color("red").lighten(-0.5);
            // label.stroke = am4core.color("red").lighten(0.5);

            let label = mainContainer.createChild(am4core.Label);
            label.isMeasured = false;
            label.x = am4core.percent(80);
            label.horizontalCenter = "middle";
            label.y = 50;
            label.showOnInit = true;
            // label.text = "US Population pyramid";
            label.hiddenState.properties.dy = -100;
            
        }
    },
}
</script>

<style>
#chartdiv1 {
  width: 100%;
  height: 2400px;
}
</style>
