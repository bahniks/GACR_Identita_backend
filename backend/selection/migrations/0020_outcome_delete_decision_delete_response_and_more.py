# Generated by Django 5.1.1 on 2024-10-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('selection', '0019_alter_participant_lastprogress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_id', models.CharField(default='', max_length=50)),
                ('roundNumber', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('reward', models.IntegerField(default=0)),
                ('version', models.CharField(default='', max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Decision',
        ),
        migrations.DeleteModel(
            name='Response',
        ),
        migrations.RemoveField(
            model_name='group',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='group',
            name='winner',
        ),
        migrations.RemoveField(
            model_name='group',
            name='winning_block',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='finished_after',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='finished_fourth',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='number_in_group',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='pairNumber',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='reward_in_after',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='reward_in_fourth',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='role',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='wins_in_after',
        ),
        migrations.AddField(
            model_name='group',
            name='reward_order',
            field=models.CharField(default='', max_length=12),
        ),
        migrations.AddField(
            model_name='pair',
            name='endowment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pair',
            name='returns',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='pair',
            name='roundNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pair',
            name='sentA',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pair',
            name='sentB',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='pair',
            name='token',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='paidtoken',
            field=models.BooleanField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='pair3',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='participant',
            name='pair4',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='participant',
            name='pair5',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='participant',
            name='pair6',
            field=models.IntegerField(default=-1),
        ),
        migrations.AddField(
            model_name='participant',
            name='token',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participant',
            name='winning_block',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participant',
            name='winning_trust',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='group',
            name='condition',
            field=models.CharField(default='', max_length=15),
        ),
    ]