from django.contrib import admin
from .models import Baby


class BabyAdmin(admin.ModelAdmin):
    # Define the list of fields to display in the admin interface
    list_display = ('name', 'age', 'allergy')

    # Add search functionality for specific fields
    search_fields = ('name', 'age', 'allergy')

    # Add filters for the name, age, and allergy fields in the sidebar
    list_filter = ('name', 'age', 'allergy')

    # Define which fields can be clicked to view the details page
    list_display_links = ('name',)

    # Define how fields are displayed when editing a Baby instance
    fields = ('name', 'age', 'allergy')


# Register the model and admin class
admin.site.register(Baby, BabyAdmin)
