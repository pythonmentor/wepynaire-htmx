from functools import wraps
from re import sub

from django.urls import path, re_path
from django.views.generic import View
from django.http import HttpResponseNotAllowed
from django.utils.log import log_response


class Router:
    class _UrlConfig:
        def __init__(self, urls):
            self.urlpatterns = urls

    def __init__(self):
        self._urlpatterns = []

    def _process_decorator(
        self,
        pathfunc,
        *,
        url_path=None,
        url_name=None,
        methods=None,
    ):
        if methods is None:
            methods = ["GET"]

        def decorator(func):
            if isinstance(func, View):
                func = func.as_view()

            path = sub(
                r"^index$", "", url_path or func.__name__.replace("__", "/")
            ).strip()
            if path and not path.endswith("/"):
                path += "/"
            name = (
                url_name or func.__name__.replace("__", "-").replace("_", "-")
            ).strip()

            @wraps(func)
            def wrapper(request, *args, **kwargs):
                if request.method not in methods:
                    response = HttpResponseNotAllowed(methods)
                    log_response(
                        "Method Not Allowed (%s): %s",
                        request.method,
                        request.path,
                        response=response,
                        request=request,
                    )
                    return response
                return func(request, *args, **kwargs)

            self._urlpatterns.append(pathfunc(path, wrapper, name=name))

            return wrapper

        return decorator

    def url(self, url_path=None, url_name=None, methods=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=methods
        )

    def get(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["GET"]
        )

    def post(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["POST"]
        )

    def put(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["PUT"]
        )

    def patch(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["PATCH"]
        )

    def delete(self, url_path=None, url_name=None):
        return self._process_decorator(
            path,
            url_path=url_path,
            url_name=url_name,
            methods=["DELETE"],
        )

    def re_url(self, url_path=None, url_name=None, methods=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=methods
        )

    def re_get(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["GET"]
        )

    def re_post(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["POST"]
        )

    def re_put(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["PUT"]
        )

    def re_patch(self, url_path=None, url_name=None):
        return self._process_decorator(
            path, url_path=url_path, url_name=url_name, methods=["PATCH"]
        )

    def re_delete(self, url_path=None, url_name=None):
        return self._process_decorator(
            path,
            url_path=url_path,
            url_name=url_name,
            methods=["DELETE"],
        )

    @property
    def urls(self):
        return self._UrlConfig(urls=self._urlpatterns.copy())
