# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'tv_show.image_wide'
        db.alter_column('main_tv_show', 'image_wide', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.official_website'
        db.alter_column('main_tv_show', 'official_website', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.twitter'
        db.alter_column('main_tv_show', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.image_square'
        db.alter_column('main_tv_show', 'image_square', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.image_iphone'
        db.alter_column('main_tv_show', 'image_iphone', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.imdb'
        db.alter_column('main_tv_show', 'imdb', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.images'
        db.alter_column('main_tv_show', 'images', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'tv_show.image_normal'
        db.alter_column('main_tv_show', 'image_normal', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.title'
        db.alter_column('main_tv_show', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.wikipedia'
        db.alter_column('main_tv_show', 'wikipedia', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.gid'
        db.alter_column('main_tv_show', 'gid', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.program_creator'
        db.alter_column('main_tv_show', 'program_creator', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.image_thumbnail'
        db.alter_column('main_tv_show', 'image_thumbnail', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.status'
        db.alter_column('main_tv_show', 'status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'tv_show.topical_webpage'
        db.alter_column('main_tv_show', 'topical_webpage', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.description'
        db.alter_column('main_tv_show', 'description', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'tv_show.netflix_link'
        db.alter_column('main_tv_show', 'netflix_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.facebook_url'
        db.alter_column('main_tv_show', 'facebook_url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.regular_cast'
        db.alter_column('main_tv_show', 'regular_cast', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'tv_show.starring'
        db.alter_column('main_tv_show', 'starring', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'tv_show.genre'
        db.alter_column('main_tv_show', 'genre', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'tv_show.tvrage'
        db.alter_column('main_tv_show', 'tvrage', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.banner'
        db.alter_column('main_tv_show', 'banner', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'tv_show.image_banner'
        db.alter_column('main_tv_show', 'image_banner', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.freebase_api_response'
        db.alter_column('main_tv_show', 'freebase_api_response', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'tv_show.netflix'
        db.alter_column('main_tv_show', 'netflix', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.url'
        db.alter_column('main_tv_show', 'url', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.guru'
        db.alter_column('main_tv_show', 'guru', self.gf('jsonfield.fields.JSONField')(null=True))

        # Changing field 'tv_show.summary'
        db.alter_column('main_tv_show', 'summary', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'tv_show.trailer_link'
        db.alter_column('main_tv_show', 'trailer_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.itunes_link'
        db.alter_column('main_tv_show', 'itunes_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.amazon_link'
        db.alter_column('main_tv_show', 'amazon_link', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

        # Changing field 'tv_show.tvguide'
        db.alter_column('main_tv_show', 'tvguide', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

        # Changing field 'tv_show.hulu_link'
        db.alter_column('main_tv_show', 'hulu_link', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'tv_show.showtimes'
        db.alter_column('main_tv_show', 'showtimes', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):

        # Changing field 'tv_show.image_wide'
        db.alter_column('main_tv_show', 'image_wide', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.official_website'
        db.alter_column('main_tv_show', 'official_website', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.twitter'
        db.alter_column('main_tv_show', 'twitter', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.image_square'
        db.alter_column('main_tv_show', 'image_square', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.image_iphone'
        db.alter_column('main_tv_show', 'image_iphone', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.imdb'
        db.alter_column('main_tv_show', 'imdb', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.images'
        db.alter_column('main_tv_show', 'images', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'tv_show.image_normal'
        db.alter_column('main_tv_show', 'image_normal', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.title'
        db.alter_column('main_tv_show', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.wikipedia'
        db.alter_column('main_tv_show', 'wikipedia', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.gid'
        db.alter_column('main_tv_show', 'gid', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.program_creator'
        db.alter_column('main_tv_show', 'program_creator', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.image_thumbnail'
        db.alter_column('main_tv_show', 'image_thumbnail', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.status'
        db.alter_column('main_tv_show', 'status', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'tv_show.topical_webpage'
        db.alter_column('main_tv_show', 'topical_webpage', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.description'
        db.alter_column('main_tv_show', 'description', self.gf('django.db.models.fields.TextField')())

        # Changing field 'tv_show.netflix_link'
        db.alter_column('main_tv_show', 'netflix_link', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.facebook_url'
        db.alter_column('main_tv_show', 'facebook_url', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.regular_cast'
        db.alter_column('main_tv_show', 'regular_cast', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'tv_show.starring'
        db.alter_column('main_tv_show', 'starring', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'tv_show.genre'
        db.alter_column('main_tv_show', 'genre', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'tv_show.tvrage'
        db.alter_column('main_tv_show', 'tvrage', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.banner'
        db.alter_column('main_tv_show', 'banner', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'tv_show.image_banner'
        db.alter_column('main_tv_show', 'image_banner', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.freebase_api_response'
        db.alter_column('main_tv_show', 'freebase_api_response', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'tv_show.netflix'
        db.alter_column('main_tv_show', 'netflix', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.url'
        db.alter_column('main_tv_show', 'url', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.guru'
        db.alter_column('main_tv_show', 'guru', self.gf('jsonfield.fields.JSONField')())

        # Changing field 'tv_show.summary'
        db.alter_column('main_tv_show', 'summary', self.gf('django.db.models.fields.TextField')())

        # Changing field 'tv_show.trailer_link'
        db.alter_column('main_tv_show', 'trailer_link', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.itunes_link'
        db.alter_column('main_tv_show', 'itunes_link', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.amazon_link'
        db.alter_column('main_tv_show', 'amazon_link', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'tv_show.tvguide'
        db.alter_column('main_tv_show', 'tvguide', self.gf('django.db.models.fields.URLField')(max_length=200))

        # Changing field 'tv_show.hulu_link'
        db.alter_column('main_tv_show', 'hulu_link', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'tv_show.showtimes'
        db.alter_column('main_tv_show', 'showtimes', self.gf('django.db.models.fields.CharField')(max_length=200))

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
            'amazon_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'banner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'currently_in_production': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'dislikes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'episode_running_time': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'facebook_url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'freebase_api_response': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'genre': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'gid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'guru': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'hulu_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_banner': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_iphone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_normal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_square': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_thumbnail': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'image_wide': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'images': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'imdb': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'itunes_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'likes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'netflix': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'netflix_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'number_of_episodes': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'number_of_seasons': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'official_website': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'program_creator': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'regular_cast': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'reviewed': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'show_year': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'}),
            'showtimes': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'starring': ('jsonfield.fields.JSONField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'topical_webpage': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'trailer_link': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tvguide': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tvrage': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'default': "''", 'max_length': '200', 'null': 'True', 'blank': 'True'})
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