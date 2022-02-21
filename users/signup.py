from django.contrib import messages

def signup(request):
    # redirect a user to the home page if he is already logged in
    if request.user.is_authenticated:
        return redirect('core:home')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # display a nice message when a new user is registered
            messages.success(request, "Congratulations, you are now a registered user!")
            return redirect('core:home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})