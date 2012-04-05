# -*- coding:utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response

from django.contrib.auth.decorators import login_required


@login_required()
def prof_admin(request):
    ctxt = RequestContext(request, {
        'hoge': u"ほげ",
    })
    return render_to_response('prof/index.html', ctxt)

