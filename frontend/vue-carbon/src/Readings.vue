<template>
    <div class="container">
        <div id="reading-list" class="large-12 medium-12 small-12 cell">
            <button v-on:click="toggleGraph">{{ toggleText }}</button>
            <ReadingGraph v-if="showgraph" ref="graph" :rawdata="readings">
            </ReadingGraph>
            <table v-if="!showgraph" align="center">
                <tr>
                    <th>Reading time</th> <th>Consumption</th>
                </tr>
                <tr v-for="(reading, i) in readings" :key="`reading-${i}`">
                    <td>{{ reading.reading_date_time }}</td>
                    <td>{{ reading.consumption }} {{ reading.meter }}</td>
                </tr>
            </table>
            <div style="display:inline"><button v-on:click="previouspage()">Previous</button></div>
            <div style="display:inline">Page {{ page }}</div>
            <div style="display:inline"><button v-on:click="nextpage()">Next</button></div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Readings',
        props: ['meterid'],
        watch: {
            meterid: function(newMeterId) {
                this.apiCall(1);
                console.log(this.$refs.graph);
                if(this.showgraph) {
                    this.$refs.graph.setValues(this.readings);
                }
            }
        },
        data() {
            return {
                page: 1,
                hasNext: true,
                readings: [],
                showgraph: false,
                toggleText: "Show Graph"
            }
        },
        methods: {
            toggleGraph() {
                this.showgraph = !this.showgraph;
                this.toggleText = "Show " + (this.showgraph? "Table": "Graph");
            },
            nextpage() {
                if(this.hasNext) {
                    this.apiCall(this.page + 1);
                }
            },
            previouspage() {
                if(this.page > 1) {
                    this.apiCall(this.page - 1);
                }
            },
            apiCall(page_num) {
                axios.get('http://localhost:5000/readings/?meter_id=' + this.meterid + '&page=' + page_num).then(
                    (response) => {
                        console.log(response.data.results);
                        this.readings = response.data.results;
                        this.page = page_num;
                        this.hasNext = (response.data.next != null);
                    },
                    (error) => { console.log(error) }
                );
            }
        },
        mounted() {
            this.apiCall(this.page);
        }
    };
</script>
