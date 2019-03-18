from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

class M1(MiddlewareMixin):

    def process_request(self,request):

        print('this is m1 process request.')

    def process_response(self,request,response):

        print('this is m1 process response.')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        print('this is m1 process view')

    def process_exception(self, request, exception):

        print('this is m1 process exception.')

        return HttpResponse('this is m1 catch error.')

    def process_template_response(self, request, response):

        print('this is m1 process_template_response')
        return response

class M2(MiddlewareMixin):

    def process_request(self,request):

        print('this is m2 process request.')

    def process_response(self,request,response):

        print('this is m2 process response')
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):

        print('this is m2 process view.')

    def process_exception(self, request, exception):

        print('this is m2 process exception')

    def process_template_response(self, request, response):

        print('this is m2 process_template_response')
        return response