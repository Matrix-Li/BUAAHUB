<template>
  <div class="container">
    <div class="panel" style="padding-top: 2rem;">
      <div class="panel-header">
        <h3
          class="panel-header-title"
          style="color: red; font-size: 1.15rem; margin-bottom: 20px"
        >提示：您正在尝试以管理员身份登录。</h3>
      </div>
      <form class="form" action="javascript:void(0);">
        <div class="input">
          <label class="input-label">用户名</label>
          <input type="text" class="input-field" id="user_name" v-model="un" />
        </div>
        <div class="input">
          <label class="input-label">密码</label>
          <input type="password" class="input-field" id="user_pwd" v-model="pwd" />
        </div>
        <div class="input2">
          <b-button block variant="primary" @click="login">登&nbsp&nbsp录</b-button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
export default {
  name: "AdminLogin",
  data() {
    return {
      un: "",
      pwd: ""
    };
  },
  methods: {
    login() {
      this.admin_login_(this.un, this.pwd);
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../assets/login.css";
</style>
