<template>
    <div id="chart"></div>
</template>

<script>
import * as am4core from "@amcharts/amcharts4/core";
import * as am4charts from "@amcharts/amcharts4/charts";
import am4themes_animated from "@amcharts/amcharts4/themes/animated";
export default {
    data () {
        return {
        }
    },
    props:{
        wins : { type : Number },
        losses : { type : Number },
        summonerName : { type: String}
    },
    created() {
        // this.create_chart(this.wins, this.losses)
    },
    watch: {
        summonerName: function(newVal, oldVal) {
            this.create_chart(this.wins, this.losses);
        },
    },
    methods: {
        create_chart(wins,losses) {
            // Themes begin
            am4core.useTheme(am4themes_animated);

            // Create chart instance
            var chart = am4core.create("chart", am4charts.PieChart);

            // Add data
            chart.data = [
                {
                country: "승",
                ratio: wins,
                color: "red"
                },
                {
                country: "패",
                ratio: losses,
                color: "yellow"
                }
            ];

            // Set inner radius
            chart.innerRadius = am4core.percent(10);

            // Add and configure Series
            var pieSeries = chart.series.push(new am4charts.PieSeries());
            pieSeries.dataFields.value = "ratio";
            pieSeries.dataFields.category = "country";
            pieSeries.slices.template.stroke = am4core.color("#333");
            // pieSeries.slices.template.fill = am4core.color(color);

            pieSeries.slices.template.strokeWidth = 3;

            pieSeries.slices.template.strokeOpacity = 1;

            // This creates initial animation
            pieSeries.hiddenState.properties.opacity = 1;
            pieSeries.hiddenState.properties.endAngle = -90;
            pieSeries.hiddenState.properties.startAngle = -90;
        } // end am4core.ready()
       
    }
};
</script>
<style>
</style>
