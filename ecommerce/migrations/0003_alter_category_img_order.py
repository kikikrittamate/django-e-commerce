# Generated by Django 4.1.7 on 2023-04-14 17:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='img',
            field=models.ImageField(blank=True, upload_to='categories'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='reference number')),
                ('qty', models.IntegerField(default=0)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.customer')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.item')),
            ],
        ),
    ]