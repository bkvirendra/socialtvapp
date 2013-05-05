# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'subscriptions'
        db.create_table('main_subscriptions', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series', self.gf('django.db.models.fields.IntegerField')()),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('timestamp_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True)),
        ))
        db.send_create_signal('main', ['subscriptions'])

        # Adding field 'series_s_e.timestamp_added'
        db.add_column('main_series_s_e', 'timestamp_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.subscriptions_count'
        db.add_column('main_userprofile', 'subscriptions_count',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.timestamp_added'
        db.add_column('main_userprofile', 'timestamp_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'episode.timestamp_added'
        db.add_column('main_episode', 'timestamp_added',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'series.airdate'
        db.delete_column('main_series', 'airdate')

        # Adding field 'series.airday'
        db.add_column('main_series', 'airday',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'subscriptions'
        db.delete_table('main_subscriptions')

        # Deleting field 'series_s_e.timestamp_added'
        db.delete_column('main_series_s_e', 'timestamp_added')

        # Deleting field 'UserProfile.subscriptions_count'
        db.delete_column('main_userprofile', 'subscriptions_count')

        # Deleting field 'UserProfile.timestamp_added'
        db.delete_column('main_userprofile', 'timestamp_added')

        # Deleting field 'episode.timestamp_added'
        db.delete_column('main_episode', 'timestamp_added')


        # User chose to not deal with backwards NULL issues for 'series.airdate'
        raise RuntimeError("Cannot reverse this migration. 'series.airdate' and its values cannot be restored.")
        # Deleting field 'series.airday'
        db.delete_column('main_series', 'airday')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'main.episode': {
            'Meta': {'object_name': 'episode'},
            'aired': ('django.db.models.fields.DateTimeField', [], {}),
            'fanart': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'ssemapid': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'})
        },
        'main.series': {
            'Meta': {'object_name': 'series'},
            'actor': ('django.db.models.fields.TextField', [], {}),
            'airday': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'genre': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'imdbid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {}),
            'seriesid': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.series_s_e': {
            'Meta': {'object_name': 'series_s_e'},
            'episodeid': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seasonid': ('django.db.models.fields.IntegerField', [], {}),
            'seriesid': ('django.db.models.fields.IntegerField', [], {}),
            'ssemapid': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'})
        },
        'main.subscriptions': {
            'Meta': {'object_name': 'subscriptions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age_range': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'subscriptions_count': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'television': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'timestamp_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']