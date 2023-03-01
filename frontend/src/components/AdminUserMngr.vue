<template>
  <div class="container">
    <div class="tt-tab-wrapper">
      <div class="tt-wrapper-inner">
        <ul class="nav nav-tabs pt-tabs-default" role="tablist">
          <li class="nav-item tt-hide-xs show">
            <a
              class="nav-link active"
              data-toggle="tab"
              role="tab"
              style="padding-left: 16px; padding-right: 16px;"
            >
              <span>用户管理</span>
            </a>
          </li>
          <router-link to="/AdminThreadMngr">
            <li class="nav-item tt-hide-xs" style="padding-left: 0">
              <a
                class="nav-link"
                data-toggle="tab"
                role="tab"
                style="padding-left: 16px; padding-right: 16px;"
              >
                <span>帖子管理</span>
              </a>
            </li>
          </router-link>
        </ul>
      </div>
      <div class="tab-content">
        <div class="tab-pane tt-indent-none show active" id="tt-tab-02" role="tabpanel">
          <div class="tt-topic-list">
            <div class="tt-list-header">
              <div class="tt-col-value">uid</div>
              <div class="tt-col-value" style="padding-left: 18px;">头像</div>
              <div class="tt-col-topic">用户名</div>
              <div class="tt-col-category">最后活跃时间</div>
              <div class="tt-col-category">操作</div>
            </div>
            <div class="tt-item" v-for="banneduser in alluser.banned">
              <div class="tt-col-value">{{banneduser.ID}}</div>
              <div class="tt-col-avatar">
                <svg class="tt-icon">
                  <use xlink:href="#icon-ava-d" />
                </svg>
              </div>
              <div class="tt-col-description">
                <h6 class="tt-title">
                  <a>{{banneduser.Cname}}</a>
                </h6>
              </div>
              <div class="tt-col-category">{{new Date(banneduser.lastTime*1000).toLocaleString()}}</div>
              <div class="tt-col-category hide-mobile">
                <div class="tt-col-btn" id="js-settings-btn" style="zoom: 0.9;">
                  <div class="tt-list-btn">
                    <button
                      type="button"
                      class="btn btn-primary"
                      @click="opt('unban', banneduser.ID)"
                    >解禁</button>
                  </div>
                </div>
              </div>
            </div>
            <div class="tt-item" v-for="normaluser in alluser.normal">
              <div class="tt-col-value">{{normaluser.ID}}</div>
              <div class="tt-col-avatar">
                <svg class="tt-icon">
                  <use xlink:href="#icon-ava-d" />
                </svg>
              </div>
              <div class="tt-col-description">
                <h6 class="tt-title">
                  <a>{{normaluser.Cname}}</a>
                </h6>
              </div>
              <div class="tt-col-category">{{new Date(normaluser.lastTime*1000).toLocaleString()}}</div>
              <div class="tt-col-category hide-mobile">
                <div class="tt-col-btn" id="js-settings-btn" style="zoom: 0.9;">
                  <div class="tt-list-btn">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      @click="opt('ban', normaluser.ID)"
                    >禁言</button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      alluser: { banned: [], normal: [] }
    };
  },
  computed: {
    user: function() {
      if (this.$store.state.isLogin) {
        return this.$store.state.user;
      } else {
        alert("请登录后浏览！");
        this.$router.push({ path: "/AdminLogin" });
        return "未登录";
      }
    }
  },
  methods: {
    opt(o, uid) {
      var that = this;
      var str = "";
      if (o == "ban") {
        str = "adminban";
      }
      if (o == "unban") {
        str = "admin_remove_ban";
      }
      that.axios
        .get(`${that.user.sid}/${uid}/${str}`)
        .then(res => {
          console.log(res);
          if (res.data.status != 0) {
            alert("请求失败，原因：" + res.data.msg);
            return;
          }
          alert("操作成功！");
          location.reload();
        })
        .catch(err => {
          console.log(err);
          if (res.data.status != 0) {
            alert("操作失败，原因：" + err);
            return;
          }
        });
    }
  },
  mounted() {
    var that = this;
    if (that.$store.state.user.rank != "管理员") {
      alert("不合法的登录");
      this.$router.push({ path: "/AdminLogin" });
      return "未登录";
    } else {
      that.axios
        .get(`/${that.user.sid}/customer_show?t=${new Date().getTime()}`)
        .then(res => {
          console.log(res);
          if (res.data.status != 0) {
            alert("打开页面出错，原因：" + res.data.msg);
            return;
          }
          that.alluser.normal = res.data.data[0];
          that.alluser.banned = res.data.data[1];
        })
        .catch(err => {
          console.log(err);
          if (res.data.status != 0) {
            alert("打开页面出错，原因：" + err);
            return;
          }
        });
    }
  }
};
</script>

<style>
</style>