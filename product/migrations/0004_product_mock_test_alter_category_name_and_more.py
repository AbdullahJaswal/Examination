# Generated by Django 4.0.2 on 2022-03-03 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examination', '0002_userproduct_submission_is_correct_submission_user_and_more'),
        ('product', '0003_add_dev_manytomanyto_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='mock_test',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.DeleteModel(
            name='UserProduct',
        ),
    ]
