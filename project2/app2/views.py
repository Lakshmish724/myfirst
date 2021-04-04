from django.shortcuts import render,get_object_or_404
from app2.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.


def post_list_view(request):
	post_list=Post.objects.all()

	paginator=Paginator(post_list,2)
	page_number=request.GET.get('page')

	try:
		post_list=paginator.page(page_number)
	except PageNotAnInteger:
		post_list=paginator.page(1)
	except EmptyPage:
		post_list=paginator.page(paginator,num_pages)
	my_dict={'post_list':post_list}
	return render(request=request, template_name='app2/post.html', context=my_dict)

# class based view
from django.views.generic import ListView

class Display(ListView):
	model=Post
	template_name='app2/post.html'
	paginate_by=2

def post_detail_view(request,year,month,day,post):
	post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	my_dict={'post':post}
	return render(request=request, template_name='app2/detail.html', context=my_dict)

from app2.forms import EmailForm
from django.core.mail import send_mail

def mail_send_view(request,id):
	post=get_object_or_404(Post,id=id,status='published')
	sent=False
	if request.method=="POST":
		form=EmailForm(request.POST)
		if form.is_valid():
			dtt=form.cleaned_data
			send_mail('project2','hi,howis','lakku@123.com',[dtt['to']])
			sent=True
	else:
		form=EmailForm()

	my_dict={'form':form,'post':post,'sent':sent}
	return render(request=request, template_name='app2/email.html',context=my_dict)