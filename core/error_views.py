from django.shortcuts import render


def handler404(request, exception, template_name="core/http_error/404.html"):
    return render(request, template_name, {"title": "404 Page Not Found"}, status=404)


def handler500(request, template_name="core/http_error/500.html"):
    return render(request, template_name, {"title": "500 Internal Server Error"}, status=500
    )


def handler400(request, exception, template_name="core/http_error/400.html"):
    return render(request, template_name, {"title": "400 Bad Request"}, status=400)


def handler403(request, exception, template_name="core/http_error/403.html"):
    return render(request, template_name, {"title": "403 Forbidden"}, status=403)
