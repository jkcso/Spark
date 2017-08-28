from django.shortcuts import render, redirect, render_to_response
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.views.generic import View


def profile_page(request, user_id):
    user = User.objects.get(pk=user_id)

    return render(request, 'user/profile_page.html', {'user': user})


class UserFormView(View):
    form_class = UserForm
    template_name = 'user/signup_form.html'

    # displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # creates object from form without saving in db for getting data.
            user = form.save(commit=False)
            # cleaned (normalised) data: data formatted properly.
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # saves password as hashed
            user.set_password(password)
            user.save()

            # returns user object if credentials are correct
            user = authenticate(username=username, password=password)

            # website login
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # redirects them in their profile page with info they passed.
                    return redirect('user:profile_page')

        return render(request, 'user/profile_page.html', {'form': form})
