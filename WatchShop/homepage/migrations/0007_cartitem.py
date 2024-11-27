# Generated by Django 5.1.3 on 2024-11-27 07:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_alter_cart_user_watchreview'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_count', models.IntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.watchesuploads')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.cart')),
            ],
        ),
    ]