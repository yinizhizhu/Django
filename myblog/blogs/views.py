# -*- coding: utf-8 -*-
from blogs.models import blog_lee
from string import atoi
from django.template import Context
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

def HomePage(request):
	"""
		The homepage for my blogs
	"""
	blogs = blog_lee.objects.all()
	c = Context({"blogs": blogs,})
	return render_to_response('HomePage.html', c)

def PythonFile(request):
	"""
		The operation for file in python
	"""	
	blogs_lee = blog_lee.objects.all()
	for blog in blogs_lee:
		if blog.class_blog == 'PythonFile':
			print 'hahahah'
			return render_to_response('PythonFile.html')
	print 'lalla'
	python_re = blog_lee()
	python_re.title_blog = 'Python文件操作学习笔记'
	python_re.class_blog = 'PythonFile'
	python_re.tag_blog = '文件操作_python'
	python_re.link_blog = '/PythonFile'
	python_re.index_blog = 'Python的文件操作较为简单，但是容易忘掉，然后自己就得去查询。对于Python的文件操作，我们主要是了解它的：1.文件操作模式，2.常用方法[.....]'
	python_re.state_blog = True
	python_re.save()
	return render_to_response('PythonFile.html')

def PythonDjango(request):
	"""
		The basic command for django in python
	"""
	return render_to_response('PythonDjango.html')

def PythonMysql(request):
	"""
		The basic command for mysql in python
	"""
	return render_to_response('PythonMysql.html')

def PythonRE(request):
	"""
		The regular expressioin frequently used in python
	"""
	blogs_lee = blog_lee.objects.all()
	for blog in blogs_lee:
		if blog.class_blog == 'PythonRE':
			print 'hahahah'
			return render_to_response('PythonRE.html')
	print 'lalla'
	python_re = blog_lee()
	python_re.title_blog = '正则表达式RE学习笔记'
	python_re.class_blog = 'PythonRE'
	python_re.tag_blog = '正则表达式_python'
	python_re.link_blog = '/PythonRE'
	python_re.index_blog = '字符串匹配方法正则表达式：RE因为在自己在编写网络爬虫过程中，用到了正则表达式，感受到了它的优雅！为了方便用时能够记起一些重要的使用方式，所以，在此记下。对于正则表达式（RE：Regular Expression），我们主要是了解它的常用符号、常用方法、常用搭配python_re.save()[.....]'
	python_re.state_blog = True
	python_re.save()
	return render_to_response('PythonRE.html')

def PythonNumpy(request):
	"""
		The operation for number in python
	"""
	return render_to_response('PythonNumpy.html')

def PythonMatplotlib(request):
	"""
		To plot the data on screen in python
	"""
	return render_to_response('PythonMatplotlib.html')

def CPointer(request):
	"""
		The pointer in C
	"""
	return render_to_response('CPointer.html')

def CFile(request):
	"""
		The basic operation for file in C
	"""
	return render_to_response('CFile.html')

def CplusPointer(request):
	"""
		The pointer in C++
	"""
	return render_to_response('CplusPointer.html')

def CplusFile(request):
	"""
		The basic operation for file in C++
	"""
	return render_to_response('CplusFile.html')

def SvnSae(request):
	return render_to_response('SvnSae.html')

def GitCommand(request):
	return render_to_response('GitCommand.html')