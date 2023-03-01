<template>
  <div class="container">
    <div class="tt-topic-list">
      <div class="tt-list-header">搜索结果：{{searchWord}}</div>
      <div class="tt-list-header">
        <div class="tt-col-topic">主题</div>
        <div class="tt-col-category">板块</div>
        <div class="tt-col-value">喜欢</div>
        <div class="tt-col-value">回复</div>
        <div class="tt-col-value">浏览</div>
        <div class="tt-col-value">活跃时间</div>
      </div>
      <div class="postList" v-for="post in postList">
        <div class="tt-item">
          <div class="tt-col-avatar">
            <svg class="tt-icon">
              <use :href="'#icon-ava-'+post['author'][0]"></use>
            </svg>
          </div>
          <div class="tt-col-description">
            <h6 class="tt-title" >
              <a v-on:click="openPost(post)">
                {{post['title']}}
              </a>
            </h6>
          </div>
          <div class="tt-col-category"><span :class="chooseColor(post['MOID'])">{{postType[post['MOID']]}}</span></div>
          <div class="tt-col-value">{{post['likeCnt']}}</div>
          <div class="tt-col-value tt-color-select">{{post['commentnumber']}} </div>
          <div class="tt-col-value">{{post['views']}}</div>
          <div class="tt-col-value">{{getTime(post)}} {{post['lastestname']}}</div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
    export default {
      name: "PostListPage",
      data(){
          return {
            searchWord: this.$route.query.searchWord,
            postList: [],
            postType: [
              "主页",
              "课程推荐",
              "刷题交流",
              "校园周边",
              "资源共享",
              "论坛公告"],
            colorType:[
              "tt-color01",
              "tt-color02",
              "tt-color03",
              "tt-color04",
              "tt-color05",
              "tt-color06"]
          }
      },
      mounted: function() {
        var that = this;
        var con = this.searchWord;
        if(!that.$store.state.isLogin){
          alert("请先登录");
          this.$router.push('/Login');
        }
        that.axios
          // .get("/" + this.$store.state.user.sid + "/" + "search")
          .get(
            `/${that.$store.state.user.sid}/search?con=${con}`,
            {
              con: con
            }
          )
          .then(function(response) {
            if(response.data.status == 0){
              that.postList = response.data.data[1];
            }
            else if(response.data.status == 1){
              alert("用户不存在");
            }
            else if(response.data.status == 2){
              alert("SID有误");
            }
            else if(response.data.status == 3){
              alert("无操作超过一小时，已自动注销");
              that.$router.push('/Login');
            }
            else if(response.data.status == 4){
              alert("查询为空");
            }
            else{
              alert("出现错误，原因：" + response.data.status + ";"+ response.data.msg);
            }
          })
          .catch(function(error) {
            alert(error);
          });
      },
      methods:{
        getTime: function (post) {
          var date;
          if('lastestTime' in post){
            date = new Date(post['lastestTime']*1000);
          }
          else date = new Date(post['time']*1000);
          var curDate = new Date();
          var month1 = date.getMonth(), month2 = curDate.getMonth();
          var day1 = date.getUTCDate(), day2 = curDate.getUTCDate();
          if(month1 !== month2){
            return month1 + "月" + day1 + "日";
          }
          if(Math.abs(day1 - day2) < 7 && Math.abs(day1 - day2) > 0){
            return Math.abs(day1 - day2) + "天前";
          }
          return "今天" + date.getHours() + ":" + date.getMinutes();
        },
        chooseColor: function(num){
          return this.colorType[num] + " tt-badge";
        },
        openPost: function (post) {
          // console.log(post);
          this.$router.push(`/topic?fid=${post['ID']}`);
        }
      }
    }
</script>

<style scoped>
  @import "../assets/style.css";
</style>
