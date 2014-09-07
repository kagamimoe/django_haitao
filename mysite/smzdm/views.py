from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from smzdm.models import GoodsPost
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

# Create your views here.
def archive(request):
	posts = GoodsPost.objects.all()

	paginator = Paginator(posts, 10) # Show 25 contacts per page

	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		posts = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		posts = paginator.page(paginator.num_pages)

	# return render('goods.html', {"posts": posts})





	t = loader.get_template("goods.html")
	c = Context({'posts':posts})
	return HttpResponse(t.render(c))