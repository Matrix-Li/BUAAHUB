<template>
  <div class="container">
    <div class="tt-tab-wrapper">
      <div class="tt-wrapper-inner">
        <ul class="nav nav-tabs pt-tabs-default" role="tablist">
          <router-link to="/AdminUserMngr">
            <li class="nav-item tt-hide-xs">
              <a
                class="nav-link"
                data-toggle="tab"
                role="tab"
                style="padding-left: 16px; padding-right: 16px;"
              >
                <span>用户管理</span>
              </a>
            </li>
          </router-link>
          <li class="nav-item tt-hide-xs show" style="padding-left: 0">
            <a
              class="nav-link active"
              data-toggle="tab"
              role="tab"
              style="padding-left: 16px; padding-right: 16px;"
            >
              <span>帖子管理</span>
            </a>
          </li>
        </ul>
      </div>
      <div class="tab-content">
        <div class="tab-pane tt-indent-none show active" id="tt-tab-02" role="tabpanel">
          <div class="tt-topic-list">
            <div class="tt-list-header">
              <div class="tt-col-topic">标题</div>
              <div class="tt-col-category">板块</div>
              <div class="tt-col-category">发帖时间</div>
              <div class="tt-col-value">操作</div>
            </div>
            <div class="tt-item" v-for="th in threads">
              <div class="tt-col-avatar">
                <svg class="tt-icon">
                  <use xlink:href="#icon-ava-d" />
                </svg>
              </div>
              <div class="tt-col-description">
                <h6 class="tt-title">
                  <a :href="'/topic?fid='+th.FID">{{th.title}}</a>
                </h6>
              </div>
              <div class="tt-col-category">
                <span :class="'tt-color0'+ th.module_id + ' tt-badge'">{{mods[th.module_id]}}</span>
              </div>
              <div class="tt-col-category">{{new Date(th.date*1000).toLocaleString()}}</div>
              <div class="tt-col-value hide-mobile">
                <div class="tt-col-btn" id="js-settings-btn" style="zoom: 0.9;">
                  <div class="tt-list-btn">
                    <button type="button" class="btn btn-secondary" @click="del(th.FID)">删除</button>
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
      threads: [],
      mods: [
        "无板块",
        "课程推荐",
        "刷题交流",
        "校园周边",
        "资源共享",
        "论坛公告"
      ]
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
    del(fid) {
      var that = this;
      that.axios
        .get(`${that.user.sid}/${fid}/admindelete`)
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
        .get(`/${that.user.sid}/allpost?t=${new Date().getTime()}`)
        .then(res => {
          console.log(res);
          if (res.data.status != 0) {
            alert("打开页面出错，原因：" + res.data.msg);
            return;
          }
          that.threads = res.data.data;
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