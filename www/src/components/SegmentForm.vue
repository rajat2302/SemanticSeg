<template>
    <v-container>
        <div>
            <v-alert
                border="left"
                colored-border
                dismissible
                elevation="2"
                type="error"
                v-model="isError"
            >{{errorMsg}}</v-alert>
        </div>

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
                            <v-tooltip right>
                                <template v-slot:activator="{ on }">
                                    <v-btn
                                        @click="onPickFile"
                                        class="ma-2 white--text"
                                        color="blue"
                                        fab
                                        style="margin-top:100px"
                                        v-on="on"
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
                                </template>
                                <span>Upload a clear retinal fundus image(png/jpeg) for segmentation</span>
                            </v-tooltip>
                        </div>
                        <div style="margin-top:35px" v-else-if="!!imageUrl & !output & !errorMsg">
                            <v-btn
                                :loading="segmenting"
                                @click="callSeg"
                                class="primary"
                                raised
                                rounded
                            >Segment Image</v-btn>
                        </div>
                        <div style="margin-top:35px" v-else-if="!!output | !!errorMsg">
                            <v-btn @click="setDefault" class="primary" rounded>Reset</v-btn>
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
        isError: false,
        errorMsg: '',
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
                    console.log(response.status);
                    console.log(response);
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
                    that.isError = true;
                    that.errorMsg = 'Something went wrong while processing the image!';
                    that.segmenting = false;
                });
        },
        setDefault: function() {
            this.output = '';
            this.imageUrl = '';
            this.image = '';
            this.isError = false;
            this.errorMsg = '';
        },
    },
};
</script>
