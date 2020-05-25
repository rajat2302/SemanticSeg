<template>
    <v-row>
        <v-card
            class="mx-auto"
            elevation="18"
            max-width="600"
            outlined
            style="margin:0 auto; margin-top:50px;"
        >
            <v-card-text>
                <div class="headline mb-1" style="text-align:left">Biomedical Image Segmentation</div>
                <br />
                <div style="text-align:left">
                    <p>
                        The application puts in use the practicality of the algorithm and model to segment the blood vessels of retinal fundus images.
                        The U-Net architecture used help in training the model despite the low amount of images found and fed into it.
                        The datasets used have about images anywhere between 40-45 images, which are classified correctly to about an accuracy of 96-97%.
                        This web application puts all the training and complexity of the model in the background.
                        <br />
                        <br />The model follows several layers of architecture that involves fully convolutions networks.
                        This was made to keep in mind the development in technology and the issues faced with detecting various diseases that grow with time and a limited workforce.
                        Which is why applications like these can lead to major breakthroughs in terms of saving time and better results in history of medical technological advancements.
                        The images are resized to fixed values before being passed into the model.
                        It helps any user without any prior knowledge of the research, work around the application to get a successfully segmented image as the output after feeding an input image.
                        <br />
                        <br />The application is made using flask and python and helps users be well acquainted with the front end of the software.
                        The user is particularly not troubled about the niche particulars of the code as the applications take care of those in the background, and gives the right user experience.
                        Proper analysis and predictions can be made once the segmented image is received.
                    </p>
                </div>
                <div style="text-align:left">{{desc1}}</div>
                <div style="text-align:left">{{desc2}}</div>
            </v-card-text>
        </v-card>
    </v-row>
</template>

<script>
export default {
    data: () => ({}),
};
</script>

<style lang="scss" scoped>
</style>