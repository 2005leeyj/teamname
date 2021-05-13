from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def result(request)
    inputvalue = int(request.GET['teamnumber'])

    if inputnumber == 1:
        resultvalue = "1팀 최고"
    else:
        resultvalue = "안녕하세요"
        return render(request, "result.html", {'result':resultvalue})