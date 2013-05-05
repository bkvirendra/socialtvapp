# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'tv_show.checked_in'
        db.delete_column('main_tv_show', 'checked_in')

        # Deleting field 'tv_show.images_thumbnail'
        db.delete_column('main_tv_show', 'images_thumbnail')

        # Deleting field 'tv_show.images_banner'
        db.delete_column('main_tv_show', 'images_banner')

        # Deleting field 'tv_show.images_wide'
        db.delete_column('main_tv_show', 'images_wide')

        # Adding field 'tv_show.images'
        db.add_column('main_tv_show', 'images',
                      self.gf('jsonfield.fields.JSONField')(default='', blank=True),
                      keep_default=False)

        # Adding field 'tv_show.year'
        db.add_column('main_tv_show', 'year',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'tv_show.checked_in'
        db.add_column('main_tv_show', 'checked_in',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'tv_show.images_thumbnail'
        db.add_column('main_tv_show', 'images_thumbnail',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'tv_show.images_banner'
        db.add_column('main_tv_show', 'images_banner',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Adding field 'tv_show.images_wide'
        db.add_column('main_tv_show', 'images_wide',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200, blank=True),
                      keep_default=False)

        # Deleting field 'tv_show.images'
        db.delete_column('main_tv_show', 'images')

        # Deleting field 'tv_show.year'
        db.delete_column('main_tv_show', 'year')


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
        'main.subscriptions': {
            'Meta': {'object_name': 'subscriptions'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'series': ('django.db.models.fields.IntegerField', [], {}),
            'timestamp_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'main.tv_show': {
            'Meta': {'object_name': 'tv_show'},
            'amazon_link': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'banner': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'dislikes': ('django.db.models.fields.IntegerField', [], {}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'gid': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'guru': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'hulu_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_banner': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'image_iphone': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'image_normal': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'image_square': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'image_thumbnail': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'image_wide': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'images': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'itunes_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {}),
            'netflix_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'reviewed': ('django.db.models.fields.IntegerField', [], {}),
            'showtimes': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'starring': ('jsonfield.fields.JSONField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'trailer_link': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'default': '0'})
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