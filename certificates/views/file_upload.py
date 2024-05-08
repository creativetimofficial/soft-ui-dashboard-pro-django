import csv
import json
from django.http import JsonResponse
from certificates.helpers.csv_helper import CSVHelper
from mailmerge import MailMerge
from certificates.helpers.mail_merge_helper import fill_graduation_certificate
from certificates.helpers.file_helper import get_file_path


def handle_file_upload(request):
    csv = CSVHelper()

    if request.method == "POST" and request.FILES["csv-template"]:
        uploaded_file = request.FILES["csv-template"]

        if not uploaded_file.name.endswith(".csv"):
            return JsonResponse({"error": "Only CSV files are allowed."}, status=400)

        csv_data = []
        try:
            csv_data = csv.read_in_memory_csv_file(uploaded_file)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
        return JsonResponse({"csv_data": csv_data})
    else:
        return JsonResponse(
            {"error": "POST request with a file is required."}, status=400
        )


def generate_file(request):
    pass
