import { createRouter, createWebHistory } from "vue-router";

import MainPage from "./views/MainPage.vue";
import LoginPage from "./views/LoginPage.vue";
import RegisterPage from "./views/RegisterPage.vue";
import AboutPage from "./views/AboutPage.vue";
import UserTimetablesPage from "./views/UserTimetablesPage.vue";
import TimetablePage from "./views/TimetablePage.vue";
import CreateTimetablePage from "./views/CreateTimetablePage.vue";
import NotFoundPage from "./views/NotFoundPage.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: "/", component: MainPage },
    { path: "/login", component: LoginPage },
    { path: "/register", component: RegisterPage },
    { path: "/about", component: AboutPage },
    { path: "/create", component: CreateTimetablePage },
    { path: "/:email", component: UserTimetablesPage, props: true },
    { path: "/:email/:name", component: TimetablePage, props: true },
    { path: "/:pathMatch(.*)*", component: NotFoundPage },
  ],
});
