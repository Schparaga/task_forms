from django.shortcuts import render, redirect
#from django.contrib import messages
from .forms import TechnicalTask
from .models import Customer
from django.views.generic import DetailView, UpdateView, DeleteView
#from here and further I need it for PDF convert
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa

def index(request):
    return render(request, 'vallox_form/index.html')


class TaskFormView(DetailView):
    model = Customer
    template_name = 'vallox_form/task_review.html'
    context_object_name = 'filled_form'


class TaskFormUpdateView(UpdateView):
    model = Customer
    template_name = 'vallox_form/form.html'
    form_class = TechnicalTask


class TaskFormDeleteView(DeleteView):
    model = Customer
    success_url = '/task'
    template_name = 'vallox_form/task_delete.html'


def task_form(request):
    error = ''    
    if request.method == 'POST':
        form = TechnicalTask(request.POST)
        if form.is_valid():
            form.save()
#            messages.success(request, "The form is submited!")
            return redirect('task')
        else:
            error = "The form is not valid"        
    
    form = TechnicalTask()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'vallox_form/form.html', data)


def task(request):
    task = Customer.objects.all()
    return render(request, 'vallox_form/task.html', {'task': task})

#PDF from here and further ------------------------------------------------------
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


#Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):
        task = Customer.objects.all()
        pdf = render_to_pdf('vallox_form/task.html', {'task': task})
        return HttpResponse(pdf, content_type='application/pdf')



