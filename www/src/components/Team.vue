<template>
    <v-layout>
        <v-flex offset-xs4 sm6 style="margin:0 auto; margin-top:50px" xs12>
            <v-card class="mx-auto" max-width="500">
                <v-container fluid>
                    <v-row dense>
                        <v-col :cols="card.flex" :key="card.title" v-for="card in cards">
                            <v-card elevation="18">
                                <v-img
                                    :src="card.src"
                                    class="white--text align-end"
                                    gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                    height="200px"
                                >
                                    <v-card-title v-text="card.title"></v-card-title>
                                </v-img>
                            </v-card>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card>
        </v-flex>
    </v-layout>
</template>

<script>
export default {
    name: 'Team',
    data: () => ({
        cards: [
            {
                title: 'Dr Ketan Kotecha',
                src: require('../assets/images/ketan_sir.jpeg'),
                flex: 12,
            },
            {
                title: 'Dr Rahee Walambe',
                src: require('../assets/images/Rahee_maam.jpeg'),
                flex: 6,
            },
            {
                title: 'Ranjana Agrawal',
                src: require('../assets/images/Ranjna_maam.jpeg'),
                flex: 6,
            },
        ],
    }),
};
</script>

<style lang="scss" scoped>
</style>