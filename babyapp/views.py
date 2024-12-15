from django.shortcuts import render, redirect
from .forms import DataEntryForm
from .models import Baby

# View to input new data
def input_data(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_data')  # Redirect to the page that shows all data entries
    else:
        form = DataEntryForm()
    return render(request, 'input_data.html', {'form': form})

# View to display all data entries
def view_data(request):
    data_entries = Baby.objects.all().order_by('-created_at_date')  # Order by the most recent first
    return render(request, 'view_data.html', {'data_entries': data_entries})

def home(request):
    # Retrieve recent entries
    recent_entries = Baby.objects.all().order_by('-created_at_date')[:5]  # Get the latest 5 entries

    return render(request, 'home.html', {
        'recent_entries': recent_entries
    })