from django.shortcuts import render, redirect, HttpResponse


def index(request):
    if 'count' in request.session:
        request.session['count'] += 1 
    else:
        request.session['count'] = 1

    if 'visit' in request.session:
        request.session['visit'] += 1 
    else:
        request.session['visit'] = 1

    context = {
        "count" : request.session['count'],
        "visit" : request.session['visit']
    }

    return render(request, 'index.html', context)

def destroy_session(request):
    del request.session['count']
    del request.session['visit']
    return redirect('/')

def by_two(request): 
    if 'count' in request.session: 
        request.session['count'] += 1


    return redirect('/')

def by_x(request) :
    if 'count' in request.session: 
        request.session['count'] += int(request.POST['number']) - 1

    return redirect('/')


