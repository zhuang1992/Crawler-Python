<div>
        用户名<input id="username" type="text" />
        密码<input id="password" type="text" />
        <input id="btnlogin" type="button" value="登录" onclick="login()" />
</div>

<script type="text/javascript">
        function login() {
            if (document.getElementById("username") == "你的用户名" && document.getElementById("passowrd") == "你的密码") {
                window.location.href = "你的URL";
            }
        }
</script>