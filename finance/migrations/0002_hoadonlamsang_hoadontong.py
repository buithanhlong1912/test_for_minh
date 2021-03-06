# Generated by Django 3.1.4 on 2020-12-04 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoaDonLamSang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tong_tien', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HoaDonTong',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoi_gian_tao', models.DateTimeField(blank=True, editable=False, null=True)),
                ('thoi_gian_cap_nhat', models.DateTimeField(blank=True, null=True)),
                ('benh_nhan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hoa_don_tong_nguoi_dung', to=settings.AUTH_USER_MODEL)),
                ('hoa_don_chuoi_kham', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.hoadonchuoikham')),
                ('hoa_don_lam_sang', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.hoadonlamsang')),
                ('hoa_don_thuoc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.hoadonthuoc')),
            ],
        ),
    ]
