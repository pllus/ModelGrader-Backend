# Generated by Django 4.1.2 on 2023-12-19 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_submission_topic'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSubmission',
            fields=[
                ('best_submission_id', models.AutoField(primary_key=True, serialize=False)),
                ('account', models.ForeignKey(db_column='account_id', on_delete=django.db.models.deletion.CASCADE, to='api.account')),
                ('problem', models.ForeignKey(db_column='problem_id', on_delete=django.db.models.deletion.CASCADE, to='api.problem')),
                ('submission', models.ForeignKey(db_column='submission_id', on_delete=django.db.models.deletion.CASCADE, to='api.submission')),
                ('topic', models.ForeignKey(db_column='topic_id', null=True, on_delete=django.db.models.deletion.CASCADE, to='api.topic')),
            ],
        ),
    ]
