import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Team from '../views/Team.vue';
import About from '../views/About.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home,
    },
    {
        path: '/team',
        name: 'team',
        component: Team,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: About,
    },
];

const router = new VueRouter({
    routes,
});

export default router;
