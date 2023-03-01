<template>
  <div class="tab-content">
    <div class="tab-pane tt-indent-none show active" id="tt-tab-01" role="tabpanel">
      <div class="tt-topic-list">
        <div class="tt-list-header">
          <div class="tt-col-topic">帖子标题</div>
          <div class="tt-col-category hide-mobile">所属板块</div>
          <div class="tt-col-category hide-mobile">发帖时间</div>
        </div>
        <div class="tt-item" v-for="coll in colls">
          <div class="tt-col-description">
            <a :href="'/#/topic?fid='+coll.FID">{{coll.title}}</a>
          </div>
          <div class="tt-col-category">
            <span :class="'tt-color0'+ coll.module_id + ' tt-badge'">{{mods[coll.module_id]}}</span>
          </div>
          <div class="tt-col-category">{{new Date(coll.date*1000).toLocaleString()}}</div>
        </div>
      </div>
    </div>
  </div>
</template>





<script>
import Vue from "vue";

export default {
  name: "UserTiezi",
  data() {
    return {
      colls: [],
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
  mounted() {
    var that = this;
    let sid = that.$store.state.user.sid;
    that.axios
      .get(`/${sid}/mypost`)
      .then(function(response) {
        console.log(response);
        if (response.data.status == 0) {
          that.colls = response.data.data;
        } else {
          alert("获取主题失败，原因：" + response.data.msg);
          that.$router.push({ path: "/" });
        }
      })
      .catch(function(error) {
        console.log(error);
        alert("请求主题时遇到了错误");
      });
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../assets/user.css";
</style>