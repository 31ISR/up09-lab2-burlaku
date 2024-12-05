from django.shortcuts import render
from .models import Community
def communities_list(req):
    communities = Community.objects.all()
    return render(req, 'communities/communities.html', {'communities': communities})
