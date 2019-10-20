from django.shortcuts import render
from django.http import Http404

from rest_framework import mixins
from rest_framework import generics
#  from rest_framework.response import JSONResponse

from .serializers import EntrySerializer
from .models import Entry

from os.path import join
import logging
logger = logging.getLogger (__name__)
logger.setLevel (logging.INFO)
handler = logging.FileHandler (join("logs", f"{__name__}.log"))
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
        logger.info (f'in get {args} {kwargs}')
        try:
            response = self.retrieve (request, *args, **kwargs)
        except Exception as e:
            logger.error (e)
            raise 
        logger.info (response)
        return response

    def put(self, request, *args, **kwargs):
        return self.update (request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.retrieve (request, *args, **kwargs)


class EntryCompletions(generics.ListAPIView):
    """Returns a number of dictionary completiosn for a prefix"""
    MAX_COMPLETIONS= 20

    def get_queryset(self):
        #  logger.info (f'In get_queryset with {self.request.query_params}') 
        try:
            prefix = self.request.query_params['prefix']
            #  logger.info (prefix)
        except Exception as e:
            logger.error ("prefix not passed in request")
            raise Http404

        logger.info (f'In get_queryset with prefix={prefix}') 
        #  query=  Entry.objects.filter (text__startswith= prefix)
        query=  Entry.objects.filter (text__contains= prefix)
        return query [:self.MAX_COMPLETIONS]

    serializer_class = EntrySerializer

def double(arg:dict) -> list:
    """docstring for func"""
    #  if len (name) % 2 == 0:
    #      return name*2
    #  else:
    #      return '3'

