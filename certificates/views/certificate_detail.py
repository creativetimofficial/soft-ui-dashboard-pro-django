from typing import Any
from django.views.generic import View
from django.shortcuts import render


class CertificateDetailView(View):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.template_name = "pages/certificate_detail.html"

    def get(self, request, *args, **kwargs):
        context = {
            "certificate_name": kwargs["certificate_name"],
            "certificate_lang": kwargs["certificate_lang"],
            "is_import_available": False,
        }
        return render(request, self.template_name, context)
