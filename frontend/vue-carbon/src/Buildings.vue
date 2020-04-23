<template>
    <div class="container">
        <div id="building-list" class="large-12 medium-12 small-12 cell">
            <table align="center">
                <tr>
                    <th>ID</th> <th>Name</th> <th>Meters</th>
                </tr>
                <tr v-for="(building, i) in buildings" :key="`building-${building.id}`">
                    <td>{{ building.id }}</td>
                    <td>{{ building.name }}</td>
                    <td><button v-on:click="open(i)">Meters</button></td>
                    <modal height="360px" :name="`meter-${i}`">
                        <table>
                            <tr style="vertical-align:top">
                                <td>
                                    <ul v-for="meter in building.meters" :key="`meter-${meter.id}`">
                                        <li>{{ meter.id }}</li>
                                        <li><a v-on:click="getreadings(meter.id)" href="#">{{ meter.fuel }}</a></li>
                                        <li>{{ meter.unit }}</li>
                                    </ul>
                                </td>
                                <td><Readings v-if="meterid" :meterid="meterid"></Readings></td>
                            </tr>
                        </table>
                    </modal>
                </tr>
            </table>
            <div><button v-on:click="previouspage()">Previous</button></div>
            <div>Page {{ page }}</div>
            <div><button v-on:click="nextpage()">Next</button></div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';

    export default {
        name: 'Buildings',
        data() {
            return {
                page: 1,
                hasNext: true,
                buildings: [],
                meterid: null
            }
        },
        methods: {
            open(index) {
                this.meterid = null;
                this.$modal.show("meter-" + index, this.buildings[index].meters);
            },
            getreadings(meterid) {
                this.meterid = meterid;
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
                axios.get('http://localhost:5000/buildings/?page=' + page_num).then(
                    (response) => {
                        console.log(response.data.results);
                        this.buildings = response.data.results;
                        this.page = page_num;
                        this.hasNext = (response.data.next != null);
                    },
                    (error) => { console.log(error) }
                );
            }
        },
        created() {
            this.apiCall(this.page);
        }
    };
</script>
