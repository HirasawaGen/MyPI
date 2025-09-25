from django.http import HttpRequest
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import Http404
from django.http import FileResponse

from django.urls import URLResolver
from django.urls import path

from django.views.decorators.http import require_http_methods as methods
from django.shortcuts import render

import hashlib

from .settings import PACKAGE_ROOT


urlpatterns: list[URLResolver] = []


def register(route: str | None = None, kwargs = None, name: str | None = None):
    def wrapper(func):
        urlpatterns.append(path(route, func, kwargs=kwargs, name=name))
        return func
    return wrapper


@register('test/')
@methods(['GET'])
def test(request: HttpRequest) -> JsonResponse:
    return JsonResponse({'message': 'Hello, world!'})


@register('packages/<path:path>')
@methods(['GET'])
def packages_download(request: HttpRequest, path: str) -> Http404 | FileResponse:
    full_path = PACKAGE_ROOT / path
    if not full_path.is_relative_to(PACKAGE_ROOT):
        return Http404("invalid path.")
    if not full_path.exists():
        return Http404("file not found.")
    return FileResponse(open(full_path, 'rb'))


@register('simple/')
@methods(['GET'])
def simple(request: HttpRequest) -> HttpResponse:
    packages_folder = [dir.name for dir in PACKAGE_ROOT.iterdir() if dir.is_dir()]
    return render(request, 'simple.html', {'packages_folder': packages_folder})

@register('simple/<str:package_name>/')
def package_distributions(request: HttpRequest, package_name: str) -> HttpResponse | Http404:
    package_folder = PACKAGE_ROOT / package_name
    if not package_folder.is_dir():
        return Http404("package not found.")
    sha256 = lambda file: hashlib.sha256(open(file, 'rb').read()).hexdigest()
    data = [(file.name, sha256(file)) for file in package_folder.iterdir() if file.is_file()]
    return render(request, 'package_distributions.html', {'package_name': package_name, 'data': data})
