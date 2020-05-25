<template>
    <v-container>
        <v-row class="text-center">
            <v-col cols="12">
                <v-layout v-if="imageUrl">
                    <v-flex style="margin-top:50px" text-center xs12>
                        <v-row class="text-center">
                            <div :class="!!output ? '' : 'col-sm-12'" class="col-xs-12 col-sm-6">
                                <v-card elevation="18" light max-width="252" style="margin:0 auto">
                                    <img :src="imageUrl" style="width:252px; height:252px;" />
                                    <v-card-subtitle>
                                        <b>RETINAL FUNDUS</b>
                                    </v-card-subtitle>
                                </v-card>
                            </div>
                            <div class="col-xs-12 col-sm-6" v-if="!!output">
                                <v-card elevation="18" light max-width="252" style="margin: 0 auto">
                                    <img :src="output" style="width:252px; height:252px;" />
                                    <v-card-subtitle>
                                        <b>SEGMENTED IMAGE</b>
                                    </v-card-subtitle>
                                </v-card>
                            </div>
                        </v-row>
                    </v-flex>
                </v-layout>
                <v-layout row>
                    <v-flex text-center xs12>
                        <div style="margin-top:100px" v-if="imageUrl==''">
                            <v-btn
                                @click="onPickFile"
                                class="ma-2 white--text"
                                color="blue"
                                fab
                                style="margin-top:100px"
                                x-large
                            >
                                <v-icon dark>mdi-cloud-upload</v-icon>
                            </v-btn>
                            <input
                                @change="onFilePicked"
                                accept="image/*"
                                ref="fileInput"
                                style="display: none"
                                type="file"
                            />
                        </div>
                        <div style="margin-top:35px" v-else-if="imageUrl">
                            <v-btn
                                :loading="segmenting"
                                @click="callSeg"
                                class="primary"
                                raised
                                rounded
                            >Segment Image</v-btn>
                        </div>
                    </v-flex>
                </v-layout>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
import axios from 'axios';
export default {
    name: 'HelloWorld',

    data: () => ({
        image: '',
        imageUrl: '',
        output: '',
        segmenting: false,
    }),
    methods: {
        onPickFile: function() {
            this.$refs.fileInput.click();
        },
        onFilePicked: function(event) {
            const files = event.target.files;
            let filename = files[0].name;
            if (filename.lastIndexOf('.') <= 0) {
                return alert('Please add a valid file!');
            }
            const fileReader = new FileReader();
            fileReader.addEventListener('load', () => {
                //console.log(fileReader.result);
                this.imageUrl = fileReader.result;
            });
            fileReader.readAsDataURL(files[0]);
            console.log(files[0]);
            this.image = files[0];
        },
        callSeg: function() {
            const path = '/uploader';
            let that = this;
            this.segmenting = true;
            var formData = new FormData();
            formData.append('file', this.image);
            axios
                .post(path, formData, {
                    responseType: 'arraybuffer',
                    headers: { 'Content-Type': 'multipart/form-data' },
                })
                .then(function(response) {
                    let blob = new Blob([response.data], {
                        type: response.headers['content-type'],
                    });
                    let image = URL.createObjectURL(blob);
                    console.log(image);
                    console.log(that);
                    that.output = image;
                    that.segmenting = false;
                })
                .catch(function(error) {
                    console.log(error);
                    that.segmenting = false;
                });
        },
    },
};
</script>
