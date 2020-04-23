<template>
    <div class="container">
        <div class="large-12 medium-12 small-12 cell">
            <label>
                Select data to upload: <dropdown :options="listOfModels" :selected="selectedModel" v-on:updateOption="onSelectMethod"></dropdown>
            </label>
        </div>
        <div class="large-12 medium-12 small-12 cell">
            <label>
                File <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
            </label>
            <button v-on:click="submitFile()">Submit</button>
            <div>{{result}}</div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios';
    import dropdown from 'vue-dropdowns';

    export default {
        name: 'BuildingUpload',
        data() {
            return {
                file: '',
                result: '',
                listOfModels: [
                    {name: 'buildings'}, 
                    {name: 'meters'},
                    {name: 'readings'}
                ],
                selectedModel: {
                    name: 'buildings',
                }
            }
        },
        components: {
            'dropdown': dropdown,
        },
        methods: {
            submitFile() {
                let formData = new FormData();
                formData.append('file', this.file);
                
                axios.post(
                    'http://localhost:5000/' + this.selectedModel.name + '-upload/', formData,
                    {
                        headers: {
                            'Content-Type': 'multipart/form-data'
                        }
                    }
                ).then((response) => {
                    this.result = "SUCCESS";
                }, (error) => {
                    this.result = error;
                }).catch(function(err) {
                    console.log(err);
                });
            },

            handleFileUpload() {
                this.file = this.$refs.file.files[0];
            },
        
            onSelectMethod(payload) {
                this.selectedModel = payload;
            }
        }
    }
</script>
