<template>
  <div class="container">
    <div class="tt-categories-title">
      <div class="tt-title">板块列表</div>
      <div class="tt-search">
        <form class="search-wrapper">
          <div class="search-form">
            <input type="text" v-model="searchWord" class="tt-search__input" placeholder="搜索..." />
            <router-link :to="{path:'/PostListPage', query:{searchWord:this.searchWord}}">
              <button class="tt-search__btn" type="submit">
                <svg class="tt-icon">
                  <use xlink:href="#icon-search" />
                </svg>
              </button>
            </router-link>
            <button class="tt-search__close">
              <svg class="tt-icon">
                <use xlink:href="#icon-cancel" />
              </svg>
            </button>
          </div>
        </form>
      </div>
    </div>
    <div class="tt-categories-list">
      <div class="row">
        <div class="col-md-6 col-lg-4" v-for="sec in secs">
          <div class="tt-item">
            <div class="tt-item-header">
              <ul class="tt-list-badge">
                <li>
                  <router-link :to="{path:'/SectionPostListPage', query:{id: sec.id}}">
                    <span :class="chooseColor(sec.id)">{{sec.name}}</span>
                  </router-link>
                </li>
              </ul>
              <h6 class="tt-title">
                <router-link :to="{path:'/SectionPostListPage', query:{id: sec.id}}">总贴数-{{curNumber[sec.place]}}</router-link>
              </h6>
            </div>
            <div class="tt-item-layout">
              <div class="tt-innerwrapper tt-intro">欢迎访问{{sec.name}}板块！</div>
              <div class="tt-innerwrapper">
                <h6 class="tt-title">最新发帖</h6>
                <ul class="tt-list-badge" >
                  <li v-for="post in postList[sec.place]">
                    <a :href="'#/topic?fid=' + post['ID']">
                      <span class="tt-badge">{{post['title']}}</span>
                    </a>
                    <span></span>
                  </li>

                </ul>
              </div>
              <div class="tt-innerwrapper">
                <a href="#" class="tt-btn-icon">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-favorite" />
                    </svg>
                  </i>
                </a>
              </div>
            </div>
          </div>
        </div>
        <div class="col-12">
          <div class="tt-row-btn">
            <button type="button" class="btn-icon js-topiclist-showmore">
              <svg class="tt-icon">
                <use xlink:href="#icon-load_lore_icon" />
              </svg>
            </button>
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
      searchWord: null,
      secs: [
        { id: 1, name: "课程推荐", place: 0 },
        { id: 2, name: "刷题交流", place: 1 },
        { id: 3, name: "校园周边", place: 2 },
        { id: 4, name: "资源共享", place: 3 },
        { id: 5, name: "论坛公告", place: 4 }
      ],
      colorType: [
        "tt-color01",
        "tt-color02",
        "tt-color03",
        "tt-color04",
        "tt-color05",
        "tt-color06"
      ],
      postList: [
        [{ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}],
        [{ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}],
        [{ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}],
        [{ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}],
        [{ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}],
        [{ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}, {ID: "", date: "", title: ""}]
      ],
      curNumber: [0,0,0,0,0,0]
    };
  },
  mounted() {
    var that = this;
    for(let i = 0; i < 5; i++){
      that.axios
        .get(`/${i + 1}/forum_show`)
        .then(function(response) {
            if (response.data.status === 0) {
              that.$set(that.curNumber, i, response.data.data[0]['total']);
              that.$set(that.postList, i, response.data.data[1]);
            }
          }
        )
        .catch(function(error) {
          alert("查找最新帖子时出错" + error);
        });
    }
  },
  methods: {
    chooseColor: function(num) {
      return this.colorType[num] + " tt-badge";
    },
    output: function (number) {
      var that = this;
      alert(number);
    }
  }
};
</script>

<style>
.tt-item {
  text-align: left;
}
.tt-intro {
  color: #666f74;
  margin-bottom: 30px;
}
</style>
