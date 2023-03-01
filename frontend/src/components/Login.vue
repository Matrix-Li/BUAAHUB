<template>
 <div class="container">
        <div class="panel">
          <!--
          <div class="panel-header">
            <h1 class="panel-header-title">
                    登&nbsp&nbsp录
                    </h1 >
          </div>
          -->
            <form class="form" action="javascript:void(0);">
                <div class="input">
                    <label class="input-label">用户名</label>
                    <input type="text" class="input-field" id="user_name"  v-model="un" />
                </div>
                <div class="input">
                    <label class="input-label">密码</label>
                    <input type="password" class="input-field" id="user_pwd" v-model="pwd" />
                </div>
                <div class="input2">
                  <b-button block variant="primary" @click="login" >登&nbsp&nbsp录</b-button>
                    
                </div>
            </form>
            <div class="panel-footer">
              <div class="panel-footer-info2"><router-link to="/Register" class="link">注册 </router-link></div>
            </div>
            
        </div>
    </div>
</template>


<script>

export default {
  name: 'Login',
  data () {
    return {
      un: "",
      pwd: ""
    }
  },
  methods: {
    login() {
      this.login_(this.un, this.pwd);
    }
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  @import "../assets/login.css"

</style>
