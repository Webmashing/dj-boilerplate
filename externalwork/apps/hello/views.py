# Create your views here.
from django.shortcuts import render_to_response, RequestContext
import logging

logger = logging.getLogger(__name__)


def hello(request):
    logger.info('this is a logger info example!')
    return render_to_response("index.html", context_instance=RequestContext(request))
