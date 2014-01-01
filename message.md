##报文格式
srcID：content
dstID: content
type:  content
text:  content


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
