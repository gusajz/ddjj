# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Document.upload_date'
        db.delete_column(u'ddjjapp_document', 'upload_date')


    def backwards(self, orm):
        # Adding field 'Document.upload_date'
        db.add_column(u'ddjjapp_document', 'upload_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=None),
                      keep_default=False)


    models = {
        u'ddjjapp.affidavit': {
            'Meta': {'object_name': 'Affidavit'},
            'anual_net_salary': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            'contract_type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'original_document': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.Document']", 'unique': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Person']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Position']"}),
            'position_entry_date': ('django.db.models.fields.DateField', [], {}),
            'sons': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'+'", 'symmetrical': 'False', 'to': u"orm['ddjjapp.Person']"}),
            'spouse': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['ddjjapp.Person']"}),
            'studies': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'submission_date': ('django.db.models.fields.DateTimeField', [], {}),
            'voluntary_retirement': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'worked_before_position': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ddjjapp.affidavittemplate': {
            'Meta': {'object_name': 'AffidavitTemplate'},
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_date': ('django.db.models.fields.DateField', [], {}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Jurisdiction']"}),
            'power': ('django.db.models.fields.CharField', [], {'default': "'E'", 'max_length': '1'}),
            'sample_document': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        u'ddjjapp.bankaccount': {
            'Meta': {'object_name': 'BankAccount'},
            'currency': ('django.db.models.fields.CharField', [], {'default': "'ARS'", 'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'property_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'ddjjapp.companyshare': {
            'Meta': {'object_name': 'CompanyShare', '_ormbases': [u'ddjjapp.PaperProperty']},
            'company_activity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'paperproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.PaperProperty']", 'unique': 'True', 'primary_key': 'True'}),
            'society_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_related': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ddjjapp.document': {
            'Meta': {'object_name': 'Document'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'document_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.AffidavitTemplate']"})
        },
        u'ddjjapp.financtialproperty': {
            'Meta': {'object_name': 'FinanctialProperty', '_ormbases': [u'ddjjapp.PaperProperty']},
            'company_activity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'paperproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.PaperProperty']", 'unique': 'True', 'primary_key': 'True'}),
            'property_type': ('django.db.models.fields.CharField', [], {'default': "'S'", 'max_length': '1'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {})
        },
        u'ddjjapp.fiscalproperty': {
            'Meta': {'object_name': 'FiscalProperty'},
            'affidavit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Affidavit']"}),
            'bought_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'buy_year': ('django.db.models.fields.DateField', [], {}),
            'fiscal_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money_origin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'ddjjapp.income': {
            'Meta': {'object_name': 'Income'},
            'affidavit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Affidavit']"}),
            'ammount_year': ('django.db.models.fields.DecimalField', [], {'max_digits': '12', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        u'ddjjapp.jurisdiction': {
            'Meta': {'object_name': 'Jurisdiction'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['ddjjapp.Jurisdiction']", 'null': 'True', 'blank': 'True'})
        },
        u'ddjjapp.office': {
            'Meta': {'object_name': 'Office'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Jurisdiction']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Office']"})
        },
        u'ddjjapp.otheractivities': {
            'Meta': {'object_name': 'OtherActivities'},
            'activity': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            'hours_per_week': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'init_date': ('django.db.models.fields.DateField', [], {}),
            'leave': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_related': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ddjjapp.paperproperty': {
            'Meta': {'object_name': 'PaperProperty'},
            'affidavit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Affidavit']"}),
            'bought_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'buy_year': ('django.db.models.fields.DateField', [], {}),
            'current_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money_origin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'})
        },
        u'ddjjapp.person': {
            'Meta': {'object_name': 'Person'},
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_number': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id_type': ('django.db.models.fields.CharField', [], {'default': "'D'", 'max_length': '1'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {})
        },
        u'ddjjapp.personalproperty': {
            'Meta': {'object_name': 'PersonalProperty', '_ormbases': [u'ddjjapp.FiscalProperty']},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'fabrication_year': ('django.db.models.fields.DateField', [], {}),
            u'fiscalproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.FiscalProperty']", 'unique': 'True', 'primary_key': 'True'}),
            'property_type': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'ddjjapp.position': {
            'Meta': {'object_name': 'Position'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'office': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Office']"})
        },
        u'ddjjapp.previousjob': {
            'Meta': {'object_name': 'PreviousJob'},
            'begin_date': ('django.db.models.fields.DateField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'company_activity': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'was_state_related': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'ddjjapp.realstate': {
            'Meta': {'object_name': 'RealState', '_ormbases': [u'ddjjapp.FiscalProperty']},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'fiscalproperty_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.FiscalProperty']", 'unique': 'True', 'primary_key': 'True'}),
            'improvements': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'neighborhood': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'property_type': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'}),
            'size': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['ddjjapp']