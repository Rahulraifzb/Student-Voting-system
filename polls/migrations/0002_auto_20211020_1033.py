# Generated by Django 3.2.8 on 2021-10-20 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='vote',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='polls.poll'),
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(default=0)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='election', to='polls.candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='election', to='polls.poll')),
            ],
        ),
    ]
