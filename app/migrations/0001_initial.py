# Generated by Django 2.1.1 on 2018-12-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Functiondetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fun', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NOnveg150',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nonveg200',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nonveg300',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nonveg350',
            fields=[
                ('item_id', models.IntegerField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Nonveg400',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='orderdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField()),
                ('d_add', models.CharField(max_length=500)),
                ('food_type', models.CharField(max_length=50)),
                ('d_date', models.DateField()),
                ('no_plates', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='swetdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sweet', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userregisteration',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('cno', models.IntegerField(default=10)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('add', models.CharField(max_length=500)),
                ('username', models.CharField(max_length=12)),
                ('password', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='veg150',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='veg200',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='veg300',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='veg350',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='veg400',
            fields=[
                ('item_id', models.IntegerField(default=5, primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=50)),
                ('item_type', models.CharField(max_length=50)),
                ('item_plate', models.CharField(max_length=20)),
            ],
        ),
    ]
