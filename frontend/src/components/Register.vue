<template>
  <div id="registerComponent">
    <div class="container" style="margin: auto;">
      <div class="login_body l_clear">
        <div class="login_form l_float">
          <div class="login_top">
            <img src="../assets/imgs/logo_z.jpg" alt class />

            <div class="login_tags b_clear">
              <span class="top_tag l_float active">注册</span>
            </div>
          </div>
          <div class="login_con">
            <form action>
              <div>
                <label for="user_name">用户名</label>
                <input type="text" name id="user_name" v-model="userName" placeholder="网名/手机号/邮箱名" />
                <img src="../assets/imgs/icons/user.svg" />
              </div>
              <div>
                <label for="user_pwd">密码</label>
                <input type="password" name id="user_pwd" v-model="password1" placeholder="请输入账户密码" />
                <img src="../assets/imgs/icons/lock.svg" />
              </div>
              <div class="b_clear">
                <label for="user_pwd2" class="b_clear">再次输入密码</label>
                <input
                  type="password"
                  name
                  id="user_pwd2"
                  v-model="password2"
                  placeholder="请再次输入账户密码"
                  class="l_float"
                />
                <img src="../assets/imgs/icons/lock.svg" />
              </div>
              <div class="tt-col-btn" id="js-settings-btn" style="zoom: 0.9">
                <div class="tt-list-btn">
                  <button
                    type="button"
                    class="btn btn-secondary"
                    style="padding: 20px; border-radius: 8px;"
                    @click="register"
                  >注&nbsp;&nbsp;册</button>
                </div>
              </div>
            </form>
          </div>
        </div>
        <div class="login_ad l_float" id="AdImg">
          <a style="display: none">查看详情</a>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "register.vue",
  data() {
    return {
      userName: "",
      password1: "",
      password2: "",
      tips: [false, false, false]
    };
  },
  methods: {
    register() {
      this.register_(this.userName, this.password1, this.password2);
    }
  }
};
</script>

<style scoped>
@import "../assets/login.css";
#registerComponent {
  background-color: #ffffff;
}
* {
  margin: 0;
  padding: 0;
}
.l_float {
  float: left;
}

.l_clear {
  clear: left;
  display: block;
  overflow: hidden;
  content: "";
}

.b_clear {
  clear: both;
  display: block;
  overflow: hidden;
  content: "";
}

.container > .login_body {
  width: 1000px;
  padding-top: 80px;
  padding-bottom: 40px;
}
.container > .login_body > .login_form {
  width: 300px;
}

.container > .login_body > .login_form > .login_top,
.container > .login_body > .login_form > .login_con {
  background-color: #ffffff;
}

.container > .login_body > .login_form > .login_top {
  padding: 20px 30px 10px 30px;
  border-top-left-radius: 10px;
}

.container > .login_body > .login_form > .login_top > img {
  height: 40px;
}

.container > .login_body > .login_form > .login_top > .login_tags {
  padding: 10px 0 0;
}

.container > .login_body > .login_form > .login_top > .login_tags > span {
  padding: 10px;
  text-align: center;
  width: 50%;
  box-sizing: border-box;
  border-bottom: 1px solid #d9d9d9;
}

.container > .login_body > .login_form > .login_top > .login_tags > .active {
  border-bottom: 2px solid #703eff;
}

.container > .login_body > .login_form > .login_con {
  padding: 20px 30px;
}

.container > .login_body > .login_form > .login_con > form > div {
  padding-bottom: 20px;
  position: relative;
}

.container > .login_body > .login_form > .login_con > form > div > img {
  width: 24px;
  position: absolute;
  bottom: 32px;
  left: 0;
}

.container > .login_body > .login_form > .login_con > form > div > label {
  font-size: 14px;
  float: left;
}

.container > .login_body > .login_form > .login_con > form > div > input {
  display: block;
  margin-top: 10px;
}

.container
  > .login_body
  > .login_form
  > .login_con
  > form
  > div
  > input[type="text"],
.container
  > .login_body
  > .login_form
  > .login_con
  > form
  > div
  > input[type="password"],
.container
  > .login_body
  > .login_form
  > .login_con
  > form
  > div
  > button[type="submit"] {
  padding: 0 28px;
  outline: none;
  height: 40px;
  width: 220px;
  border: none;
  border-bottom: 2px solid #703eff;
  color: #333;
  font-size: 16px;
}

.container
  > .login_body
  > .login_form
  > .login_con
  > form
  > div
  > button[type="submit"] {
  background-color: #703eff;
  width: 120px;
  border-radius: 50px;
  border-bottom: none;
  cursor: pointer;
  font-size: 16px;
  color: #fff;
  text-align: center;
  font-weight: bold;
}

.container
  > .login_body
  > .login_form
  > .login_con
  > form
  > div
  > button[type="submit"]:hover {
  background-color: #5e2fe7;
}

.container > .login_body > .login_form > .login_con > form > div > a {
  font-size: 12px;
  line-height: 40px;
}

.container > .login_body > .login_form > .login_con > .qr_code > img {
  width: 140px;
}

.container > .login_body > .login_form > .login_con > .qr_code > p {
  font-size: 12px;
  margin-top: 10px;
}

.container > .login_body > .login_form > .login_otherAccount {
  padding: 12px 20px;
  font-size: 12px;
  border-top: 1px solid #d9d9d9;
  background-color: #fafbfc;
  border-bottom-left-radius: 10px;
}
.container > .login_body > .login_form > .login_otherAccount > span {
  margin-right: 4px;
}

.container > .login_body > .login_form > .login_otherAccount > a {
  margin-right: 2px;
}
.container > .login_body > .login_form > .login_otherAccount > a > img {
  height: 24px;
  vertical-align: middle;
}

.container > .login_body > .login_ad {
  width: 700px;
  height: 558px;
  overflow: hidden;
  background-image: url("../assets/imgs/timg.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  position: relative;
  text-align: center;
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
  box-shadow: 0 0 16px 0 rgba(0, 0, 0, 0.35);
}
.container > .login_body > .login_ad > a {
  border-radius: 50px;
  position: absolute;
  bottom: 15.5%;
  left: 296px;
  padding: 10px 20px;
  text-decoration: none;
  background-color: #703eff;
  color: #fff;
  font-size: 14px;
  border: 1px solid #703eff;
}
.container > .login_body > .login_ad > a:hover {
  background-color: #fff;
  border: 1px solid #703eff;
  color: #703eff;
}
.container > .login_body > .login_form > .login_otherAccount {
  padding: 12px 20px;
  font-size: 12px;
  border-top: 1px solid #d9d9d9;
  background-color: #fafbfc;
  border-bottom-left-radius: 10px;
}
.container > .login_body > .login_form > .login_otherAccount > span {
  margin-right: 4px;
}

.container > .login_body > .login_form > .login_otherAccount > a {
  margin-right: 2px;
}
.container > .login_body > .login_form > .login_otherAccount > a > img {
  height: 24px;
  vertical-align: middle;
}
</style>

