from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

def index(request):
    '''

    :param request:
    :return:
    '''
    ret=HttpResponse('this is index page.')

    def func():
        print('in index/render')
        return HttpResponse('this is 98k.')

    ret.render=func

    print('-'*80)
    return ret

def login(request):
    '''

    :param request:
    :return:
    '''
    if request.method=='POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        if username=='alex' and password=='111':
            request.session['user']=username
            return redirect('/index/')
    return render(request,'login.html')

students_list=[]
for i in range(1,303):
    students_list.append({'name':'sakula-%s'%(i),'age':i})

def student_list(request):
    '''

    :param request:
    :param current_page_num: 当前页面数
    :param total_data_num: 总数据量
    :param total_page_num: 总页码数
    :param per_page_data_num: 每页显示数据条数
    :param per_page_pagelink_num: 每页显示的页码数
    :param page_num_list: 每页的页码链接列表
    :return:
    '''
    #获取当前的页码
    try:
        current_page_num=int(request.GET.get('page',1))
    except Exception as e:
        current_page_num=1
    #每一页的页码链接数
    per_page_pagelink_num=11
    #总的数据量
    total_data_num=len(students_list)
    #每一页的数据量
    per_page_data_num=10
    #半个 页码链接数据
    half_show=per_page_pagelink_num//2
    #页码的链接的开始
    page_start=current_page_num-half_show
    #页码的链接的结束
    page_end=current_page_num+half_show+1

    #数据的开始
    start=(current_page_num-1)*per_page_data_num
    #数据的结束
    end=current_page_num*per_page_data_num
    #总的页码数
    total_page_num,more=divmod(total_data_num,per_page_data_num)
    if more:
        total_page_num=total_page_num+1
    #规划数据列表
    students_list1=students_list[start:end]
    #页码的列表
    page_num_list=[]
    #当前的访问的路径
    current_path=request.path_info
    #调整页码链接的显示
    if current_page_num+half_show>=total_page_num:
        page_start=total_page_num-per_page_pagelink_num+1
        page_end=total_page_num+1
    if current_page_num<=half_show:
        page_start=1
        page_end=per_page_pagelink_num+1

    #添加首页
    page_num_list.append('<li><a href="{0}?page={1}">首页</a></li>'.format(current_path,1))
    #添加上一页
    pre_page_num=current_page_num-1
    if pre_page_num<1:
        page_num_list.append('<li class="disabled"><a href="{0}?page={1}">上一页</a></li>'.format(current_path,pre_page_num))
    else:
        page_num_list.append('<li><a href="{0}?page={1}">上一页</a></li>'.format(current_path,pre_page_num))
    #添加中间的页面链接
    for i in range(page_start,page_end):
        if i == current_page_num:
            page_num_list.append('<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(current_path,i))
        else:
            page_num_list.append('<li><a href="{0}?page={1}">{1}</a></li>'.format(current_path,i))
    #添加下一页
    next_page_num=current_page_num+1
    if next_page_num>total_page_num:
        page_num_list.append('<li class="disabled"><a href="{0}?page={1}">下一页</a></li>'.format(current_path,next_page_num))
    else:
        page_num_list.append('<li><a href="{0}?page={1}">下一页</a></li>'.format(current_path,next_page_num))
    #添加尾页
    page_num_list.append('<li><a href="{0}?page={1}">尾页</a></li>'.format(current_path,total_page_num))
    page_html=''.join(page_num_list)
    ret={'data_list':students_list1,'page_html':page_html}
    return render(request,'student_list.html',ret)

def staff_list(request):
    from  . import pagination
    try:
        current_pagenum=int(request.GET.get('page',1))
    except Exception as e:
        current_pagenum=1

    current_path=request.path_info
    page_obj=pagination.Pagination(current_pagenum,len(students_list),current_path)
    data1=students_list[page_obj.start:page_obj.end]
    return render(request,'student_list1.html',{'data1':data1,'page_html':page_obj.page_html})