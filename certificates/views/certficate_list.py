from django.views.generic import ListView
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from certificates.models import Certificate

@method_decorator(permission_required("certificates.view_certificate", login_url="/accounts/login/illustration-login/"), name='dispatch')
@method_decorator(login_required(login_url="/accounts/login/illustration-login/"), name='dispatch')
class CertificateListView(ListView):
    model = Certificate
    template_name = "pages/certificate_list.html"
    context_object_name = "certificates"
