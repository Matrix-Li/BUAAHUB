<template>
  <div class="header">
    <div class="container">
      <div id="logo">
        <router-link to="/">
          <img src="/static/buaa_hub.png" alt />
        </router-link>
      </div>
      <div id="avatar">
        <b-list-group style="max-width: 300px; min-width: 170px;">
          <b-list-group-item class="d-flex align-items-center">
            <router-link to="/User">
              <b-avatar class="mr-3"></b-avatar>
            </router-link>
            <span class="mr-auto">
              <router-link to="/login" style="margin-right: 15px">{{username}}</router-link>
            </span>
            <b-badge>{{rank}}</b-badge>
          </b-list-group-item>
        </b-list-group>
      </div>
      <div class="newPost">
        <router-link :to="{path: '/createTopic'}">
          <a href="#" class="tt-btn-create-topic" style="top: auto; bottom: 60px; right: 60px">
            <span class="tt-icon">
              <svg>
                <use xlink:href="#icon-create_new" />
              </svg>
            </span>
          </a>
        </router-link>
      </div>
      <div id="clear"></div>
    </div>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  computed: {
    //读取全局状态（支持双向绑定的全局变量）
    username: function() {
      if (this.$store.state.isLogin) {
        return this.$store.state.user.username;
      } else return "未登录";
    },
    rank: function() {
      if (this.$store.state.isLogin) {
        return this.$store.state.user.rank;
      } else return "0";
    }
  }
};
</script>

<style scoped>
#logo {
  float: left;
  /* margin-left: 3%; */
}
#logo img {
  width: 192px;
  height: 96px;
  vertical-align: middle;
}
#avatar {
  float: right;
  margin-top: 10px;
}
#clear {
  clear: both;
}
.header {
  margin-bottom: 25px;
}
</style>
