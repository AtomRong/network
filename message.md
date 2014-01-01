##报文格式
### srcID：content
### dstID: content
### type:  content
### text:  content

## 事件流程[]中的内容是content

### 注册流程
     User向服务器发送注册请求[name，pass]
     服务器返回信息，成功与否
     若成功，返回分配给的用户id
       失败，错误状态
### 登录流程
     user向服务器发送登录请求[id,pass]
     服务器返回信息，成功与否
     若成功，服务器返回id，name，好友列表，在线好友与ip
       失败，错误状态
### 添加好友
     user A向服务器发送添加请求[User B(id)]
     服务器向User B转发请求[User A,name]
     User B向服务器返回同意与否
     若同意:服务器分别向A,B发送对方信息
      拒绝 ：服务器转发结果给A
### 删除好友
     user A向服务器发送删除请求[User B(id)]
     服务器分别更新A，B好友列表
### 广播消息
     user A向服务器发送广播请求[广播内容]
     服务器分别向在它所有在线好友发送该消息[广播内容]
    
     
###  1. id=0 代表服务器，id是dstId（下同）
####  type = 0 注册
    pass,name
####  type = 1 登录
    id,pass
####  type = 2 退出
    Null
####  type = 3 增加好友
    好友id
#### type = 4 删除好友
    同上
####  type = 5 离线消息
    id,msg
####  type = 6 广播消息
    msg
####  type = 1000 心跳信息，确认，30s 一次

### 2 id = 用户id
#### type = 0 系统通知
   操作成功
#### type = 1 自身信息
   id，pass，friends(id,ip)
#### type = 2 状态更新，某用户的ip 变了
   id,property,new_content
#### type = 6 广播消息
    msg
  
  

 总结（考虑的问题）：
>  1.向服务器确认自己在线（定时）
>  2.可靠数据传输，
>   ack:如果用户在某时刚确认自己在线，然后掉线了，
      其他用户向它发送信息，必须要ack，然后消息发给服务器
>      加密：
>   有序到达:
>  3.
