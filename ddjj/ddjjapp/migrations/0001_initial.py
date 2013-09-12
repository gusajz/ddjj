# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PreviousJob'
        db.create_table(u'ddjjapp_previousjob', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('begin_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('company_activity', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('was_state_related', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ddjjapp', ['PreviousJob'])

        # Adding model 'AffidavitTemplate'
        db.create_table(u'ddjjapp_affidavittemplate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('power', self.gf('django.db.models.fields.CharField')(default='E', max_length=1)),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Jurisdiction'])),
            ('sample_document', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('init_date', self.gf('django.db.models.fields.DateField')()),
            ('finish_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['AffidavitTemplate'])

        # Adding model 'Document'
        db.create_table(u'ddjjapp_document', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('upload_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('template', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.AffidavitTemplate'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['Document'])

        # Adding model 'Affidavit'
        db.create_table(u'ddjjapp_affidavit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('original_document', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.Document'], unique=True)),
            ('submission_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('person', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Person'])),
            ('marital_status', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('position_entry_date', self.gf('django.db.models.fields.DateField')()),
            ('position', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Position'])),
            ('contract_type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('anual_net_salary', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('studies', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('spouse', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['ddjjapp.Person'])),
            ('voluntary_retirement', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('worked_before_position', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ddjjapp', ['Affidavit'])

        # Adding M2M table for field sons on 'Affidavit'
        m2m_table_name = db.shorten_name(u'ddjjapp_affidavit_sons')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('affidavit', models.ForeignKey(orm[u'ddjjapp.affidavit'], null=False)),
            ('person', models.ForeignKey(orm[u'ddjjapp.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['affidavit_id', 'person_id'])

        # Adding model 'Income'
        db.create_table(u'ddjjapp_income', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('affidavit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Affidavit'])),
            ('ammount_year', self.gf('django.db.models.fields.DecimalField')(max_digits=12, decimal_places=2)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['Income'])

        # Adding model 'Property'
        db.create_table(u'ddjjapp_property', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('polymorphic_ctype', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'polymorphic_ddjjapp.property_set', null=True, to=orm['contenttypes.ContentType'])),
            ('percentage', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('buy_year', self.gf('django.db.models.fields.DateField')()),
            ('bought_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('affidavit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Affidavit'])),
            ('money_origin', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'ddjjapp', ['Property'])

        # Adding model 'FiscalProperty'
        db.create_table(u'ddjjapp_fiscalproperty', (
            (u'property_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.Property'], unique=True, primary_key=True)),
            ('fiscal_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'ddjjapp', ['FiscalProperty'])

        # Adding model 'PaperProperty'
        db.create_table(u'ddjjapp_paperproperty', (
            (u'property_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.Property'], unique=True, primary_key=True)),
            ('current_value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'ddjjapp', ['PaperProperty'])

        # Adding model 'RealState'
        db.create_table(u'ddjjapp_realstate', (
            (u'fiscalproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.FiscalProperty'], unique=True, primary_key=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(default='H', max_length=1)),
            ('neighborhood', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('size', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('improvements', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=2)),
        ))
        db.send_create_signal(u'ddjjapp', ['RealState'])

        # Adding model 'CompanyShare'
        db.create_table(u'ddjjapp_companyshare', (
            (u'paperproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.PaperProperty'], unique=True, primary_key=True)),
            ('society_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_activity', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state_related', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ddjjapp', ['CompanyShare'])

        # Adding model 'FinanctialProperty'
        db.create_table(u'ddjjapp_financtialproperty', (
            (u'paperproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.PaperProperty'], unique=True, primary_key=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(default='S', max_length=1)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('company_activity', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['FinanctialProperty'])

        # Adding model 'BankAccount'
        db.create_table(u'ddjjapp_bankaccount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('currency', self.gf('django.db.models.fields.CharField')(default='ARS', max_length=3)),
        ))
        db.send_create_signal(u'ddjjapp', ['BankAccount'])

        # Adding model 'PersonalProperty'
        db.create_table(u'ddjjapp_personalproperty', (
            (u'fiscalproperty_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['ddjjapp.FiscalProperty'], unique=True, primary_key=True)),
            ('property_type', self.gf('django.db.models.fields.CharField')(default='C', max_length=1)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('fabrication_year', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['PersonalProperty'])

        # Adding model 'Jurisdiction'
        db.create_table(u'ddjjapp_jurisdiction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Jurisdiction'])),
        ))
        db.send_create_signal(u'ddjjapp', ['Jurisdiction'])

        # Adding model 'OtherActivities'
        db.create_table(u'ddjjapp_otheractivities', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('activity', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('init_date', self.gf('django.db.models.fields.DateField')()),
            ('finish_date', self.gf('django.db.models.fields.DateField')()),
            ('leave', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hours_per_week', self.gf('django.db.models.fields.DecimalField')(max_digits=3, decimal_places=2)),
            ('state_related', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ddjjapp', ['OtherActivities'])

        # Adding model 'Person'
        db.create_table(u'ddjjapp_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('id_type', self.gf('django.db.models.fields.CharField')(default='D', max_length=1)),
            ('id_number', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('birth_date', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.CharField')(default='M', max_length=1)),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['Person'])

        # Adding model 'Office'
        db.create_table(u'ddjjapp_office', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Office'])),
            ('jurisdiction', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Jurisdiction'])),
        ))
        db.send_create_signal(u'ddjjapp', ['Office'])

        # Adding model 'Position'
        db.create_table(u'ddjjapp_position', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('office', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ddjjapp.Office'])),
            ('notes', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ddjjapp', ['Position'])


    def backwards(self, orm):
        # Deleting model 'PreviousJob'
        db.delete_table(u'ddjjapp_previousjob')

        # Deleting model 'AffidavitTemplate'
        db.delete_table(u'ddjjapp_affidavittemplate')

        # Deleting model 'Document'
        db.delete_table(u'ddjjapp_document')

        # Deleting model 'Affidavit'
        db.delete_table(u'ddjjapp_affidavit')

        # Removing M2M table for field sons on 'Affidavit'
        db.delete_table(db.shorten_name(u'ddjjapp_affidavit_sons'))

        # Deleting model 'Income'
        db.delete_table(u'ddjjapp_income')

        # Deleting model 'Property'
        db.delete_table(u'ddjjapp_property')

        # Deleting model 'FiscalProperty'
        db.delete_table(u'ddjjapp_fiscalproperty')

        # Deleting model 'PaperProperty'
        db.delete_table(u'ddjjapp_paperproperty')

        # Deleting model 'RealState'
        db.delete_table(u'ddjjapp_realstate')

        # Deleting model 'CompanyShare'
        db.delete_table(u'ddjjapp_companyshare')

        # Deleting model 'FinanctialProperty'
        db.delete_table(u'ddjjapp_financtialproperty')

        # Deleting model 'BankAccount'
        db.delete_table(u'ddjjapp_bankaccount')

        # Deleting model 'PersonalProperty'
        db.delete_table(u'ddjjapp_personalproperty')

        # Deleting model 'Jurisdiction'
        db.delete_table(u'ddjjapp_jurisdiction')

        # Deleting model 'OtherActivities'
        db.delete_table(u'ddjjapp_otheractivities')

        # Deleting model 'Person'
        db.delete_table(u'ddjjapp_person')

        # Deleting model 'Office'
        db.delete_table(u'ddjjapp_office')

        # Deleting model 'Position'
        db.delete_table(u'ddjjapp_position')


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'Meta': {'object_name': 'FiscalProperty', '_ormbases': [u'ddjjapp.Property']},
            'fiscal_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.Property']", 'unique': 'True', 'primary_key': 'True'})
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Jurisdiction']"})
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
            'Meta': {'object_name': 'PaperProperty', '_ormbases': [u'ddjjapp.Property']},
            'current_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            u'property_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['ddjjapp.Property']", 'unique': 'True', 'primary_key': 'True'})
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
        u'ddjjapp.property': {
            'Meta': {'object_name': 'Property'},
            'affidavit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ddjjapp.Affidavit']"}),
            'bought_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'buy_year': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'money_origin': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'percentage': ('django.db.models.fields.DecimalField', [], {'max_digits': '3', 'decimal_places': '2'}),
            'polymorphic_ctype': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'polymorphic_ddjjapp.property_set'", 'null': 'True', 'to': u"orm['contenttypes.ContentType']"})
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