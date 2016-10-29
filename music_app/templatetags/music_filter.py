""""Filter."""
from django import template
# from requests import request
# from apps.cards.models import Cards
register = template.Library()


@register.filter
def average(ratings):
    """Calculating Average of ratings in 1 Music Track."""
    try:
        count = 0
        counter = 0
        for rating in ratings:
            counter += 1
            count += rating.rating

        avg = int(count / counter)
        lis = list(range(avg))
        return lis
    except:
        return 0


@register.filter
def user_rating(ratings, request):
    try:
        for rating in ratings:
            if rating.user == request.user:
                if rating.rating:
                    return rating.rating
                else:
                    return None
        return None
    except:
        return None
