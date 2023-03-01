<template>
  <div class="tab-content">
    <div class="tab-pane tt-indent-none show active" id="tt-tab-01" role="tabpanel">
      <div class="tt-topic-list">
        <div class="tt-list-header">
          <div class="tt-col-topic">回复内容</div>
          <div class="tt-col-category hide-mobile">回复主题</div>
          <div class="tt-col-category hide-mobile">回复时间</div>
        </div>
        <div class="tt-item" v-for="coll in colls">
          <div class="tt-col-description" v-text="coll.information"></div>
          <div class="tt-col-category">
            <a :href="'/#/topic?fid='+coll.FID">{{coll.title}}</a>
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
  name: "UserReply",
  data() {
    return { colls: [] };
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
      .get(`/${sid}/mycomment`)
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