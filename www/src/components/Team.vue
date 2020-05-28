<template>
    <v-layout>
        <v-flex offset-xs4 sm8 style="margin:0 auto; margin-top:25px" xs12>
            <v-container fluid>
                <v-row dense>
                    <v-col :cols="card.flex" :key="card.title" v-for="card in cards">
                        <v-card class="mx-auto" light max-width="344" width="344px">
                            <v-img
                                :src="card.src"
                                class="white--text align-end"
                                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                                height="280px"
                                sm6cd
                            ></v-img>
                            <v-card-title v-text="card.title"></v-card-title>
                            <v-card-subtitle v-text="card.descn"></v-card-subtitle>
                        </v-card>
                    </v-col>
                </v-row>
            </v-container>
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
                descn: 'Director @SIT - Project Mentor',
                src: require('../assets/images/ketan_sir.jpeg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
            {
                title: 'Dr Rahee Walambe',
                descn: 'Ass. Proffesor @SIT - Project Mentor',
                src: require('../assets/images/Rahee_maam.jpeg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
            {
                title: 'Ranjana Agrawal',
                descn: 'Lecturar @MIT - Project Mentor',
                src: require('../assets/images/Ranjna_maam.jpeg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
            {
                title: 'Akash Dholaria',
                descn: 'CS Student @SIT',
                src: require('../assets/images/akash.jpeg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
            {
                title: 'Gauri Nigam',
                descn: 'CS Student @SIT',
                src: require('../assets/images/gauri.jpeg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
            {
                title: 'Rajat Pandey',
                descn: 'IT Student @SIT',
                src: require('../assets/images/rajat.jpg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
            {
                title: 'Shambhavi Tiwari',
                descn: 'IT Student @SIT',
                src: require('../assets/images/shambhu.jpeg'),
                flex: 'window.innerWidth<668 ? 4 : 12',
            },
        ],
    }),
};
</script>

<style lang="scss" scoped>
</style>