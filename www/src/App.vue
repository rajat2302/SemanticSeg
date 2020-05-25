<template>
    <v-app>
        <v-container>
            <v-card class="overflow-hidden" style="min-height:100vh">
                <v-navigation-drawer
                    :color="color"
                    :expand-on-hover="expandOnHover"
                    :mini-variant="miniVariant"
                    :permanent="permanent"
                    :right="right"
                    :src="bg"
                    absolute
                    dark
                    v-model="drawer"
                >
                    <v-list class="py-0" dense nav>
                        <v-list-item :class="miniVariant && 'px-0'" two-line>
                            <v-avatar color="indigo" size="25" style="margin-right:10px">
                                <v-icon dark>mdi-account-circle</v-icon>
                            </v-avatar>

                            <v-list-item-content>
                                <v-list-item-title>Segmentation</v-list-item-title>
                                <v-list-item-subtitle>U-Net</v-list-item-subtitle>
                            </v-list-item-content>
                        </v-list-item>

                        <v-divider></v-divider>
                        <router-link :key="item.title" :to="item.route" link v-for="item in items">
                            <v-list-item>
                                <v-list-item-icon>
                                    <v-icon>{{ item.icon }}</v-icon>
                                </v-list-item-icon>

                                <v-list-item-content>
                                    <v-list-item-title>{{ item.title }}</v-list-item-title>
                                </v-list-item-content>
                            </v-list-item>
                        </router-link>
                    </v-list>
                </v-navigation-drawer>
                <v-layout class="app-page">
                    <v-flex class="text-center" xs12>
                        <router-view></router-view>
                    </v-flex>
                </v-layout>
            </v-card>
        </v-container>
    </v-app>
</template>

<script>
export default {
    name: 'App',

    data() {
        return {
            title: 'Samentic Segmentation',
            drawer: true,
            items: [
                { title: 'Segment', icon: 'mdi-view-dashboard', route: '/' },
                { title: 'Supervisor', icon: 'mdi-image', route: '/team' },
                { title: 'About', icon: 'mdi-help-box', route: '/about' },
            ],
            color: 'primary',
            colors: ['primary', 'blue', 'success', 'red', 'teal'],
            right: false,
            permanent: true,
            miniVariant: false,
            expandOnHover: true,
            background: true,
        };
    },
    computed: {
        bg() {
            return this.background
                ? 'https://cdn.vuetifyjs.com/images/backgrounds/bg-2.jpg'
                : undefined;
        },
    },
};
</script>

<style>
.v-application--is-ltr .v-list-item__action:first-child,
.v-application--is-ltr .v-list-item__icon:first-child {
    margin-right: 10px !important;
}
.app-page {
    margin-left: 56px;
    transition: all 0.1s ease-out;
}
@media screen and (min-width: 768px) {
    .v-navigation-drawer--is-mouseover ~ .app-page {
        margin-left: 256px;
    }
}
.v-application--wrap {
    max-width: 968px !important;
    margin: 0 auto;
}
</style>
