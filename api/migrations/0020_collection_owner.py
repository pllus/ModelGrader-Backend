# Generated by Django 4.1.2 on 2023-04-22 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_collection_topiccollection_collectionproblem'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='owner',
            field=models.ForeignKey(db_column='owner_id', default=4, on_delete=django.db.models.deletion.CASCADE, to='api.account'),
            preserve_default=False,
        ),
    ]
