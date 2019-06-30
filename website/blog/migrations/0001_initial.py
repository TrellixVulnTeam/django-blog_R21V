# Generated by Django 2.2.2 on 2019-06-26 20:41

import blog.models
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='博客分类')),
            ],
            options={
                'verbose_name': '博客分类',
                'verbose_name_plural': '博客分类',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('img', models.ImageField(blank=True, null=True, upload_to=blog.models.user_image_file_path, verbose_name='用户头像')),
                ('has_confirmed', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserEmailConfirm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=256)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.User')),
            ],
            options={
                'verbose_name': '邮件确认码',
                'verbose_name_plural': '邮件确认码',
                'ordering': ['-c_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='博客标签')),
                ('category', models.ManyToManyField(to='blog.Category', verbose_name='所属标签')),
            ],
            options={
                'verbose_name': '博客标签',
                'verbose_name_plural': '博客标签',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=164, verbose_name='项目名称')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='项目描述')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='文章标题')),
                ('img', models.ImageField(blank=True, null=True, upload_to=blog.models.bolg_image_file_path, verbose_name='博客配图')),
                ('body', models.TextField(verbose_name='博客正文')),
                ('visiting', models.PositiveIntegerField(default=0, verbose_name='博客访问量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.User', verbose_name='博客作者')),
                ('category', models.ManyToManyField(to='blog.Category', verbose_name='博客分类')),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='博客标签')),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='书本名称')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '未读'), (1, '阅读中'), (2, '已读完')], default=0, verbose_name='阅读状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='所属类别')),
            ],
            options={
                'verbose_name': '书籍',
                'verbose_name_plural': '书籍',
            },
        ),
    ]
