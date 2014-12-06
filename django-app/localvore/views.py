
from django.views.static import serve

def index_serve (request, document_root=None):
  if request.path.startswith(('/favicon.ico', '/components/', '/css/', '/img/', '/js/', '/tpl/')):
    return serve(request, request.path[1:], document_root=document_root)
    
  return serve(request, 'index.html', document_root=document_root)
  