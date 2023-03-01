<template>
  <main id="tt-pageContent">
    <div class="container">
      <div class="tt-single-topic-list">
        <div class="tt-item">
          <div class="tt-single-topic">
            <div class="tt-item-header">
              <div class="tt-item-info info-top">
                <div class="tt-avatar-icon">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-ava-d" />
                    </svg>
                  </i>
                </div>
                <div class="tt-avatar-title">
                  <a href="#">{{thread.author}}</a>
                </div>
                <a href="#" class="tt-info-time">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-time" />
                    </svg>
                  </i>
                  {{new Date(thread.date*1000).toLocaleString()}}
                </a>
              </div>
              <h3 class="tt-item-title">
                <a href="#">{{thread.title}}</a>
              </h3>
            </div>
            <div class="tt-item-description" v-html="decodeURIComponent(thread.Finf)"></div>
            <div class="tt-item-info info-bottom">
              <a class="tt-icon-btn" style="cursor: pointer" @click="like()">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-like" />
                  </svg>
                </i>
                <span class="tt-text">{{thread.good}}</span>
              </a>
              <a class="tt-icon-btn" style="cursor: pointer" @click="collect()">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-favorite" />
                  </svg>
                </i>
              </a>
              <!-- <a href="#" class="tt-icon-btn">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-dislike" />
                  </svg>
                </i>
                <span class="tt-text">39</span>
              </a>
              -->
              <div class="col-separator"></div>
              <a href="#" class="tt-icon-btn tt-hover-02 tt-small-indent">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-share" />
                  </svg>
                </i>
              </a>
              <a href="#" class="tt-icon-btn tt-hover-02 tt-small-indent">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-flag" />
                  </svg>
                </i>
              </a>
              <a href="#" class="tt-icon-btn tt-hover-02 tt-small-indent">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-reply" />
                  </svg>
                </i>
              </a>
            </div>
          </div>
        </div>
        <div class="tt-item">
          <div class="tt-info-box">
            <h6 class="tt-title">浏览量与评论数</h6>
            <div class="tt-row-icon">
              <!-- <div class="tt-item">
                <a href="#" class="tt-icon-btn tt-position-bottom">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-reply" />
                    </svg>
                  </i>
                  <span class="tt-text">283</span>
                </a>
              </div>-->
              <div class="tt-item">
                <a href="#" class="tt-icon-btn tt-position-bottom">
                  <i class="tt-icon" style="filter: invert(60%);">
                    <svg>
                      <use xlink:href="#icon-view" />
                    </svg>
                  </i>
                  <span class="tt-text">{{thread.views}}</span>
                </a>
              </div>
              <div class="tt-item">
                <a href="#" class="tt-icon-btn tt-position-bottom">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-user" />
                    </svg>
                  </i>
                  <span class="tt-text">{{reviews.length}}</span>
                </a>
              </div>
              <!-- <div class="tt-item">
                <a href="#" class="tt-icon-btn tt-position-bottom">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-like" />
                    </svg>
                  </i>
                  <span class="tt-text">2.4k</span>
                </a>
              </div>
              <div class="tt-item">
                <a href="#" class="tt-icon-btn tt-position-bottom">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-favorite" />
                    </svg>
                  </i>
                  <span class="tt-text">951</span>
                </a>
              </div>
              <div class="tt-item">
                <a href="#" class="tt-icon-btn tt-position-bottom">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-share" />
                    </svg>
                  </i>
                  <span class="tt-text">32</span>
                </a>
              </div>-->
            </div>
          </div>
        </div>
        <div class="tt-item" v-for="review in reviews">
          <div class="tt-single-topic">
            <div class="tt-item-header pt-noborder">
              <div class="tt-item-info info-top">
                <div class="tt-avatar-icon">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-ava-t" />
                    </svg>
                  </i>
                </div>
                <div class="tt-avatar-title">
                  <a href="#">{{review.comment_man_name}}</a>
                </div>
                <a href="#" class="tt-info-time">
                  <i class="tt-icon">
                    <svg>
                      <use xlink:href="#icon-time" />
                    </svg>
                  </i>
                  {{new Date(review.comment_date*1000).toLocaleString()}}
                </a>
              </div>
            </div>
            <div class="tt-item-description" v-html="decodeURIComponent(review.Coinf)"></div>
            <div class="tt-item-info info-bottom">
              <!-- <a href="#" class="tt-icon-btn">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-like" />
                  </svg>
                </i>
                <span class="tt-text">671</span>
              </a>
              <a href="#" class="tt-icon-btn">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-dislike" />
                  </svg>
                </i>
                <span class="tt-text">39</span>
              </a>
              <a href="#" class="tt-icon-btn">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-favorite" />
                  </svg>
                </i>
                <span class="tt-text">12</span>
              </a>-->
              <div class="col-separator"></div>
              <a href="#" class="tt-icon-btn tt-hover-02 tt-small-indent">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-share" />
                  </svg>
                </i>
              </a>
              <a href="#" class="tt-icon-btn tt-hover-02 tt-small-indent">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-flag" />
                  </svg>
                </i>
              </a>
              <a href="#" class="tt-icon-btn tt-hover-02 tt-small-indent">
                <i class="tt-icon">
                  <svg>
                    <use xlink:href="#icon-reply" />
                  </svg>
                </i>
              </a>
            </div>
          </div>
        </div>
      </div>
      <div class="tt-wrapper-inner">
        <h4 class="tt-title-separator">
          <span>已加载所有回帖</span>
        </h4>
      </div>
      <div class="tt-topic-list" v-if="false">
        <div class="tt-item tt-item-popup">
          <div class="tt-col-avatar">
            <svg class="tt-icon">
              <use xlink:href="#icon-ava-f" />
            </svg>
          </div>
          <div class="tt-col-message">您似乎未登录。现在就注册或者登录，加入讨论吧。</div>
          <div class="tt-col-btn">
            <router-link to="/Register" style="margin-right: 10px">
              <button type="button" class="btn btn-primary">注册</button>
            </router-link>
            <router-link to="/Login">
              <button type="button" class="btn btn-secondary">登录</button>
            </router-link>
            <button type="button" class="btn-icon" @click="cancelTip()">
              <svg class="tt-icon">
                <use xlink:href="#icon-cancel" />
              </svg>
            </button>
          </div>
        </div>
      </div>
      <div class="tt-wrapper-inner">
        <div class="pt-editor form-default">
          <h6 class="pt-title">发表回复</h6>
          <div class="pt-row">
            <div class="col-left">
              <ul class="pt-edit-btn">
                <!-- <li>
                  <button type="button" class="btn-icon" @click="insert('quote')">
                    <svg class="tt-icon">
                      <use xlink:href="#icon-quote" />
                    </svg>
                  </button>
                </li>-->
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
                <!-- <li>
                  <button type="button" class="btn-icon" @click="insert('upload_files')">
                    <svg class="tt-icon">
                      <use xlink:href="#icon-upload_files" />
                    </svg>
                  </button>
                </li>-->
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
                <!-- <li>
                  <button type="button" class="btn-icon" @click="insert('emoticon')">
                    <svg class="tt-icon">
                      <use xlink:href="#icon-emoticon" />
                    </svg>
                  </button>
                </li>
                <li>
                  <button type="button" class="btn-icon" @click="insert('settings')">
                    <svg class="tt-icon">
                      <use xlink:href="#icon-settings" />
                    </svg>
                  </button>
                </li>
                <li>
                  <button type="button" class="btn-icon" @click="insert('color_picker')">
                    <svg class="tt-icon">
                      <use xlink:href="#icon-color_picker" />
                    </svg>
                  </button>
                </li>-->
              </ul>
            </div>
            <!-- <div class="col-right tt-hidden-mobile">
              <a href="#" class="btn btn-primary">预览</a>
            </div>-->
          </div>
          <div class="form-group">
            <textarea
              name="message"
              class="form-control"
              rows="5"
              placeholder="写下您的回复..."
              v-model="input_reply"
            ></textarea>
          </div>
          <div class="pt-row">
            <!-- <div class="col-auto">
              <div class="checkbox-group">
                <input type="checkbox" id="checkBox21" name="checkbox" checked />
                <label for="checkBox21">
                  <span class="check"></span>
                  <span class="box"></span>
                  <span class="tt-text">Subscribe to this topic.</span>
                </label>
              </div>
            </div>-->
            <div class="col-auto">
              <button
                type="button"
                class="btn btn-secondary btn-width-lg"
                @click="create_reply()"
              >提交</button>
            </div>
          </div>
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
      input_reply: ""
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
      var cont = that.input_reply;
      let sid = that.sid;
      let fid = that.$route.query.fid;

      cont = cont.replace("\n", "<br>");
      cont = encodeURIComponent(cont);
      that.axios
        .post(`/${sid}/${fid}/comment?comment=${cont}`, {
          comment: cont
        })
        .then(function(response) {
          console.log(response);
          if (response.data.status == 0) {
            alert("发表回复成功，等级+0.5！");
            location.reload();
          } else {
            alert("发表回复失败，原因：" + response.data.msg);
          }
        })
        .catch(function(error) {
          console.log(error);
          alert("请求回复帖子时遇到了错误");
        });
    },
    like() {
      var that = this;
      let fid = that.$route.query.fid;
      let sid = that.sid;

      that.axios
        .get(`/${sid}/${fid}/good`)
        .then(function(response) {
          console.log(response);
          if (response.data.status == 0) {
            alert("你觉得这个帖子很赞！");
            location.reload();
          } else {
            alert("点赞失败，原因：" + response.data.msg);
          }
        })
        .catch(function(error) {
          console.log(error);
          alert("请求点赞时遇到了错误");
        });
    },
    collect() {
      var that = this;
      let fid = that.$route.query.fid;
      let sid = that.sid;

      that.axios
        .get(`/${sid}/${fid}/collect`)
        .then(function(response) {
          console.log(response);
          if (response.data.status == 0) {
            alert("成功添加收藏！！");
            location.reload();
          } else {
            alert("收藏失败，原因：" + response.data.msg);
          }
        })
        .catch(function(error) {
          console.log(error);
          alert("请求收藏时遇到了错误");
        });
    }
  },
  mounted() {
    var that = this;
    if (!this.$store.state.isLogin) {
      alert("请登录后访问！");
      that.$router.push({ path: "/" });
      return;
    } else {
      let sid = that.sid;
      let fid = that.$route.query.fid;
      that.axios
        .get(`/${sid}/${fid}/browsefo`)
        .then(function(response) {
          console.log(response);
          if (response.data.status == 0) {
            that.thread = response.data.data[0];
            that.reviews = response.data.data[1];
          } else {
            alert("获取帖子详情失败，原因：" + response.data.msg);
            that.$router.push({ path: "/" });
          }
        })
        .catch(function(error) {
          console.log(error);
          alert("请求帖子详情时遇到了错误");
        });
    }
  }
};
</script>

<style>
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