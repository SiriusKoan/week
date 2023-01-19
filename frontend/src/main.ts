import { createApp } from "vue";
import App from "./App.vue";
import { router } from "./route";
import { initializeApp } from "firebase/app";

const FIREBASE_APIKEY = import.meta.env.VITE_FIREBASE_APIKEY
const FIREBASE_AUTHDOMAIN = import.meta.env.VITE_FIREBASE_AUTHDOMAIN
const FIREBASE_DATABASEURL = import.meta.env.VITE_FIREBASE_DATABASEURL
const FIREBASE_PROJECTID = import.meta.env.VITE_FIREBASE_PROJECTID
const FIREBASE_STORAGE_BUCKET = import.meta.env.VITE_FIREBASE_STORAGE_BUCKET
const FIREBASE_MESSAGING_SENDER_ID = import.meta.env.VITE_FIREBASE_MESSAGING_SENDER_ID
const FIREBASE_APPID = import.meta.env.VITE_FIREBASE_APPID
const firebaseConfig = {
  apiKey: FIREBASE_APIKEY,
  authDomain: FIREBASE_AUTHDOMAIN,
  databaseURL: FIREBASE_DATABASEURL,
  projectId: FIREBASE_PROJECTID,
  storageBucket: FIREBASE_STORAGE_BUCKET,
  messagingSenderId: FIREBASE_MESSAGING_SENDER_ID,
  appId: FIREBASE_APPID,
};

initializeApp(firebaseConfig);

const app = createApp(App).use(router);
app.mount("#app");
