from django.shortcuts import render
import timeit

# Create your views here.
def demo(request):
	return render(request,'fibonacci/index.html')

def fib(request):
	start =timeit.timeit()
	n = int(request.POST['num'])
	s = 1
	s1 = 1
	for i in range(n):
		if i == 0:
			c ==s 
		elif i==1:
			c = s1 
		else:
			c = s1+s 
			s = s1 
			s1 = c 
	end =timeit.timeit()
	total_time=end-start
	return render(requset,'fibonacci/result.html',{'res':c,'time_taken':total_time})