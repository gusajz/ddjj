# -*- coding: utf-8 -*-

from django.db import models

from polymorphic import PolymorphicModel


class PreviousJob(models.Model):
    begin_date = models.DateField()
    end_date = models.DateField()
    company = models.CharField(max_length=50)
    company_activity = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    was_state_related = models.BooleanField()


class Income(models.Model):
    affidavit = models.ForeignKey(Affidavit)
    ammount_year = models.DecimalField(
        max_digits=12, decimal_places=2)
    notes = models.TextField()


class Property(PolymorphicModel):
    percentage = models.DecimalField()
    buy_year = models.DateField()

    bought_value = models.DecimalField()

    affidavit = models.ForeignKey(Affidavit)

    # REVIEW
    money_origin = models.CharField(max_length=100)


class FiscalProperty(Property):

    """
        Propiedades con valor fiscal
    """

    fiscal_value = models.DecimalField()    # Only valid value.


class PaperProperty(Property):

    """
    """
    current_value = models.DecimalField()


class RealState(FiscalProperty):
    HOUSE = 'H'
    PROPERTY_TYPE_CHOICES = (
        (HOUSE, 'Casa'),
    )

    property_type = models.CharField(
        max_length=1, choices=PROPERTY_TYPE_CHOICES, default=HOUSE)

    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    size = models.DecimalField()

    unidad = models.DecimalField()  # no tengo idea de lo que es esto.

    improvements = models.DecimalField()


class CompanyShare(PaperProperty):

    society_type = models.CharField(max_length=100)

    company_activity = models.CharField(max_length=100)

    state_related = models.BooleanField()


class FinanctialProperty(PaperProperty):

    """
        Acciones
    """
    STOCKS = 'S'
    PROPERTY_TYPE_CHOICES = (
        (STOCKS, 'Acciones'),
    )

    property_type = models.CharField(
        max_length=1, choices=PROPERTY_TYPE_CHOICES, default=STOCKS)

    description = models.CharField(max_length=100)

    company_activity = models.CharField(max_length=100)

    quantity = models.IntegerField()


class BankAccount(models.Model):
    CHECKING_ACCOUNT = 'C'
    SAVINGS_ACCOUNT = 'S'

    ACCOUNT_TYPE_CHOICES = (
        (CHECKING_ACCOUNT, 'Cuenta Corriente'),
        (SAVINGS_ACCOUNT, 'Cuenta Corriente'),
    )

    property_type = models.CharField(
        max_length=1, choices=PROPERTY_TYPE_CHOICES, default=STOCKS)
    currency = models.CharField(max_length=3, default='ARS')


class PersonalProperty(FiscalProperty):

    """
        Bienes muebles
        Tal vez todas las propiedades deberían tener un padre común.
    """

    CAR = 'C'
    PROPERTY_TYPE_CHOICES = (
        (CAR, 'Automotor'),
    )

    property_type = models.CharField(
        max_length=1, choices=PROPERTY_TYPE_CHOICES, default=CAR)
    description = models.CharField(max_length=100)

    fabrication_year = models.DateField()


class Jurisdiction(models.Model):

    """
        Provincia, Ciudad, Nación

        Esto no se si tiene sentido.
        Por ahí debería ser directamente el departamento.
        Ministerio de Seguridad de la


        Ejemplo:
            name: La Pampa
            parent = Argentina

            name: Argentina
            parent: None

            name: Bolivia
            parent: None
    """
    name = models.CharType(max_length=50)
    parent = ForeignKey(Jurisdiction)


class AffidavitTemplate(models.Model):

    """
        El modelo de una declaración jurada.
        Por ejemplo:
            Las DDJJ de la Ciudad eran completadas a mano creo que hasta 2009.
            Las DDJJ del Poder Judicial, tienen otras características.
            Acá debería poner de qué juridiscción, poder, etc. y la fecha
            o rango defechas.

        Entonces se debería poder buscar: del Buenos Aires, el Poder Ejecutivo,
        de tal a tal fecha, cuál es el template usado.
    """

    LEGISLATURE = 'L'
    EXECUTIVE = 'E'
    JUDICIARY = 'J'
    POWER_CHOICES = (
        (LEGISLATURE, 'Legislativo'),
        (EXECUTIVE, 'Ejecutivo'),
        (JUDICIARY, 'Judicial'),
    )

    power = models.CharField(
        max_length=1, choices=POWER_CHOICES, default=EXECUTIVE)
    jurisdiction = models.ForeignKey(Jurisdiction)
    # El instructivo para completar.
    sample_document = models.FileField(upload_to='documents')
    init_date = models.DateField()
    finish_date = models.DateField()


class Document(models.Model):

    """
        Un documento scaneado con una declaración jurada.
    """
    document_file = models.FileField(upload_to='documents')
    upload_date = models.DateTimeField()

    # qué formato tiene la declaración jurada.
    template = models.ForeignKey(AffidavitTemplate)

    notes = models.TextField()


class OtherActivities(models.Model):
    company = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    init_date = models.DateField()
    finish_date = models.DateField()
    leave = models.BooleanField()  # licencia
    hours_per_week = models.DecimalField()
    state_related = models.BooleanField()


class Affidavit(models.Model):

    """
        Una declaración jurada.
    """
    MARRIED = 'M'
    SINGLE = 'S'
    DIVORCED = 'D'
    WIDOWER = 'W'

    MARITAL_STATUS_CHOICES = (
        (MARRIED, 'Casado'),
        (SINGLE, 'Soltero'),
        (DIVORCED, 'Divorciado'),
        (WIDOWER, 'Viudo'),
    )
    # que a su vez tiene un template de donde se saca la jurisdicción y el
    # poder.
    original_document = models.OneToOneField(Document)

    submission_date = models.DateTimeField()

    # Datos personales que no cambian de una declaración jurada a otra (DNI,
    # nombre, etc.)
    person = models.ForeignKey(Person)
    marital_status = models.CharField(
        max_length=1, choices=MARITAL_STATUS_CHOICES, default=MARRIED)

    # Datos del cargo.
    position_entry_date = models.DateField()
    position = models.ForeignKey(Position)
    # tipo de contrato, probablemente lo debería hacer CHOICES
    contract_type = models.CharField(max_length=50)
    anual_net_salary = models.DecimalField(
        max_digits=12, decimal_places=2)

    # Estudios
    # REVIEW
    studies = models.CharField(max_length=100)

    spouse = models.ForeifnKey(Person)
    sons = models.ManyToMany(Person)

    voluntary_retirement = models.BooleanField()

    worked_before_position = models.BoolearField()


class Person(models.Model):

    """
        Datos que no cambian de una persona de una a otra declaración jurada.
        Lo que puede cambiar (cargos, de estado civil, de bienes, etc. va en la declaración)
    """
    DNI = 'D'
    ID_TYPE_CHOICES = (
        (DNI, 'DNI')
    )

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Masculino'),
        (FEMALE, 'Femenino')
    )

    id_type = models.CharField(
        max_length=1, choices=ID_TYPE_CHOICES, default=DNI)
    id_number = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = DateField()
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, default=MALE)
    notes = models.TextField()


class Office(models.Model):

    """
        Ministerio, subsecretaría, etc.
        Nota:
            Si se elimina un ministerio o subsecretaría, no se elimina de la base de datos porque arruinaría la integridad referencial.
            En ese caso, se lo deja, pero simplemente no tiene más declaraciones juradas. Por ahí se podría poner una fecha de creación y eliminación.
            Si se crea uno, pasa lo mismo.

            Si se cambia de padre (una subsecretaría pasa a depender de otro ministerio), no pasa nada, simplemente, se crea una nueva oficina con otro padre.

    """
    name = models.CharField(max_length=100)
    parent = models.ForeignKey(Office)

    # Hay que pensar esto mejor: El problema es que cuando se crea un documento con un Document Template, no se sabe a que oficina corresponde.
    # Solamente se sabe que corresponde a una jurisdicción determinada.
    # La oficina se conoce cuando se crea la DDJJ, pero esa oficina tiene que tener una jurisdicción
    # Entonces, se crea una referencia circular.
    jurisdiction = models.ForeignKey(Jurisdiction)


class Position(models.Model):

    """
    Cargo
    """
    name = models.CharField(max_length=100)
    office = models.ForeignKey(Office)

    notes = models.TextField()
