from django.shortcuts import render
import csv, io
import pandas as pd
from django.shortcuts import render,redirect
from django.contrib import messages

def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    if request.method == "GET":
        return render(request, template)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if csv_file.name.endswith('.csv'):
        print('hi')
        data = pd.read_csv(csv_file)

        # dropping ALL duplicte values
        data.drop_duplicates(subset="start_action", keep='first', inplace=True)

        df = data

        # saving the dataframe
        df.to_csv(r'C:\Users\evans.n\Django-Projects\AutoProj\out\output.csv')

        messages.success(request, 'You can Download your file below')
        return redirect('http://127.0.0.1:8000/download')
    else:
        messages.error(request, 'THIS IS NOT A CSV FILE')

    return render(request,'notdone.html')



import mimetypes
# import os module
import os
# Import HttpResponse module
from django.http.response import HttpResponse


def download_file(request):
    # Define Django project base directory
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define text file name
    filename = 'output.csv'
    # Define the full file path
    filepath = BASE_DIR + '\\out\\' + filename
    # Open the file for reading content
    path = open(filepath, 'r')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
