<template>
  <div class="container">
    <div :class="{'shadow':popup}">
      <div class="tt-tab-wrapper">
        <div class="tt-user-header">
          <div class="tt-col-avatar">
            <div class="tt-icon">
              <svg class="tt-icon">
                <use xlink:href="#icon-user" />
              </svg>
            </div>
          </div>
          <div class="tt-col-title">
            <div class="tt-title">尊敬的{{username}}，您好！您当前等级为：</div>
            <ul class="tt-list-badge">
              <li>
                <span class="tt-color14 tt-badge">{{rank}}</span>
              </li>
            </ul>
            <div class="tt-title">在论坛中发帖、回帖、点赞等可提升等级。请保持活跃！</div>
          </div>
          <div class="tt-col-btn" id="js-settings-btn" style="zoom: 0.9; margin-right: 30px">
            <div class="tt-list-btn">
              <button type="button" class="btn btn-secondary" @click="popup=true">修改密码</button>
            </div>
          </div>
        </div>
      </div>
      <div class="tt-tab-wrapper">
        <div class="tt-wrapper-inner">
          <ul class="nav nav-tabs pt-tabs-default" role="tablist">
            <li class="nav-item" @click="curTab=0">
              <a
                :class="{'nav-link':true, 'active':curTab==0}"
                style="cursor: pointer"
                data-toggle="tab"
                role="tab"
              >
                <span style="margin-left: 16px">
                  <a class="link">我的主题</a>
                </span>
              </a>
            </li>
            <li class="nav-item" @click="curTab=1">
              <a
                :class="{'nav-link':true, 'active':curTab==1}"
                style="cursor: pointer"
                data-toggle="tab"
                role="tab"
              >
                <span>
                  <a class="link">我的回复</a>
                </span>
              </a>
            </li>

            <li class="nav-item tt-hide-md" @click="curTab=2">
              <a
                :class="{'nav-link':true, 'active':curTab==2}"
                style="cursor: pointer"
                data-toggle="tab"
                role="tab"
              >
                <span style="margin-right: 16px">
                  <a class="link">我的收藏</a>
                </span>
              </a>
            </li>
          </ul>
        </div>
      </div>
      <UserTiezi v-if="curTab==0" />
      <UserReply v-if="curTab==1" />
      <UserCollect v-if="curTab==2" />
    </div>
    <div id="js-popup-settings" :class="{'tt-popup-settings':true, 'column-open':popup}">
      <div class="tt-btn-col-close">
        <a @click="popup=false" style="cursor: pointer">
          <span class="tt-icon-title">
            <svg>
              <use xlink:href="#icon-settings_fill" />
            </svg>
          </span>
          <span class="tt-icon-text">修改密码</span>
          <span class="tt-icon-close">
            <svg>
              <use xlink:href="#icon-cancel" />
            </svg>
          </span>
        </a>
      </div>
      <form class="form-default">
        <div class="form-group">
          <label for="settingsUserName">旧密码</label>
          <input
            type="password"
            name="name"
            class="form-control"
            id="settingsUserName"
            placeholder="请输入您的旧密码"
            v-model="pwd.oldp"
          />
        </div>
        <div class="form-group">
          <label for="settingsUserEmail">新密码</label>
          <input
            type="password"
            name="name"
            class="form-control"
            id="settingsUserEmail"
            placeholder="请输入您的新密码"
            v-model="pwd.newp"
          />
        </div>
        <div class="form-group">
          <label for="settingsUserPassword">确认新密码</label>
          <input
            type="password"
            name="name"
            class="form-control"
            id="settingsUserPassword"
            placeholder="请确认您的新密码"
            v-model="pwd.newprep"
          />
        </div>
        <div class="form-group" style="margin-top: 30px">
          <button type="button" class="btn btn-secondary" @click="updatePwd()">更新密码</button>
        </div>
      </form>
    </div>
  </div>
</template>


<script>
import Vue from "vue";
import UserTiezi from "./UserTiezi";
import UserReply from "./UserReply";
import UserCollect from "./UserCollect";

export default {
  name: "User",
  components: { UserTiezi, UserReply, UserCollect },
  data() {
    return {
      curTab: 0,
      popup: false,
      pwd: { oldp: "", newp: "", newprep: "" }
    };
  },
  computed: {
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
  },
  methods: {
    updatePwd() {
      var that = this;
      let sid = that.$store.state.user.sid;

      if (that.pwd.newp != that.pwd.newprep) {
        alert("两次输入的密码不一致，请检查！");
        return;
      }

      that.axios
        .get(`/${sid}/change?ps1=${that.pwd.oldp}&ps2=${that.pwd.newp}`)
        .then(function(response) {
          console.log(response);
          if (response.data.status == 0) {
            alert("成功修改密码。");
            location.reload();
          } else {
            alert("修改密码失败，原因：" + response.data.msg);
          }
        })
        .catch(function(error) {
          console.log(error);
          alert("请求修改密码时遇到了错误");
        });
    }
  },
  mounted() {
    var that = this;
    let sid = that.$store.state.user.sid;
    let un = that.$store.state.user.username;

    that.axios
      .get(`/${sid}/myrank`)
      .then(function(response) {
        console.log(response);
        if (response.data.status == 0) {
          //设置全局状态（支持双向绑定的全局变量）
          that.$store.commit("setUser", {
            //用户信息
            username: un,
            sid: sid,
            rank: response.data.data.rank
          });
        }
      })
      .catch(function(error) {
        console.log(error);
      });
  }
};
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../assets/user.css";
.shadow {
  filter: blur(15px);
}
</style>
