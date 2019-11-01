from django.db import migrations, models
from progress.bar import Bar

def compute_score(apps, schema_editor):
    """compute score for new field"""
    values = {'a': 0.0891, 'ą': 0.0099, 'b': 0.0147, 'c': 0.0396, 'ć': 0.0040,
            'd': 0.0325, 'e': 0.0766, 'ę': 0.0111, 'f': 0.0030, 'g': 0.0142,
            'h': 0.0108, 'i': 0.0821, 'j': 0.0228, 'k': 0.0351, 'l': 0.0210,
            'ł': 0.0182, 'm': 0.0280, 'n': 0.0552, 'ń': 0.0020, 'o': 0.0775,
            'ó': 0.0085, 'p': 0.0313, 'q': 0.0014, 'r': 0.0469, 's': 0.0432,
            'ś': 0.0066, 't': 0.0398, 'u': 0.0250, 'v': 0.0004, 'w': 0.0465,
            'x': 0.0002, 'y': 0.0376, 'z': 0.0564, 'ź': 0.0006, 'ż': 0.0083}
    Entry = apps.get_model ('dictionary', 'Entry')

    progress = Bar ("computing harmonic means", max=Entry.objects.count ())
    for entry in Entry.objects.all ():
        entry.score = 1./ sum (map (lambda ch: 1. / values[ch] if ch in values.keys () else 0, entry.text.lower ()))
        entry.save ()
        progress.next ()
    progress.finish ()

class Migration(migrations.Migration):
    """Add a score FloatField and then compute"""

    dependencies = [
        ('dictionary', '0004_auto_20191021_2056'),
    ]

    operations = [
        migrations.AddField (
            model_name='Entry',
            name= 'score',
            field = models.FloatField (default = 0.)
        ),
        migrations.RunPython (compute_score)
    ]
