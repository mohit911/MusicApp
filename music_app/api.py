from music_app.models import Music, Genere, Rating
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict


def average(ratings):
    try:
        count = 0
        counter = 0
        for rating in ratings:
            counter += 1
            count += rating.rating
        avg = int(count / counter)
        return avg
    except:
        return 0


@api_view(['GET', 'POST'])
def all_tracks(request):
    """List all Tracks."""
    try:
        if request.method == 'GET':
            tracks = Music.objects.all()
            count = tracks.count()

            '''Creating paginator'''
            paginator = PageNumberPagination()

            track_objs = paginator.paginate_queryset(tracks, request)

            track_list = []
            for track in track_objs:
                genere_list = []
                genere_list.append(OrderedDict([('id', track.genere.id), ('name', track.genere.genere)]))
                track_list.append(OrderedDict([('id', track.id), ('title', track.title), ('rating', average(track.music_track.all())), ('genres', genere_list)]))

            data = OrderedDict([('count', count), ('next', paginator.get_next_link()), ('previous', paginator.get_previous_link()), ('results', track_list)])
            return Response(data)
    except:
        print"========= all_tracks() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Failed To display tracks')])
        return Response(data)

    """Creating new Track."""
    try:
        if request.method == 'POST':
            try:
                load = request.data

                title = load['title']
                genere = load['genres'][0]
                genere = Genere.objects.get(id=genere)
                music_info = Music.objects.create(
                    title=title,
                    genere=genere)
                data = {'message': 'Track added'}
                try:
                    rate = int(load['rating'])
                    if load['rating'] != '':
                        if rate in range(1, 6):
                            rating = rate
                            Rating.objects.create(
                                music=music_info,
                                user=request.user,
                                rating=rating)
                            data['message'] += ', Rating updated'
                except:
                    data['message'] += ', Rating Adding Failed, Please make sure You are loggedin'

                return Response(data)
            except:
                pass
    except:
        print"========= all_tracks() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Failed To add track')])
        return Response(data)


@api_view(['GET', 'POST'])
def track_detail(request, id):
    """List details of a Tracks."""
    try:
        if request.method == 'GET':
            track_obj = Music.objects.get(id=id)

            genere_list = []
            genere_list.append(OrderedDict([('id', track_obj.genere.id), ('name', track_obj.genere.genere)]))

            track_list = []
            track_list.append(OrderedDict([('id', track_obj.id), ('title', track_obj.title), ('rating', average(track_obj.music_track.all())), ('genres', genere_list)]))
            data = OrderedDict([('count', 1), ('next', None), ('previous', None), ('results', track_list)])
            return Response(data)
    except:
        print"========= track_detail() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Track Not Found')])
        return Response(data)

    """Edit Track Details."""
    try:
        if request.method == 'POST':
            try:
                load = request.data
                track = Music.objects.get(id=load['id'])
                if 'title' in load:
                    track.title = load['title']
                if 'genres' in load:
                    try:
                        genere = Genere.objects.get(id=load['genres'][0])
                        track.genere = genere
                    except:
                        pass
                track.save()
                data = {'message': 'track updated'}
                try:
                    rate = int(load['rating'])
                    if 'rating' in load:
                        if rate in range(1, 6):
                            rating_info = Rating.objects.get_or_create(music=track, user=request.user)
                            rating_info[0].rating = rate
                            rating_info[0].save()
                            data['message'] += ', Rating updated'
                        else:
                            data['message'] += ', Rating Should be in 1 - 5 range'
                except:
                    data['message'] += ', Rating update Failed, Please make sure You are loggedin'

                return Response(data)
            except:
                print"========= track_detail() Expection ======="
                data = OrderedDict([('results', 'Track Not Found')])
                return Response(data)

    except:
        print"========= track_detail() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Track Not Updated')])
        return Response(data)


@api_view(['GET', 'POST'])
def all_generes(request):
    """List all Genres."""
    try:
        if request.method == 'GET':
            generes = Genere.objects.all()
            count = generes.count()

            '''Creating paginator'''
            paginator = PageNumberPagination()

            generes = paginator.paginate_queryset(generes, request)

            genere_list = []
            for genere in generes:
                genere_list.append(OrderedDict([('id', genere.id), ('name', genere.genere)]))
            data = OrderedDict([('count', count), ('next', paginator.get_next_link()), ('previous', paginator.get_previous_link()), ('results', genere_list)])
            return Response(data)
    except:
        print"========= all_generes() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Genre Not Found')])
        return Response(data)

    """Creating new Genre."""
    try:
        data = {}
        if request.method == 'POST':
            load = request.data
            if load['name'] != '':
                Genere.objects.create(genere=load['name'])
                data = {'message': 'Genre Created'}
            else:
                data = {'message': 'Genre Not Created, please add data in proper format.'}
        return Response(data)
    except:
        print"========= all_generes() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Genre Not Created')])
        return Response(data)


@api_view(['GET', 'POST'])
def genere_detail(request, id):
    """List details of a Genre."""
    try:
        if request.method == 'GET':
            genere = Genere.objects.get(id=id)
            data = OrderedDict([('id', genere.id), ('name', genere.genere)])
            return Response(data)
    except:
        print"========= genere_detail() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Genre Not Found')])
        return Response(data)

    """Edit Genre Details."""
    try:
        if request.method == 'POST':
            try:
                load = request.data
                genere = Genere.objects.get(id=load['id'])
                if load['name'] != '':
                    genere.genere = load['name']
                    genere.save()
                data = {'id': genere.id, 'name': genere.genere}
            except:
                data = {'message': 'Genre Not Updated'}
            return Response(data)
    except:
        print"========= genere_detail() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Genre Not Updated')])
        return Response(data)


@api_view(['GET', ])
def search_api(request):
    """Api for search."""
    title = request.GET.get('title')
    try:
        if request.method == 'GET':
            track_list = []
            tracks = Music.objects.filter(title__icontains=title)
            count = tracks.count()
            for track in tracks:
                genere_list = []
                genere_list.append(OrderedDict([('id', track.genere.id), ('name', track.genere.genere)]))
                track_list.append(OrderedDict([('id', track.id), ('title', track.title), ('rating', track.rating), ('genres', genere_list)]))
            data = OrderedDict([('count', count), ('next', None), ('previous', None), ('results', track_list)])
            return Response(data)
    except:
        print"========= search_api() Expection ======="
        data = OrderedDict([('count', 0), ('next', None), ('previous', None), ('results', 'Track Not Found')])
        return Response(data)
