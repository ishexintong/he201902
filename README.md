# he201902
分页，中间件
总结：
	process_request：
		1. 是在视图执行前执行的
		2. 它的顺序是从上往下
		3. 返回值是None,继续往后执行
		4. 返回值是HttpResponse的对象，执行对应中间件的process_response方法
		，接着往上，返回给浏览器

		
	process_response:
		1. 是在视图执行后执行的
		2. 它的顺序是从下往上
		3. 返回必须是HttpResponse的对象，继续往上执行
		
	process_view：
		1. 是在视图执行前执行的，process_request之后
		2. 它的顺序是从上往下
		3. 返回值是None,继续往后执行
		4. 返回值是HttpResponse的对象，执行最后一个中间件的process_response方法
		，接着往上，返回给浏览器，视图不走了
		
	process_exception：
		1. 报错了才执行
		2. 在视图函数之后，process_response之前
		3. 它的顺序是从下往上
		4. 返回值是HttpResponse的对象，执行最后一个中间件的process_response方法
		，接着往上，返回给浏览器
	

	process_template_response：
		1. 视图返回的对象有render方法 才执行
		2. 在视图函数之后，process_response之前
		3. 它的顺序是从下往上
		4. 返回值是HttpResponse的对象。
		5. 执行完所有的中间件的process_template_response之后，
		才执行对象.render()得到一个新的HttpResponse的对象，执行往交给process_response继续
