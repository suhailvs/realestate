from django.shortcuts import render
import csv
# Create your views here.

class ReadCSV:
    def format_latlogs(self, latlogs):
        """
        INPUT: ['76.4600737 10.5997217', '76.459953 10.5995977', '76.4598323 10.5995819', '76.4597679 10.5996399',...
        OUTPUT: [[10.59, 76.45],[10.5901, 76.4503],
        """
        resp = []
        for latlog in latlogs:
            f_latlog = latlog.split(' ')
            resp.append([float(f_latlog[1]),float(f_latlog[0])])
        return resp

    def get(self):
        csvfile = open('map/static/data.csv')
        rows = csv.reader(csvfile, delimiter=',', quotechar='"')
        f_latlogs = []
        for i,row in enumerate(rows):
            if i == 0:continue # if header then skip

            data = row[0].replace('POLYGON ((','').replace('))','').split(', ')
            f_latlogs.append(self.format_latlogs(data))

        return f_latlogs    

def home(request):
    """
    latlngs =  [
        [[10.59, 76.45],[10.5901, 76.4503],[10.5808, 76.4501]],
        [[10.5903, 76.4502],[10.5901, 76.4504],[10.5808, 76.4501]]      
    ];
    """
    r_csv = ReadCSV()
    f_latlogs = r_csv.get()
    return render(request, 'map/home.html',{'f_latlogs':f_latlogs})