from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


class CreatePaper:
    def init(self):
        pass

    def create_paper_1(self, request):
        if request.method == "GET":
            return render(request, "create_paper/create_paper_1.html")
        else:
            print("in the POST method")


def test1(request):
    return render(request, "base.html")

