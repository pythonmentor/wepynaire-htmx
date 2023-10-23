from functools import wraps
from re import sub

from django.urls import path, re_path
from django.views.generic import View
from django.http import HttpResponseNotAllowed
from django.utils.log import log_response


class Router:
    """Router registering related views urls automatically."""

    class _UrlConfig:
        def __init__(self, urls):
            self.urlpatterns = urls

    def __init__(self):
        """Initializes a new router object."""
        self._urlpatterns = []

    def _process_decorator(
        self,
        pathfunc,
        func=None,
        *,
        url_path=None,
        url_name=None,
        methods=None,
    ):
        """Implements the router decorators to register views."""
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

        return decorator if func is None else decorator(func)

    def url(self, func=None, *, url_path=None, url_name=None, methods=None):
        """Decorator used to register a view with a router, using a list of
        allowed methods."""
        return self._process_decorator(
            path, func, url_path=url_path, url_name=url_name, methods=methods
        )

    def get(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the GET
        HTTP method."""
        return self._process_decorator(
            path, func, url_path=url_path, url_name=url_name, methods=["GET"]
        )

    def post(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the POST
        HTTP method."""
        return self._process_decorator(
            path, func, url_path=url_path, url_name=url_name, methods=["POST"]
        )

    def put(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the PUT
        HTTP method."""
        return self._process_decorator(
            path, func, url_path=url_path, url_name=url_name, methods=["PUT"]
        )

    def patch(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the PATCH
        HTTP method."""
        return self._process_decorator(
            path, func, url_path=url_path, url_name=url_name, methods=["PATCH"]
        )

    def delete(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the DELETE
        HTTP method."""
        return self._process_decorator(
            path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=["DELETE"],
        )

    def re_url(self, func=None, *, url_path=None, url_name=None, methods=None):
        """Decorator used to register a view with a router, using a list of
        allowed methods and the re_path function."""
        return self._process_decorator(
            re_path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=methods,
        )

    def re_get(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the GET HTTP
        method and the re_path function."""
        return self._process_decorator(
            re_path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=["GET"],
        )

    def re_post(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the POST HTTP
        method and the re_path function."""
        return self._process_decorator(
            re_path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=["POST"],
        )

    def re_put(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the PUT HTTP
        method and the re_path function."""
        return self._process_decorator(
            re_path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=["PUT"],
        )

    def re_patch(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the PATCH
        HTTP method and the re_path function."""
        return self._process_decorator(
            re_path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=["PATCH"],
        )

    def re_delete(self, func=None, *, url_path=None, url_name=None):
        """Decorator used to register a view with a router, using the DELETE
        HTTP method and the re_path function."""
        return self._process_decorator(
            re_path,
            func,
            url_path=url_path,
            url_name=url_name,
            methods=["DELETE"],
        )

    @property
    def urls(self):
        """Returns the URL configuration for the current router, to be used
        the django's include function."""
        return self._UrlConfig(urls=self._urlpatterns.copy())
