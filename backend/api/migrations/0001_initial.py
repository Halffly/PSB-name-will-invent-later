# Generated by Django 3.0.6 on 2021-04-17 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prototype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('views', models.IntegerField(default=0)),
                ('ratings', models.IntegerField(default=0)),
                ('img', models.ImageField(upload_to='', verbose_name='prototype/')),
                ('isShow', models.BooleanField(default=False)),
                ('description', models.TextField(null=True)),
                ('publicKey', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='QuestionStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('prototype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Prototype')),
                ('question', models.ManyToManyField(to='api.QuestionStep')),
            ],
        ),
        migrations.CreateModel(
            name='Taps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=300)),
                ('path', models.TextField(blank=True, null=True)),
                ('classElement', models.TextField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('resource_id', models.TextField(blank=True, null=True)),
                ('content_desc', models.TextField(blank=True, null=True)),
                ('windowType', models.TextField(blank=True, null=True)),
                ('label', models.TextField(blank=True, null=True)),
                ('accessibilityId', models.TextField(blank=True, null=True)),
                ('parentClass', models.TextField(blank=True, null=True)),
                ('time', models.CharField(max_length=500)),
                ('ui', models.TextField()),
                ('xPos', models.FloatField()),
                ('yPos', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='UserAnalytics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('feedBack', models.TextField(null=True)),
                ('finalComment', models.TextField(null=True)),
                ('isFinished', models.BooleanField(default=False)),
                ('averageRate', models.IntegerField()),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Step')),
                ('taps', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Taps')),
            ],
        ),
    ]
