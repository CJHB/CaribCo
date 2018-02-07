from django.shortcuts import render
import json, os, gspread
from oauth2client.service_account import ServiceAccountCredentials


def index(request):
    path = CLIENT_SECRETS = os.path.join(
        os.path.dirname(__file__), 'creds.json')
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(path, scope)

    

    if request.method == 'POST':
        print(request.POST["name"])
        sheet = gspread.authorize(credentials).open_by_url("https://docs.google.com/spreadsheets/d/1G9-jXiAxY4xqMlXnAr7c8LR28SRVkF0P1RhnODakCD0/edit?usp=sharing").get_worksheet(0) 
        val = [item for item in sheet.col_values(1) if item]
        # for x in range(6, 15):
        #     sheet.update_cell(x, 1, "")
        #     sheet.update_cell(x, 2, "")
        #     sheet.update_cell(x, 3, "")
        #     sheet.update_cell(x, 4, "")
        if (not request.POST["email"]):
            print("no email")
            return render(request, 'index.html', {})
        if( len(val) == 1 ):
            sheet.update_cell(1, 1, "1")
            sheet.update_cell(1, 2, request.POST["name"])
            sheet.update_cell(1, 3, request.POST["email"])
            sheet.update_cell(1, 4, request.POST["message"])
        elif( len(val) == 0):
            sheet.update_cell(1, 1, "Number")
            sheet.update_cell(1, 2, "Name")
            sheet.update_cell(1, 3, "Email Address")
            sheet.update_cell(1, 4, "message")
            sheet.update_cell(2, 1, "1")
            sheet.update_cell(2, 2, request.POST["name"])
            sheet.update_cell(2, 3, request.POST["email"])
            sheet.update_cell(2, 4, request.POST["message"])
        else:
            sheet.update_cell(len(val) + 1, 1, len(val))
            sheet.update_cell(len(val) + 1, 2, request.POST["name"])
            sheet.update_cell(len(val) + 1, 3, request.POST["email"])
            sheet.update_cell(len(val) + 1, 4, request.POST["message"])
        return render(request, 'index.html', {})
    else:
        print("not OK")
        return render(request, 'index.html', {})
