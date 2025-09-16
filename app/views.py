from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, "test.html")

def home(request):
    # You can pass context data here if needed
    context = {
        'name': 'Anagh Kumar',
        'title': 'Full Stack Developer & AI Specialist',
    }
    return render(request, 'index.html', context)