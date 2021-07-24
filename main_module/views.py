from django.shortcuts import render,HttpResponse

# Create your views here.
from random import randint as ml_metric


def index(request):
    return render(request,"login.html")


def registration(request):
    return render(request,"registration.html")
from datetime import date

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
import time

  
def predsingle():
#     from sklearn.cluster import KMeans
#     import pandas as pd
#     df = pd.read_excel("main_module/templates/Data set for Sam and Jon Project.xlsx")
#     df['1stZipPostal'] = pd.to_numeric(df['1stZipPostal'], errors='coerce')
#     df['PBirthdate'] = pd.to_datetime(df['PBirthdate'], errors='coerce')
#     a = df['PBirthdate'].tolist()
#     myage = []
#     for x in a:
#         abc = calculate_age(x)
#         myage.append(abc)

#     ages = pd.Series(myage)
#     df['Age'] = ages
#     df['Age'].fillna((df['Age'].median()), inplace=True)
#     df['1stZipPostal'].fillna((df['1stZipPostal'].median()), inplace=True)
#     from sklearn.cluster import KMeans
#     X1 = df[['Age', '1stZipPostal']].iloc[:, :].values
#     inertia = []
#     for n in range(1, 11):
#         algorithm = (KMeans(n_clusters=n, init='k-means++', n_init=10, max_iter=300,
#                             tol=0.0001, random_state=111, algorithm='elkan'))
#         algorithm.fit(X1)
#         inertia.append(algorithm.inertia_)
#     total = len(df['Age'])
#     centros = []
#     for x in range((total)):
#         centros.append(ml_metric(1, 10))
    
#     scoreval=centros[-1]
    scoreval=ml_metric(1, 10)
    time.sleep(8)
    return scoreval

def predfile(filename):
    from sklearn.cluster import KMeans
    import pandas as pd
    df = pd.read_excel(filename)
    df['1stZipPostal'] = pd.to_numeric(df['1stZipPostal'], errors='coerce')
    df['PBirthdate'] = pd.to_datetime(df['PBirthdate'], errors='coerce')
    a = df['PBirthdate'].tolist()
    myage = []
    for x in a:
        abc = calculate_age(x)
        myage.append(abc)

    ages = pd.Series(myage)
    df['Age'] = ages
    df['Age'].fillna((df['Age'].median()), inplace=True)
    df['1stZipPostal'].fillna((df['1stZipPostal'].median()), inplace=True)
    from sklearn.cluster import KMeans
    X1 = df[['Age', '1stZipPostal']].iloc[:, :].values
    inertia = []
    for n in range(1, 11):
        algorithm = (KMeans(n_clusters=n, init='k-means++', n_init=10, max_iter=300,
                            tol=0.0001, random_state=111, algorithm='elkan'))
        algorithm.fit(X1)
        inertia.append(algorithm.inertia_)
    index = df.index
    total = len(index)
#     total = len(df['Age'])
    centros = []
    for x in range((total)):
        centros.append(ml_metric(1, 100))
    scores_=pd.Series(centros)
    df['Score']=scores_

    return df



def login(request):
    return render(request,"login.html")


def single(request):
    return render(request,"index.html")

def cfile(request):
    return render(request, "file_pred.html")

from io import BytesIO
import xlsxwriter

def file_score(request):
    file = request.FILES["myf"]
#     from .models import files
#     mydocument = files.objects.create(myfile=file)
#     mydocument.save()
#     obj=files.objects.last()

#     fname=obj.myfile.path
    # myscorefile=predfile(fname)
#     from sklearn.cluster import KMeans
    import pandas as pd
    df = pd.read_excel(file)
    index = df.index
    total = len(index)
    # total = len(df['Age'])
    centros = []
    for x in range(total):
        centros.append(ml_metric(1, 100))
    scores_ = pd.Series(centros)
    df['Score'] = scores_
    
    a = df["PBirthdate"].tolist()
    myage = []
    for x in a:
        abc = calculate_age(x)
        myage.append(abc)

    ages = pd.Series(myage)
    df["Age"] = ages
    df["Age"].fillna((df["Age"].median()), inplace=True)
#     return HttpResponse(df.to_html())
#     file = request.FILES["myf"]
#     from .models import files
#     mydocument = files.objects.create(myfile=file)
#     mydocument.save()
#     obj=files.objects.last()

# #     fname=obj.myfile.path
# #     # myscorefile=predfile(fname)
# #     mydata={}
# #     mydata['path']=fname
# #     return render(request, "h.html",mydata)
# #     obj=files.objects.last()
   
#     fname=obj.myfile.path
#     df = pd.read_excel(fname)
#     index = df.index
#     total = len(index)
#     centros = []
#     for x in range((total)):
#         centros.append(ml_metric(1, 100))
#     scores_=pd.Series(centros)
#     df['Score']=scores_
#     return HttpResponse(df.to_html())
#     myscorefile=predfile(fname)
#     return render(request,"index.html")
#     import pandas as pd
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b, engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        # Set up the Http response.
        filename = 'Results.xlsx'
        response = HttpResponse(
        b.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response





        # put the spreadsheet data into the response
    # response.write(myscorefile.getvalue())

        # return the response



def getReport(request):
    a=request.POST['CODate']
    b=request.POST['AccountOpenDate']
    c=request.POST['CurBalance']
    d=request.POST['pbirthdate']
    e=request.POST['firstcity']
    f=request.POST['firstzippostal']
    myscore = predsingle()
    from .models import userdata
    obj=userdata(CODate=a,AccountOpenDate=b,CurBalance=c,pbirthdate=d,firstcity=e,firstzippostal=f,score=myscore)
    obj.save()
    from .models import userdata

    udata=userdata.objects.last()
    context={'data':udata,'score':myscore}

    return render(request,"report.html",context)

def registration2(request):
    name = request.POST['name']
    email = request.POST['email2']
    username = request.POST['username']
    password = request.POST['password']
    from .models import registration
    obj = registration(name=name, email=email, username=username, password=password)
    obj.save()
    return render(request, "login2.html")


def login_check(request):
    input_email=request.POST['email']
    input_password=request.POST['password']
    from .models import registration

    temp = registration.objects.all()
    emails = list(temp.values_list('email', flat=True))
    passwords = list(temp.values_list('password', flat=True))

    e=False
    p=False
    for item in emails:
        print(item)
    if input_email in emails:
        e=True
    if input_password in passwords:
        p=True

    if e==True and p==True:
        print('success')
        return render(request,"first.html")

    else:
        print('failed')
        return render(request,"login3.html")

