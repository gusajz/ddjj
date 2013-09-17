# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Property'
        db.delete_table(u'ddjjapp_property')

        # Deleting field 'PaperProperty.property_ptr'
        db.delete_column(u'ddjjapp_paperproperty', u'property_ptr_id')

        # Adding field 'PaperProperty.id'
        db.add_column(u'ddjjapp_paperproperty', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Adding field 'PaperProperty.percentage'
        db.add_column(u'ddjjapp_paperproperty', 'percentage',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'PaperProperty.buy_year'
        db.add_column(u'ddjjapp_paperproperty', 'buy_year',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)

        # Adding field 'PaperProperty.bought_value'
        db.add_column(u'ddjjapp_paperproperty', 'bought_value',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'PaperProperty.affidavit'
        db.add_column(u'ddjjapp_paperproperty', 'affidavit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['ddjjapp.Affidavit']),
                      keep_default=False)

        # Adding field 'PaperProperty.money_origin'
        db.add_column(u'ddjjapp_paperproperty', 'money_origin',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)

        # Deleting field 'FiscalProperty.property_ptr'
        db.delete_column(u'ddjjapp_fiscalproperty', u'property_ptr_id')

        # Adding field 'FiscalProperty.id'
        db.add_column(u'ddjjapp_fiscalproperty', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=None, primary_key=True),
                      keep_default=False)

        # Adding field 'FiscalProperty.percentage'
        db.add_column(u'ddjjapp_fiscalproperty', 'percentage',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=3, decimal_places=2),
                      keep_default=False)

        # Adding field 'FiscalProperty.buy_year'
        db.add_column(u'ddjjapp_fiscalproperty', 'buy_year',
                      self.gf('django.db.models.fields.DateField')(default=None),
                      keep_default=False)

        # Adding field 'FiscalProperty.bought_value'
        db.add_column(u'ddjjapp_fiscalproperty', 'bought_value',
                      self.gf('django.db.models.fields.DecimalField')(default=None, max_digits=10, decimal_places=2),
                      keep_default=False)

        # Adding field 'FiscalProperty.affidavit'
        db.add_column(u'ddjjapp_fiscalproperty', 'affidavit',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['ddjjapp.Affidavit']),
                      keep_default=False)

        # Adding field 'FiscalProperty.money_origin'
        db.add_column(u'ddjjapp_fiscalproperty', 'money_origin',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'Property'
        db.create_table(u'ddjjapp_property', (
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_ddjjapp.property_set', null=True, to=orm['contenttypes.ContentType'])),
            ('buy_year', self.gf('django.db.models.fields.DateField')()),
            ('money_origin', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('bought_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('affidavit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Affidavit'])),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'ddjjapp', ['Property'])

        # Adding field 'PaperProperty.property_ptr'
        db.add_column(u'ddjjapp_paperproperty', u'property_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['ddjjapp.Property'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'PaperProperty.id'
        db.delete_column(u'ddjjapp_paperproperty', u'id')

        # Deleting field 'PaperProperty.percentage'
        db.delete_column(u'ddjjapp_paperproperty', 'percentage')

        # Deleting field 'PaperProperty.buy_year'
        db.delete_column(u'ddjjapp_paperproperty', 'buy_year')

        # Deleting field 'PaperProperty.bought_value'
        db.delete_column(u'ddjjapp_paperproperty', 'bought_value')

        # Deleting field 'PaperProperty.affidavit'
        db.delete_column(u'ddjjapp_paperproperty', 'affidavit_id')

        # Deleting field 'PaperProperty.money_origin'
        db.delete_column(u'ddjjapp_paperproperty', 'money_origin')

        # Adding field 'FiscalProperty.property_ptr'
        db.add_column(u'ddjjapp_fiscalproperty', u'property_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=None, to=orm['ddjjapp.Property'], unique=True, primary_key=True),
                      keep_default=False)

        # Deleting field 'FiscalProperty.id'
        db.delete_column(u'ddjjapp_fiscalproperty', u'id')

        # Deleting field 'FiscalProperty.percentage'
        db.delete_column(u'ddjjapp_fiscalproperty', 'percentage')

        # Deleting field 'FiscalProperty.buy_year'
        db.delete_column(u'ddjjapp_fiscalproperty', 'buy_year')

        # Deleting field 'FiscalProperty.bought_value'
        db.delete_column(u'ddjjapp_fiscalproperty', 'bought_value')

        # Deleting field 'FiscalProperty.affidavit'
        db.delete_column(u'ddjjapp_fiscalproperty', 'affidavit_id')

        # Deleting field 'FiscalProperty.money_origin'
        db.delete_column(u'ddjjapp_fiscalproperty', 'money_origin')


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
            'document_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {}),
            'template': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.AffidavitTemplate']"}),
            'upload_date': ('django.db.models.fields.DateTimeField', [], {})
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