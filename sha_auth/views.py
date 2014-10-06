#from django.shortcuts import get_object_or_404, render


#def index(request):
#    return render(request, 'sha_auth/index.html')

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.context import RequestContext

def index(request):
   context = RequestContext(request,
                           {'request': request,
                            'user': request.user})
   return render_to_response('sha_auth/index.html',
                             context_instance=context)
