
class Pagination(object):
    '''
    自定义分页组件
    '''
    def __init__(self,current_page_num,total_data_num,current_path,per_page_data_num=10,per_page_pagelink_num=11):
        self.current_page_num=current_page_num  #当前页码
        self.total_data_num=total_data_num  #总共的页码数
        self.current_path=current_path  #当前的路径
        self.per_page_data_num=per_page_data_num  #每一页显示的数据条数
        self.per_page_pagelink_num=per_page_pagelink_num  #每一页显示的页码个数
        self.half_show=self.per_page_pagelink_num//2  #一半页码数
        #计算出总的页码数
        self.total_page_num, more = divmod(self.total_data_num, per_page_data_num)
        if more:
            self.total_page_num = self.total_page_num + 1
        if self.current_page_num>self.total_page_num:
            self.current_page_num=self.total_page_num
        if self.current_page_num<1:
            self.current_page_num=1

    @property
    def start(self):
        '''
        数据的截取开始位置
        :return:
        '''
        start = (self.current_page_num - 1) * self.per_page_data_num
        return start

    @property
    def end(self):
        '''
        数据的截取结束位置
        :return:
        '''
        end = self.current_page_num * self.per_page_data_num
        return end

    @property
    def page_html(self):
        '''
        返回页码链接的列表
        pagelink_list   页码链接列表
        page_html       页码的字符串形式
        page_start      页码开始位置
        page_end        页码结束位置
        pre_page_num    上一页
        next_page_num   下一页
        :return:
        '''
        #页码链接列表
        pagelink_list=[]
        #页码链接的开始
        page_start=self.current_page_num-self.half_show
        #页码链接的结束
        page_end=self.current_page_num+self.half_show+1
        # 调整页码链接的开始和结束位置
        if self.current_page_num + self.half_show >= self.total_page_num:
            page_start = self.total_page_num - self.per_page_pagelink_num + 1
            page_end = self.total_page_num + 1
        if self.current_page_num <= self.half_show:
            page_start = 1
            page_end = self.per_page_pagelink_num + 1
        #添加首页
        pagelink_list.append('<li><a href="{0}?page={1}">首页</a></li>'.format(self.current_path, 1))
        #添加上一页
        pre_page_num = self.current_page_num - 1
        if pre_page_num < 1:
            pagelink_list.append('<li class="disabled"><a href="{0}?page={1}">上一页</a></li>'.format(self.current_path, pre_page_num))
        else:
            pagelink_list.append('<li><a href="{0}?page={1}">上一页</a></li>'.format(self.current_path, pre_page_num))
        #添加中间的页码链接部分
        for i in range(page_start, page_end):
            if i == self.current_page_num:
                pagelink_list.append('<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.current_path, i))
            else:
                pagelink_list.append('<li><a href="{0}?page={1}">{1}</a></li>'.format(self.current_path, i))
        #添加下一页
        next_page_num = self.current_page_num + 1
        if next_page_num > self.total_page_num:
            pagelink_list.append(
                '<li class="disabled"><a href="{0}?page={1}">下一页</a></li>'.format(self.current_path, next_page_num))
        else:
            pagelink_list.append('<li><a href="{0}?page={1}">下一页</a></li>'.format(self.current_path, next_page_num))
        #添加尾页
        pagelink_list.append('<li><a href="{0}?page={1}">尾页</a></li>'.format(self.current_path, self.total_page_num))
        #把页面的列表转换为字符串形式
        page_html = ''.join(pagelink_list)
        return page_html