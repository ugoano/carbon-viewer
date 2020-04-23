<template>
    <div>
        <div id="chartcontainer" style="height: 300px; width: 350px;"></div>
    </div>
</template>

<script>
    export default {
        name: 'ReadingGraph',
        props: ['rawdata'],
        methods: {
            transformValues() {
                var data = {
                    type: "line",
                    dataPoints: [
                    ]
                };
                console.log(this.rawdata);
                var maxDate = new Date("1970-01-01");
                var minDate = new Date();
                var maxValue = 0;
                for(var v=0; v<this.rawdata.length; v++) {
                    var readingDate = new Date(this.rawdata[v].reading_date_time);
                    if (readingDate < minDate) {
                        minDate = readingDate;
                    }
                    if (readingDate >= maxDate) {
                        maxDate = readingDate;
                    }
                    if (this.rawdata[v].consumption > maxValue) {
                        maxValue = this.rawdata[v].consumption;
                    }
                    data.dataPoints.push(
                        {
                            x: readingDate,
                            y: this.rawdata[v].consumption
                        }
                    );
                }
                this.chartOptions.data = [data];
            },
        },  
        data() {
            return {
                labels:[
                ],
                values: [
                ],
                ymax: 100,
                chart: null,
                chartOptions: {
                    title: {
                        text: "Chart"
                    },
                    data: [
                        {
                            type: "line",
                            dataPoints: [
                                { x: 10, y: 71 },
                                { x: 20, y: 55 },
                                { x: 30, y: 25 },
                                { x: 40, y: 15 },
                                { x: 50, y: 28 }
                            ]
                        }
                    ]
                },
            }
        },
        watch: {
            rawdata: function() {
                this.transformValues();
                this.chart = new CanvasJS.Chart("chartcontainer", this.chartOptions);
                this.chart.render();
            }
        },
        mounted() {
            this.transformValues();
            this.chart = new CanvasJS.Chart("chartcontainer", this.chartOptions);
            this.chart.render();
        }
    }
</script>
