<template>
    <v-app id="inspire">
        <v-navigation-drawer app clipped v-model="drawer">
            <v-list>
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

        <v-app-bar app clipped-left>
            <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
            <v-toolbar-title>BIO IMG SEGMENTATION</v-toolbar-title>
        </v-app-bar>

        <v-content>
            <router-view></router-view>
        </v-content>

        <v-footer app>
            <span>&copy; 2020</span>
        </v-footer>
    </v-app>
</template>

<script>
export default {
    props: {
        source: String,
    },

    data: () => ({
        drawer: null,
        items: [
            { title: 'SEGMENTATION', icon: 'mdi-call-split', route: '/' },
            { title: 'ABOUT', icon: 'mdi-message-text', route: '/about' },
            { title: 'TEAM', icon: 'mdi-account', route: '/team' },
        ],
    }),

    created() {
        this.$vuetify.theme.dark = true;
    },
};
</script>