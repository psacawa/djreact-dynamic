from django.shortcuts import render

from rest_framework import mixins
from rest_framework import generics

from .serializers import EntrySerializer
from .models import Entry

import logging
logger = logging.getLogger (__name__)
logger.setLevel (logging.INFO)
handler = logging.FileHandler (f"{__name__}.log")
logger.addHandler (handler)

def home(request):
    """home page"""
    return render (request, 'index.html')

class EntryList(mixins.ListModelMixin, 
                mixins.CreateModelMixin, 
                generics.GenericAPIView):
    """List dictionary entry API view"""

    queryset = Entry.objects.all ()
    serializer_class = EntrySerializer

    def get(self, request, *args, **kwargs):
        logger.info ("in get")
        return self.list (request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create (request, *args, **kwargs)


class EntryDetail(  mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """Docstring for EntryDetail. """

    queryset = Entry.objects.all ()
    serializer_class = EntrySerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve (request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update (request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.retrieve (request, *args, **kwargs)
