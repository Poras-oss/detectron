from django.shortcuts import render, redirect
from webapp.models import citizen_report
import pyrebase

Config = {
    "apiKey": "AIzaSyBbcAgo0SWllwJk-WNC3UozA6bwbWyYhe8",
    "authDomain": "ai-yantra.firebaseapp.com",
    "databaseURL": "https://ai-yantra-default-rtdb.firebaseio.com",
    "projectId": "ai-yantra",
    "storageBucket": "ai-yantra.appspot.com",
    "messagingSenderId": "432987142899",
    "appId": "1:432987142899:web:91c084348c40f66961d586",
}

firebase = pyrebase.initialize_app(Config)
authe = firebase.auth()
database = firebase.database()


# Create your views here.
def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "pages/dashboard.html")


def login(request):
    return render(request, "pages/login.html")


def main(request):
    return render(request, "pages/main.html")


def viewreport(request):
    return render(request, "pages/view-report.html")


def bookmarks(request):
    return render(request, "pages/bookmark.html")


def analytics(request):
    return render(request, "pages/analytics.html")


def casehistory(request):
    return render(request, "pages/casehistory.html")


def application(request):
    return render(request, "pages/application.html")


def select(request):
    return render(request, "pages/select.html")


def submit(request):
    return render(request, "pages/submit.html")


def citizen(request):
    return render(request, "pages/citizen.html")


# def faq(request):
#     return render(request, "pages/faq.html")

# def notification(request):
#     return render(request, "pages/notification.html")

# def news(request):
#     return render(request, "pages/news.html")


# importing models


def report_citizen(request):
    if request.method == "POST":
        incident_type = request.POST.get("incident")
        location = request.POST.get("location")
        date = request.POST.get("date")
        description = request.POST.get("description")
        media = request.FILES.get("media")
        name = request.POST.get("name")
        email = request.POST.get("email")
        number = request.POST.get("number")
        address = request.POST.get("address")

        report = citizen_report(
            incident_type=incident_type,
            location=location,
            date=date,
            description=description,
            media=media,
            name=name,
            email=email,
            number=number,
            address=address,
        )
        report.save()

        return redirect("submit")

    return render(request, "pages/citizen.html")
