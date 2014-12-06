
from django.views.static import serve

def index_serve (request, document_root=None):
  return serve(request, 'index.html', document_root=document_root)
  