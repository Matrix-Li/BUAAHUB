<template>
  <main id="tt-pageContent">
    <div class="container">
      <div class="container">
        <div class="tt-wrapper-inner">
          <h1 class="tt-title-border">发布新帖</h1>
          <form class="form-default form-create-topic">
            <div class="form-group">
              <label for="inputTopicTitle">帖子标题</label>
              <div class="tt-value-wrapper">
                <input
                  type="text"
                  name="name"
                  class="form-control"
                  id="inputTopicTitle"
                  placeholder="请输入标题"
                  v-model="title"
                />
                <span class="tt-value-input"></span>
              </div>
              <div class="tt-note">请简短描述您帖子的主题</div>
            </div>
            <div class="form-group">
              <label>选择一个版块</label>
              <div class="tt-js-active-btn tt-wrapper-btnicon">
                <div class="row tt-w410-col-02">
                  <div class="col-4 col-lg-3 col-xl-2">
                    <a
                      href="#"
                      class="tt-button-icon"
                      @click="selected_sec=1"
                      v-bind:class="{ active: selected_sec==1 }"
                    >
                      <span class="tt-icon">
                        <svg>
                          <use xlink:href="#icon-discussion" />
                        </svg>
                      </span>
                      <span class="tt-text">课程推荐</span>
                    </a>
                  </div>
                  <div class="col-4 col-lg-3 col-xl-2">
                    <a
                      href="#"
                      class="tt-button-icon"
                      @click="selected_sec=2"
                      v-bind:class="{ active: selected_sec==2 }"
                    >
                      <span class="tt-icon">
                        <svg>
                          <use xlink:href="#icon-Question" />
                        </svg>
                      </span>
                      <span class="tt-text">刷题交流</span>
                    </a>
                  </div>
                  <div class="col-4 col-lg-3 col-xl-2">
                    <a
                      href="#"
                      class="tt-button-icon"
                      @click="selected_sec=3"
                      v-bind:class="{ active: selected_sec==3}"
                    >
                      <span class="tt-icon">
                        <svg>
                          <use xlink:href="#icon-gallery" />
                        </svg>
                      </span>
                      <span class="tt-text">校园周边</span>
                    </a>
                  </div>
                  <div class="col-4 col-lg-3 col-xl-2">
                    <a
                      href="#"
                      class="tt-button-icon"
                      @click="selected_sec=4"
                      v-bind:class="{ active: selected_sec==4 }"
                    >
                      <span class="tt-icon">
                        <svg>
                          <use xlink:href="#icon-Video" />
                        </svg>
                      </span>
                      <span class="tt-text">资源共享</span>
                    </a>
                  </div>
                  <div class="col-4 col-lg-3 col-xl-2">
                    <a
                      href="#"
                      class="tt-button-icon"
                      @click="selected_sec=5"
                      v-bind:class="{ active: selected_sec==5 }"
                    >
                      <span class="tt-icon">
                        <svg>
                          <use xlink:href="#icon-Others" />
                        </svg>
                      </span>
                      <span class="tt-text">论坛公告</span>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div class="pt-editor">
              <h6 class="pt-title">帖子内容</h6>
              <div class="pt-row">
                <div class="col-left">
                  <ul class="pt-edit-btn">
                    <li>
                      <button type="button" class="btn-icon" @click="insert('bold')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-bold" />
                        </svg>
                      </button>
                    </li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('italic')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-italic" />
                        </svg>
                      </button>
                    </li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('share_topic')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-share_topic" />
                        </svg>
                      </button>
                    </li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('blockquote')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-blockquote" />
                        </svg>
                      </button>
                    </li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('performatted')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-performatted" />
                        </svg>
                      </button>
                    </li>
                    <li class="hr"></li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('bullet_list')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-bullet_list" />
                        </svg>
                      </button>
                    </li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('heading')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-heading" />
                        </svg>
                      </button>
                    </li>
                    <li>
                      <button type="button" class="btn-icon" @click="insert('horizontal_line')">
                        <svg class="tt-icon">
                          <use xlink:href="#icon-horizontal_line" />
                        </svg>
                      </button>
                    </li>
                  </ul>
                </div>
              </div>
              <div class="form-group">
                <textarea
                  name="message"
                  class="form-control"
                  rows="5"
                  placeholder="请输入帖子内容"
                  v-model="input_reply"
                ></textarea>
              </div>
              <div class="row">
                <div class="col-md-5">
                  <div class="form-group">
                    <label for="inputTopicTags">设置帖子查看权限</label>
                    <input
                      type="text"
                      name="name"
                      class="form-control"
                      id="inputTopicTags"
                      placeholder
                      v-model="view_rank"
                    />
                  </div>
                  <div class="tt-note">
                    低于所设等级的用户将无法查看此贴。
                    <br />
                    所设置的值必须不高于您的等级{{your_rank}}，并且必须为整数。
                    <br />请慎重设置此项。
                  </div>
                </div>
              </div>
              <div class="row">
                <div class="col-auto ml-md-auto">
                  <button
                    type="button"
                    class="btn btn-secondary btn-width-lg"
                    @click="create_reply()"
                  >发表</button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
export default {
  data() {
    return {
      // cancelTip: true,
      thread: { Finf: "", author: "", date: 0, good: 0, title: "" },
      reviews: [],
      input_reply: "",
      selected_sec: 0,
      title: "",
      view_rank: 1
    };
  },
  computed: {
    sid: function() {
      if (this.$store.state.isLogin) {
        return this.$store.state.user.sid;
      } else {
        alert("请登录后浏览！");
        this.$router.push({ path: "/login" });
        return "未登录";
      }
    },
    your_rank: function() {
      if (this.$store.state.isLogin) {
        return this.$store.state.user.rank;
      } else {
        alert("请登录后浏览！");
        this.$router.push({ path: "/login" });
        return "未登录";
      }
    }
  },
  methods: {
    // cancelTip() {
    //   this.cancelTip = false;
    // }
    insert(opt) {
      var html_tag = "";
      switch (opt) {
        case "bold":
          html_tag = "<b></b>";
          break;
        case "italic":
          html_tag = "<i></i>";
          break;
        case "share_topic":
          html_tag = '<a href="">这是一个超链接</a>';
          break;
        case "blockquote":
          html_tag = "<blockquote></blockquote>";
          break;
        case "performatted":
          html_tag = "<pre><code></code></pre>";
          break;
        case "bullet_list":
          html_tag = "<ul><li>1</li><li>2</li><li>3</li></ul>";
          break;
        case "heading":
          html_tag = "<h3></h3>";
          break;
        case "horizontal_line":
          html_tag = "<s></s>";
          break;
        default:
          break;
      }
      this.input_reply += html_tag;
    },
    create_reply() {
      var that = this;
      var sec = that.selected_sec;
      if (sec == 0) {
        alert("请先选择版块！");
        return;
      }
      var cont = that.input_reply;
      var title = that.title;
      var rank = String(that.view_rank);
      let sid = that.sid;
      let fid = that.$route.query.fid;

      cont = cont.replace("\n", "<br>");
      cont = encodeURIComponent(cont);
      that.axios
        .get(
          `/${sid}/${sec}/create_in_module?note=${cont}&title=${title}&rank=${rank}`,
          {
            note: cont,
            title: title,
            rank: rank
          }
        )
        .then(function(response) {
          if (response.data.status == 0) {
            alert("发表帖子成功，等级+0.5！");
            let fid = response.data.data.FID;
            that.$router.push(`/topic?fid=${fid}`);
          } else {
            alert("发表帖子失败，原因：" + response.data.msg);
          }
        })
        .catch(function(error) {
          console.log(error);
          alert("请求发表帖子时遇到了错误");
        });
    }
  },
  mounted() {}
};
</script>

<style scoped>
/* blockquote 样式 */
blockquote {
  display: block;
  border-left: 8px solid #d0e5f2;
  padding: 5px 10px;
  margin: 10px 0;
  line-height: 1.4;
  font-size: 100%;
  background-color: #f1f1f1;
}

/* code 样式 */
code {
  display: inline-block;
  *display: inline;
  *zoom: 1;
  background-color: #f1f1f1;
  border-radius: 3px;
  padding: 3px 5px;
  margin: 0 3px;
}
pre code {
  display: block;
}

/* ul ol 样式 */
ul,
ol {
  margin: 10px 0 10px 20px;
}
</style>
