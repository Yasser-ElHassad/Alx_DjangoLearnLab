from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

@permission_required('myapp.can_edit', raise_exception=True)
def edit_view(request, pk):
    # Your view logic here
    return render(request, 'edit_template.html')

@permission_required('myapp.can_create', raise_exception=True)
def create_view(request):
    # Your view logic here
    return render(request, 'create_template.html')