from django.shortcuts import render
from .models import File, Person
import pandas as pd
import xml.etree.ElementTree as ET


def create_db_from_csv(file_path):
    df = pd.read_csv(file_path)
    insert_people(df)


def create_db_from_excel(file_path):
    df = pd.read_excel(file_path)
    insert_people(df)


def create_db_from_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for person in root.findall("person"):
        Person.objects.create(
            first_name=person.findtext("first_name"),
            last_name=person.findtext("last_name"),
            email=person.findtext("email"),
            gender=person.findtext("gender"),
            ip_address=person.findtext("ip_address"),
        )


def insert_people(df):
    for _, row in df.iterrows():
        Person.objects.create(
            first_name=row["first_name"],
            last_name=row["last_name"],
            email=row["email"],
            gender=row["gender"],
            ip_address=row["ip_address"],
        )


def csvRead(request):
    if request.method == "POST":
        file = request.FILES["file"]
        obj = File.objects.create(file=file)
        file_path = obj.file.path

        if file.name.endswith(".csv"):
            create_db_from_csv(file_path)
        elif file.name.endswith(".xlsx") or file.name.endswith(".xls"):
            create_db_from_excel(file_path)
        elif file.name.endswith(".xml"):
            create_db_from_xml(file_path)
        else:
            return render(request, "csv/csv.html", {"error": "Unsupported file type."})

    return render(request, "csv/csv.html")
