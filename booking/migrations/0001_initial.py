# Generated by Django 4.2.10 on 2024-02-19 17:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_id', models.IntegerField(unique=True)),
                ('capacity', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')])),
                ('availability', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['table_id', 'capacity'],
            },
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('reservation_id', shortuuid.django_fields.ShortUUIDField(alphabet=None, length=6, max_length=6, prefix='', primary_key=True, serialize=False)),
                ('guest_name', models.CharField(max_length=50)),
                ('reservation_date', models.DateField()),
                ('reservation_time', models.CharField(choices=[('12pm', '12:00pm - 1.25pm'), ('2pm', '2:00pm - 3:45pm'), ('4pm', '4:00pm - 5:45pm'), ('6pm', '6:00pm - 7:45pm'), ('8pm', '8:00pm - 9:45pm')], max_length=10)),
                ('company_size', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('additional_info', models.TextField(blank=True, max_length=200, null=True)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_guest', to=settings.AUTH_USER_MODEL)),
                ('table_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_table', to='booking.table')),
            ],
            options={
                'ordering': ['reservation_date', 'reservation_time'],
            },
        ),
    ]
