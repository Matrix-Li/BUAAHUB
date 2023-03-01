<template>
  <div class="tab-content">
    <div class="tab-pane tt-indent-none show active" id="tt-tab-01" role="tabpanel">
      <div class="tt-topic-list">
        <div class="tt-list-header">
          <div class="tt-col-topic">帖子标题</div>
          <div class="tt-col-category hide-mobile">所属板块</div>
          <div class="tt-col-category hide-mobile">发帖时间</div>
          <div class="tt-col-category hide-mobile">操作</div>
        </div>
        <div class="tt-item" v-for="coll in colls">
          <div class="tt-col-description">
            <a :href="'/#/topic?fid='+coll.FID">{{coll.title}}</a>
          </div>
          <div class="tt-col-category">
            <span :class="'tt-color0'+ coll.module_id + ' tt-badge'">{{mods[coll.module_id]}}</span>
          </div>
          <div class="tt-col-category">{{new Date(coll.date*1000).toLocaleString()}}</div>
          <div class="tt-col-category">
            <div class="tt-col-btn" id="js-settings-btn" style="zoom: 0.9;">
              <div class="tt-list-btn">
                <button type="button" class="btn btn-secondary" @click="cancel(coll.FID)">取消收藏</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>



<script>
import Vue from "vue";

export default {
  name: "UserCollect",
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
  methods: {
    cancel(fid) {
      var that = this;
      that.axios
        .get(`${that.$store.state.user.sid}/${fid}/cancel_collect`)
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
    let sid = that.$store.state.user.sid;
    that.axios
      .get(`/${sid}/returncollection`)
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