# openstack-api
api身份验证
首先安装好所需的request和json模块，然后配置好所需的url身份验证地址(url="container:5000/v3/auth/token")，body身份信息，headers消息体类型为json形式，之后通过request库中的post请求来获取token值，之后将返回的token值(令牌)打印出来，以及以json形式的身份信息。
