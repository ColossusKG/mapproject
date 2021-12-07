from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


from .forms import UserForm


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('maps:index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def page_not_found(request, excpetions):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', status=404)
    # response = render_to_response('common/404.html', {}, context_instance=RequestContext(request))
    # response = render(RequestContext(request), 'common/404.html', {})
    # response.status_code = 404
    # return response


def server_error(request):
    """
    500 Internal Server Error
    """
    return render(request, 'common/500.html', status=500)
    # response = render_to_response('common/500.html', {}, context_instance=RequestContext(request))
    # response = render(RequestContext(request), 'common/500.html', {})
    # response.status_code = 500
    # return response
