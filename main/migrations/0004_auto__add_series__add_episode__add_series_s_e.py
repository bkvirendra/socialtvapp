# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'series'
        db.create_table('main_series', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seriesid', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('airdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('actor', self.gf('django.db.models.fields.TextField')()),
            ('genre', self.gf('django.db.models.fields.TextField')()),
            ('imdbid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('overview', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('runtime', self.gf('django.db.models.fields.IntegerField')()),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('main', ['series'])

        # Adding model 'episode'
        db.create_table('main_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ssemapid', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('aired', self.gf('django.db.models.fields.DateTimeField')()),
            ('overview', self.gf('django.db.models.fields.TextField')()),
            ('rating', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('image', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
        ))
        db.send_create_signal('main', ['episode'])

        # Adding model 'series_s_e'
        db.create_table('main_series_s_e', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seriesid', self.gf('django.db.models.fields.IntegerField')()),
            ('seasonid', self.gf('django.db.models.fields.IntegerField')()),
            ('episodeid', self.gf('django.db.models.fields.IntegerField')()),
            ('ssemapid', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('main', ['series_s_e'])


    def backwards(self, orm):
        # Deleting model 'series'
        db.delete_table('main_series')

        # Deleting model 'episode'
        db.delete_table('main_episode')

        # Deleting model 'series_s_e'
        db.delete_table('main_series_s_e')


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
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'ssemapid': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.series': {
            'Meta': {'object_name': 'series'},
            'actor': ('django.db.models.fields.TextField', [], {}),
            'airdate': ('django.db.models.fields.DateTimeField', [], {}),
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
            'ssemapid': ('django.db.models.fields.IntegerField', [], {})
        },
        'main.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'age_range': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'picture': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'television': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['main']