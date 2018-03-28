from django.shortcuts import render

from django.shortcuts import redirect

from .forms import PostQueryForm

def index(request):
	return render(request, 'webapp/home.html')

def postQuery(request):
	if request.method == "POST":
		form = PostQueryForm(request.POST)
		if form.is_valid():
			post = form.save()
			# post.name = request.name
			# post.query = request.query
			# post.contact = request.contact
			post.save()
			return redirect('submitConfirmation')

	form = PostQueryForm()
	return render(request, 'webapp/postQuery.html', {'form': form})

def contact(request):
	return render(request, 'webapp/basic.html', 
		{'content' : ['If you would like to contact me, please email me.','aman.rania1@gmail.com']})

def submitConfirmation(request):
	return render(request, 'webapp/basic.html', 
		{'content' : ['Your query has been recorded. You will be contacted shortly.']})