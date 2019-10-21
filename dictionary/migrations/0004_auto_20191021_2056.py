# Generated by Django 2.2.6 on 2019-10-21 20:56

from django.db import migrations
from progress.bar import Bar

def compute_length(apps, schema_editor):
    """compute the length for the whole table"""
    Entry = apps.get_model ('dictionary', 'Entry')
    progress = Bar ('computing lengths', max= Entry.objects.count ())
    for entry in Entry.objects.all ():
        entry.length = len (entry.text)
        entry.save ()
        progress.next ()
    progress.finish ()

class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0003_entry_length'),
    ]

    operations = [
        migrations.RunPython (compute_length)
    ]
