from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timezone


def service(request):
    response_data = {
        "email": "ugbedeojoabba@gmail.com",
        "current_datetime": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "github_url": "https://github.com/Ugbe/hng12-stage1"
    }
    return JsonResponse(response_data, safe=False)
