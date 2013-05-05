# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'series_s_e.id'
        db.delete_column('main_series_s_e', 'id')


        # Changing field 'series_s_e.ssemapid'
        db.alter_column('main_series_s_e', 'ssemapid', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))
        # Adding unique constraint on 'series_s_e', fields ['ssemapid']
        db.create_unique('main_series_s_e', ['ssemapid'])

        # Deleting field 'episode.id'
        db.delete_column('main_episode', 'id')


        # Changing field 'episode.ssemapid'
        db.alter_column('main_episode', 'ssemapid', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True))
        # Adding unique constraint on 'episode', fields ['ssemapid']
        db.create_unique('main_episode', ['ssemapid'])

        # Deleting field 'series.id'
        db.delete_column('main_series', 'id')


        # Changing field 'series.seriesid'
        db.alter_column('main_series', 'seriesid', self.gf('django.db.models.fields.IntegerField')(primary_key=True))
        # Adding unique constraint on 'series', fields ['seriesid']
        db.create_unique('main_series', ['seriesid'])


    def backwards(self, orm):
        # Removing unique constraint on 'series', fields ['seriesid']
        db.delete_unique('main_series', ['seriesid'])

        # Removing unique constraint on 'episode', fields ['ssemapid']
        db.delete_unique('main_episode', ['ssemapid'])

        # Removing unique constraint on 'series_s_e', fields ['ssemapid']
        db.delete_unique('main_series_s_e', ['ssemapid'])


        # User chose to not deal with backwards NULL issues for 'series_s_e.id'
        raise RuntimeError("Cannot reverse this migration. 'series_s_e.id' and its values cannot be restored.")

        # Changing field 'series_s_e.ssemapid'
        db.alter_column('main_series_s_e', 'ssemapid', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'episode.id'
        raise RuntimeError("Cannot reverse this migration. 'episode.id' and its values cannot be restored.")

        # Changing field 'episode.ssemapid'
        db.alter_column('main_episode', 'ssemapid', self.gf('django.db.models.fields.CharField')(max_length=50))

        # User chose to not deal with backwards NULL issues for 'series.id'
        raise RuntimeError("Cannot reverse this migration. 'series.id' and its values cannot be restored.")

        # Changing field 'series.seriesid'
        db.alter_column('main_series', 'seriesid', self.gf('django.db.models.fields.IntegerField')())

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
            'aired': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'ssemapid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        'main.series': {
            'Meta': {'object_name': 'series'},
            'actor': ('django.db.models.fields.TextField', [], {}),
            'airday': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'fanart': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'genre': ('django.db.models.fields.TextField', [], {}),
            'imdbid': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'rating': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'runtime': ('django.db.models.fields.IntegerField', [], {}),
            'seriesid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        'main.series_s_e': {
            'Meta': {'object_name': 'series_s_e'},
            'episodeid': ('django.db.models.fields.IntegerField', [], {}),
            'seasonid': ('django.db.models.fields.IntegerField', [], {}),
            'seriesid': ('django.db.models.fields.IntegerField', [], {}),
            'ssemapid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
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