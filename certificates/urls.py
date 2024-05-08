from django.urls import path
from certificates.views.certficate_list import CertificateListView
from certificates.views.certificate_detail import CertificateDetailView
from certificates.views.diploma_detail import DiplomaDetailView
from .views.file_upload import handle_file_upload, generate_file


urlpatterns = [
    path("", CertificateListView.as_view(), name="certificate_list"),
    path(
        "diploma/",
        DiplomaDetailView.as_view(),
        name="diploma_detail",
    ),
    path(
        "<certificate_name>/<certificate_lang>/",
        CertificateDetailView.as_view(),
        name="certificate_detail",
    ),
    path("handle-upload/", handle_file_upload, name="handle_file_upload"),
    path("generate/", generate_file, name="generate_file"),
]
