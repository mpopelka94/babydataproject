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
    return render(request, 'tracker/input_data.html', {'form': form})

# View to display all data entries
def view_data(request):
    data_entries = DataEntry.objects.all().order_by('-created_at')  # Order by the most recent first
    return render(request, 'tracker/view_data.html', {'data_entries': data_entries})