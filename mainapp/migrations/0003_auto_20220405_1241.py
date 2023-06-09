# Generated by Django 3.2.9 on 2022-04-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='spesification',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Ingliz tili', 'Ingliz tili'), ('Rus tili', 'Rus tili'), ('Xitoy tili', 'Xitoy tili'), ('Matematika', 'Matematika'), ('Mental Arifmetika', 'Mental Arifmetika'), ('Mobile/Android', 'Mobile/Android'), ('Mobile/Ios', 'Mobile/Ios'), ('Mobile/Flutter', 'Mobile/Flutter')], default='Frontend', max_length=20),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='spesification',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Ingliz tili', 'Ingliz tili'), ('Rus tili', 'Rus tili'), ('Xitoy tili', 'Xitoy tili'), ('Matematika', 'Matematika'), ('Mental Arifmetika', 'Mental Arifmetika'), ('Mobile/Android', 'Mobile/Android'), ('Mobile/Ios', 'Mobile/Ios'), ('Mobile/Flutter', 'Mobile/Flutter')], default='Backend', max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='spesification',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Ingliz tili', 'Ingliz tili'), ('Rus tili', 'Rus tili'), ('Xitoy tili', 'Xitoy tili'), ('Matematika', 'Matematika'), ('Mental Arifmetika', 'Mental Arifmetika'), ('Mobile/Android', 'Mobile/Android'), ('Mobile/Ios', 'Mobile/Ios'), ('Mobile/Flutter', 'Mobile/Flutter')], default='Backend', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='spesification',
            field=models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Ingliz tili', 'Ingliz tili'), ('Rus tili', 'Rus tili'), ('Xitoy tili', 'Xitoy tili'), ('Matematika', 'Matematika'), ('Mental Arifmetika', 'Mental Arifmetika'), ('Mobile/Android', 'Mobile/Android'), ('Mobile/Ios', 'Mobile/Ios'), ('Mobile/Flutter', 'Mobile/Flutter')], default='Backend', max_length=20),
        ),
    ]
