import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    isLogin: false,
    user: {
      username: "",
      sid: "",
      rank: ""
    }
  },
  mutations: {
    setIsLogin(state, data) {
      state.isLogin = data;
    },
    setUser(state, data) {
      state.user = data;
    }
  },
  plugins: [createPersistedState()]
})

export default store

//使用方法
/* <script>
computed: { //获取状态
    count () {
      return store.state.count
    },
methods:{ //修改状态
    increment() {
        this.$store.commit('increment')
        console.log(this.$store.state.count)
    }
}
</script> */