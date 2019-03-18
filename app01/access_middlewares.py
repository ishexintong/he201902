from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,render,redirect

class CheckinMiddle(MiddlewareMixin):
    '''
    从中间件的角度解决需要登录的访问
    '''
    white_list=['/login/',]
    black_list=['/black/',]

    def process_request(self,request):
        user=request.session.get('user')
        local_path=request.path_info
        if local_path  in self.black_list:
            return HttpResponse('你的路径有问题。')
        elif local_path in self.white_list or user:
            return
        else:
            return redirect('/login/')