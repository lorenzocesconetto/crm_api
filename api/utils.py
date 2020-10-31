from django.shortcuts import render


def render_react(request, app_name, props={}):
    return render(
        request, "api/base.html", {"app_name": app_name, "props": props}
    )
