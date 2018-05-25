from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'text': 'hello world', 'number': 100}
    return render(request, 'basic_template_url_app/thursday_list.html', context_dict)


def other(request):
    return render(request, 'basic_template_url_app/other.html')


def relative(request):
    return render(request, 'basic_template_url_app/relative_url_templates.html')
