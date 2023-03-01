//全局状态定义于此
exports.install = function (Vue, options) {
  Vue.prototype.login_ = function (userName, pwd) {
    var that = this;
    that.axios
      .get("/login?nm=" + userName + "&ps=" + pwd)
      .then(function (response) {
        console.log(response);
        if (response.data.status == 0) {
          //设置全局状态（支持双向绑定的全局变量）
          that.$store.commit('setIsLogin', true);
          that.$store.commit('setUser', {
            //用户信息
            username: response.data.data.Cname,
            sid: response.data.data.SID,
            rank: response.data.data.crank
          });
          console.log(that.$store.state)
          alert("您已成功登录！");
          that.$router.push({ path: "/" });
        } else {
          alert("登录失败，原因：" + response.data.msg);
        }
      })
      .catch(function (error) {
        alert("处理登录请求时遇到了错误");
      });
  }
  Vue.prototype.admin_login_ = function (userName, pwd) {
    var that = this;
    that.axios
      .get("/adminlogin?nm=" + userName + "&ps=" + pwd)
      .then(function (response) {
        console.log(response);
        if (response.data.status == 0) {
          //设置全局状态（支持双向绑定的全局变量）
          that.$store.commit('setIsLogin', true);
          that.$store.commit('setUser', {
            //用户信息
            username: response.data.data.Adname,
            sid: response.data.data.SID,
            rank: "管理员"
          });
          console.log(that.$store.state)
          alert("您已成功登录！");
          that.$router.push({ path: "/AdminUserMngr" });
        } else {
          alert("登录失败，原因：" + response.data.msg);
        }
      })
      .catch(function (error) {
        alert("处理登录请求时遇到了错误");
      });
  }
  Vue.prototype.register_ = function (userName, pwd1, pwd2) {
    var that = this;
    if (userName === "") {
      alert("用户名不能为空");
      return;
    }
    if(!((userName[0] >= 'a'&& userName[0] <= 'z')||(userName[0] >= 'A' && userName[0] <= 'Z'))){
             alert("用户名首位必须是字母");
             return;
    }
    if (!(pwd1 === pwd2)) {
      alert("两次密码必须相同");
      return;
    }
    that.axios
      .get("/regist?nm=" + userName + "&ps=" + pwd1)
      .then(function (response) {
        if (response.data.status == 0) {
          // that.$store.commit('setIsLogin', true);
          // that.$store.commit('setUser', {
          //   //用户信息
          //   username: response.data.data.Cname,
          //   sid: response.data.data.SID,
          //   rank: response.data.data.crank
          // });
          // console.log(that.$store.state)
          alert("您已成功注册，下面跳转到主界面！");
          that.$router.push({ path: "/" });
        } else {
          alert("注册失败，原因：" + response.data.msg);
        }
      })
      .catch(function (error) {
        alert(error);
      });
  }
}
