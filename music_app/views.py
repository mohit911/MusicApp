from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.core.urlresolvers import reverse
from django.shortcuts import render, HttpResponseRedirect
from music_app.models import Genere, Music, Rating

# Create your views here.


def tracks(request):
    context = {}
    genres = Genere.objects.all()
    if request.method == 'POST':
        '''Saving New Track'''
        try:
            if request.POST.get('title') == '' or request.POST.get('genere') == '':
                context['message'] = 'Failed to update, Try again later'
            else:
                title = request.POST.get('title')
                rating = request.POST.get('rating')
                genere = request.POST.get('genere')
                genere = Genere.objects.get(id=genere)
                music_info = Music.objects.create(
                    title=title,
                    genere=genere)
                Rating.objects.create(
                    music=music_info,
                    user=request.user,
                    rating=rating)
        except:
            context['message'] = 'Failed to update, Try again later'
    tracks = Music.objects.all()
    '''Creating paginator'''
    paginator = Paginator(tracks, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        tracks = paginator.page(page)
    except(EmptyPage, InvalidPage):
        tracks = paginator.page(paginator.num_pages)

    context = {'data': tracks, 'genres': genres, 'loop': range(1, 6)}
    template = 'tracks.html'
    return render(request, template, context)


def t_detail(request, id):
    context = {}
    if request.method == 'POST':
        '''Saving New Track'''
        try:
            music_info = Music.objects.get(id=id)
            rating_info = Rating.objects.get_or_create(music=music_info, user=request.user)
            if request.POST.get('title') != '':
                title = request.POST.get('title')
                music_info.title = title
            if request.POST.get('rating') != '':
                rating = request.POST.get('rating')
                rating_info[0].rating = rating
                rating_info[0].save()
            if request.POST.get('genere') != '':
                genere = request.POST.get('genere')
                genere = Genere.objects.get(id=genere)
                music_info.genere = genere
            music_info.save()
        except:
            context['message'] = 'Failed to update, Try again later'

    return HttpResponseRedirect('/')


def generes(request):
    context = {}
    if request.method == 'POST':
        '''Saving New Genre'''
        try:
            if request.POST.get('genre') != '':
                genre = request.POST.get('genre')
                Genere.objects.create(genere=genre)
            else:
                context['message'] = 'Failed to update, Try again later'
        except:
            context['message'] = 'Failed to update, Try again later'

    genres = Genere.objects.all()

    '''Creating paginator'''
    paginator = Paginator(genres, 5)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        genres = paginator.page(page)
    except(EmptyPage, InvalidPage):
        genres = paginator.page(paginator.num_pages)

    context = {'genres': genres}
    template = 'generes.html'
    return render(request, template, context)


def g_detail(request, id):
    context = {}
    if request.method == 'POST':
        '''Saving New Track'''
        try:
            if request.POST.get('genre') != '':
                genre_info = Genere.objects.get(id=id)
                genre = request.POST.get('genre')
                genre_info.genere = genre
                genre_info.save()
            else:
                context['message'] = 'Failed to update, Try again later'
        except:
            context['message'] = 'Failed to update, Try again later'

    return HttpResponseRedirect(reverse('genres'))


def search_tracks(request):
    context = {}
    template = 'search_results.html'
    genres = Genere.objects.all()
    try:
        if request.GET.get('searchText') != '':
            searchtext = request.GET.get('searchText')
            data = Music.objects.filter(title__icontains=searchtext)
            result_count = data.count()

            '''Creating paginator'''
            paginator = Paginator(data, 5)
            try:
                page = int(request.GET.get('page', '1'))
            except:
                page = 1
            try:
                data = paginator.page(page)
            except(EmptyPage, InvalidPage):
                data = paginator.page(paginator.num_pages)
            context = {'data': data, 'genres': genres, 'loop': range(1, 6), 'result_count': result_count, 'search_tracks': True}
        else:
            return HttpResponseRedirect('/')
        return render(request, template, context)
    except:
        return HttpResponseRedirect('/')


def search_genere(request):
    context = {}
    template = 'search_results.html'
    if request.method == 'GET':
        try:
            if request.GET.get('searchText') != '':
                searchtext = request.GET.get('searchText')
                genres = Genere.objects.filter(genere__icontains=searchtext)
                result_count = genres.count()

                '''Creating paginator'''
                paginator = Paginator(genres, 5)
                try:
                    page = int(request.GET.get('page', '1'))
                except:
                    page = 1
                try:
                    genres = paginator.page(page)
                except(EmptyPage, InvalidPage):
                    genres = paginator.page(paginator.num_pages)
                context = {'genres': genres, 'result_count': result_count, 'search_genre': True}
                return render(request, template, context)
            else:
                return HttpResponseRedirect('/')
        except:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

    context = {'genres': genres, 'result_count': result_count, 'search_genre': True}
    template = 'generes.html'
    return render(request, template, context)
