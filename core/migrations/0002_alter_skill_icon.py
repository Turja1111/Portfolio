from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='icon',
            field=models.CharField(blank=True, help_text='Font Awesome CSS class for icon', max_length=100),
        ),
    ]
