# -*- coding: utf-8 -*-
#type string
#id,goal_id int
class msg(object):
      def __init__(type='',srcid,dstid,text):
          self.dic={}
          self.dic['type']=type
          self.dic['srcId']=srcid
          self.dic['dstId']=dstid
          self.dic['text']=text
