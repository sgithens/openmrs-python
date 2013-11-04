# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Person(models.Model):
    person_id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=150, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    birthdate_estimated = models.IntegerField()
    dead = models.IntegerField()
    death_date = models.DateTimeField(null=True, blank=True)
    cause_of_death = models.ForeignKey('Concept', null=True, db_column='cause_of_death', blank=True, related_name='+')
    creator = models.ForeignKey('Users', db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('Users', null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey('Users', null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'person'

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    system_id = models.CharField(max_length=150)
    username = models.CharField(max_length=150, blank=True)
    password = models.CharField(max_length=384, blank=True)
    salt = models.CharField(max_length=384, blank=True)
    secret_question = models.CharField(max_length=765, blank=True)
    secret_answer = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey('self', db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey('self', null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    person = models.ForeignKey(Person, related_name='+')
    retired = models.IntegerField()
    retired_by = models.ForeignKey('self', null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'users'

class ConceptDatatype(models.Model):
    concept_datatype_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    hl7_abbreviation = models.CharField(max_length=9, blank=True)
    description = models.CharField(max_length=765)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_datatype'

class Concept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    #class_field_id = concept_id
    retired = models.IntegerField()
    short_name = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    form_text = models.TextField(blank=True)
    datatype = models.ForeignKey(ConceptDatatype, related_name='+')
    class_field = models.ForeignKey('ConceptClass', db_column="class_id",related_name='+') # Field renamed because it was a Python reserved word. Fixed SWG
    is_set = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    version = models.CharField(max_length=150, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept'

class ActiveListType(models.Model):
    active_list_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'active_list_type'

class ActiveList(models.Model):
    active_list_id = models.IntegerField(primary_key=True)
    active_list_type = models.ForeignKey(ActiveListType, related_name='+')
    person = models.ForeignKey(Person, related_name='+')
    concept = models.ForeignKey(Concept, related_name='+')
    start_obs = models.ForeignKey('Obs', null=True, blank=True, related_name='+')
    stop_obs = models.ForeignKey('Obs', null=True, blank=True, related_name='+')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True, blank=True)
    comments = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'active_list'

class ActiveListAllergy(models.Model):
    active_list_id = models.IntegerField(primary_key=True)
    allergy_type = models.CharField(max_length=150, blank=True)
    reaction_concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    severity = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'active_list_allergy'

class ActiveListProblem(models.Model):
    active_list_id = models.IntegerField(primary_key=True)
    status = models.CharField(max_length=150, blank=True)
    sort_weight = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'active_list_problem'


class CalculationTokenRegistration(models.Model):
    token_registration_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    provider_class_name = models.CharField(max_length=1536)
    calculation_name = models.CharField(max_length=1536)
    configuration = models.TextField(blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'calculation_token_registration'

class ClobDatatypeStorage(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114, unique=True)
    value = models.TextField()
    class Meta:
        db_table = u'clob_datatype_storage'

class Cohort(models.Model):
    cohort_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'cohort'

class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, related_name='+')
    patient = models.ForeignKey('Patient', related_name='+')
    class Meta:
        db_table = u'cohort_member'

class ConceptAnswer(models.Model):
    concept_answer_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, related_name='+')
    answer_concept = models.ForeignKey(Concept, null=True, db_column='answer_concept', blank=True, related_name='+')
    answer_drug = models.ForeignKey('Drug', null=True, db_column='answer_drug', blank=True, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    sort_weight = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'concept_answer'

class ConceptClass(models.Model):
    concept_class_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_class'

class ConceptComplex(models.Model):
    concept = models.ForeignKey(Concept, primary_key=True, related_name='+')
    handler = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'concept_complex'

class ConceptDescription(models.Model):
    concept_description_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, related_name='+')
    description = models.TextField()
    locale = models.CharField(max_length=150)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_description'

class ConceptMapType(models.Model):
    concept_map_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    is_hidden = models.IntegerField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_map_type'

class ConceptName(models.Model):
    concept = models.ForeignKey(Concept, null=True, blank=True) #, related_name='+')
    name = models.CharField(max_length=765)
    locale = models.CharField(max_length=150)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    concept_name_id = models.IntegerField(primary_key=True,unique=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    concept_name_type = models.CharField(max_length=150, blank=True)
    locale_preferred = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'concept_name'

class ConceptNameTag(models.Model):
    concept_name_tag_id = models.IntegerField(unique=True)
    tag = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.IntegerField(null=True, blank=True)
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_name_tag'

class ConceptNameTagMap(models.Model):
    concept_name = models.ForeignKey(ConceptName, related_name='+')
    concept_name_tag = models.ForeignKey(ConceptNameTag, related_name='+')
    class Meta:
        db_table = u'concept_name_tag_map'

class ConceptNumeric(models.Model):
    concept = models.ForeignKey(Concept, primary_key=True, related_name='+')
    hi_absolute = models.FloatField(null=True, blank=True)
    hi_critical = models.FloatField(null=True, blank=True)
    hi_normal = models.FloatField(null=True, blank=True)
    low_absolute = models.FloatField(null=True, blank=True)
    low_critical = models.FloatField(null=True, blank=True)
    low_normal = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=150, blank=True)
    precise = models.IntegerField()
    class Meta:
        db_table = u'concept_numeric'

class ConceptProposal(models.Model):
    concept_proposal_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    encounter = models.ForeignKey('Encounter', null=True, blank=True, related_name='+')
    original_text = models.CharField(max_length=765)
    final_text = models.CharField(max_length=765, blank=True)
    obs = models.ForeignKey('Obs', null=True, blank=True, related_name='+')
    obs_concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    state = models.CharField(max_length=96)
    comments = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    locale = models.CharField(max_length=150)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_proposal'

class ConceptProposalTagMap(models.Model):
    concept_proposal = models.ForeignKey(ConceptProposal, related_name='+')
    concept_name_tag = models.ForeignKey(ConceptNameTag, related_name='+')
    class Meta:
        db_table = u'concept_proposal_tag_map'

class ConceptReferenceMap(models.Model):
    concept_map_id = models.IntegerField(primary_key=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    concept = models.ForeignKey(Concept, related_name='+')
    uuid = models.CharField(max_length=114, unique=True)
    concept_reference_term = models.ForeignKey('ConceptReferenceTerm', related_name='+')
    concept_map_type = models.ForeignKey(ConceptMapType, related_name='+')
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'concept_reference_map'

class ConceptReferenceSource(models.Model):
    concept_source_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    hl7_code = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_reference_source'

class ConceptReferenceTerm(models.Model):
    concept_reference_term_id = models.IntegerField(primary_key=True)
    concept_source = models.ForeignKey(ConceptReferenceSource, related_name='+')
    name = models.CharField(max_length=765, blank=True)
    code = models.CharField(max_length=765)
    version = models.CharField(max_length=765, blank=True)
    description = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    date_changed = models.DateTimeField(null=True, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_reference_term'

class ConceptReferenceTermMap(models.Model):
    concept_reference_term_map_id = models.IntegerField(primary_key=True)
    term_a = models.ForeignKey(ConceptReferenceTerm, related_name='+')
    term_b = models.ForeignKey(ConceptReferenceTerm, related_name='+')
    a_is_to_b = models.ForeignKey(ConceptMapType, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_reference_term_map'

class ConceptSet(models.Model):
    concept_set_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, related_name='+')
    concept_set = models.ForeignKey(Concept, db_column='concept_set', related_name='+')
    sort_weight = models.FloatField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_set'

class ConceptSetDerived(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_set = models.IntegerField(primary_key=True)
    sort_weight = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'concept_set_derived'

class ConceptStateConversion(models.Model):
    concept_state_conversion_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    program_workflow = models.ForeignKey('ProgramWorkflow', null=True, blank=True, related_name='+')
    program_workflow_state = models.ForeignKey('ProgramWorkflowState', null=True, blank=True, related_name='+')
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_state_conversion'

class ConceptStopWord(models.Model):
    concept_stop_word_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=150, unique=True)
    locale = models.CharField(max_length=60, unique=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'concept_stop_word'

class ConceptWord(models.Model):
    concept_word_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, related_name='+')
    word = models.CharField(max_length=150)
    locale = models.CharField(max_length=60)
    concept_name = models.ForeignKey(ConceptName, related_name='+')
    weight = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'concept_word'

class DataintegrityIntegrityChecks(models.Model):
    dataintegrity_integrity_check_id = models.IntegerField(primary_key=True)
    check_name = models.CharField(max_length=300)
    check_type = models.CharField(max_length=135)
    check_code = models.CharField(max_length=3000)
    check_result_type = models.CharField(max_length=135)
    check_fail = models.CharField(max_length=300)
    check_fail_operator = models.CharField(max_length=135)
    check_repair_type = models.CharField(max_length=135, blank=True)
    check_repair = models.CharField(max_length=3000, blank=True)
    check_parameters = models.CharField(max_length=1500, blank=True)
    class Meta:
        db_table = u'dataintegrity_integrity_checks'

class District(models.Model):
    district = models.CharField(max_length=765)
    province = models.CharField(max_length=765)
    class Meta:
        db_table = u'district'

class Drug(models.Model):
    drug_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, related_name='+')
    name = models.CharField(max_length=765, blank=True)
    combination = models.IntegerField()
    dosage_form = models.ForeignKey(Concept, null=True, db_column='dosage_form', blank=True, related_name='+')
    dose_strength = models.FloatField(null=True, blank=True)
    maximum_daily_dose = models.FloatField(null=True, blank=True)
    minimum_daily_dose = models.FloatField(null=True, blank=True)
    route = models.ForeignKey(Concept, null=True, db_column='route', blank=True, related_name='+')
    units = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    class Meta:
        db_table = u'drug'

class DrugIngredient(models.Model):
    concept = models.ForeignKey(Concept, related_name='+')
    ingredient = models.ForeignKey(Concept, primary_key=True, related_name='+')
    class Meta:
        db_table = u'drug_ingredient'

class DrugOrder(models.Model):
    order = models.ForeignKey('Orders', primary_key=True, related_name='+')
    drug_inventory = models.ForeignKey(Drug, null=True, blank=True, related_name='+')
    dose = models.FloatField(null=True, blank=True)
    equivalent_daily_dose = models.FloatField(null=True, blank=True)
    units = models.CharField(max_length=765, blank=True)
    frequency = models.CharField(max_length=765, blank=True)
    prn = models.IntegerField()
    complex = models.IntegerField()
    quantity = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'drug_order'

class Encounter(models.Model):
    encounter_id = models.IntegerField(primary_key=True)
    encounter_type = models.ForeignKey('EncounterType', db_column='encounter_type', related_name='+')
    patient = models.ForeignKey('Patient')
    location = models.ForeignKey('Location', null=True, blank=True, related_name='+')
    form = models.ForeignKey('Form', null=True, blank=True, related_name='+')
    encounter_datetime = models.DateTimeField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    # Maybe not in OpenMRS 1.8 visit = models.ForeignKey('Visit', null=True, blank=True, related_name='+')
    class Meta:
        db_table = u'encounter'

class EncounterProvider(models.Model):
    encounter_provider_id = models.IntegerField(primary_key=True)
    encounter = models.ForeignKey(Encounter, related_name='+')
    provider = models.ForeignKey('Provider', related_name='+')
    encounter_role = models.ForeignKey('EncounterRole', related_name='+')
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(null=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    date_voided = models.DateTimeField(null=True, blank=True)
    voided_by = models.IntegerField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'encounter_provider'

class EncounterRole(models.Model):
    encounter_role_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3072, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'encounter_role'

class EncounterType(models.Model):
    encounter_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'encounter_type'

class Field(models.Model):
    field_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    field_type = models.ForeignKey('FieldType', null=True, db_column='field_type', blank=True, related_name='+')
    concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    table_name = models.CharField(max_length=150, blank=True)
    attribute_name = models.CharField(max_length=150, blank=True)
    default_value = models.TextField(blank=True)
    select_multiple = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'field'

class FieldAnswer(models.Model):
    field = models.ForeignKey(Field, related_name='+')
    answer = models.ForeignKey(Concept, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'field_answer'

class FieldType(models.Model):
    field_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    description = models.TextField(blank=True)
    is_set = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'field_type'

class Form(models.Model):
    form_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    version = models.CharField(max_length=150)
    build = models.IntegerField(null=True, blank=True)
    published = models.IntegerField()
    description = models.TextField(blank=True)
    encounter_type = models.ForeignKey(EncounterType, null=True, db_column='encounter_type', blank=True, related_name='+')
    template = models.TextField(blank=True)
    xslt = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retired_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'form'

class FormField(models.Model):
    form_field_id = models.IntegerField(primary_key=True)
    form = models.ForeignKey(Form, related_name='+')
    field = models.ForeignKey(Field, related_name='+')
    field_number = models.IntegerField(null=True, blank=True)
    field_part = models.CharField(max_length=15, blank=True)
    page_number = models.IntegerField(null=True, blank=True)
    parent_form_field = models.ForeignKey('self', null=True, db_column='parent_form_field', blank=True, related_name='+')
    min_occurs = models.IntegerField(null=True, blank=True)
    max_occurs = models.IntegerField(null=True, blank=True)
    required = models.IntegerField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    sort_weight = models.FloatField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'form_field'

class FormResource(models.Model):
    form_resource_id = models.IntegerField(primary_key=True)
    form = models.ForeignKey(Form, unique=True, related_name='+')
    name = models.CharField(max_length=255, unique=True)
    value_reference = models.TextField()
    datatype = models.CharField(max_length=765, blank=True)
    datatype_config = models.TextField(blank=True)
    preferred_handler = models.CharField(max_length=765, blank=True)
    handler_config = models.TextField(blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'form_resource'

class FormentryArchive(models.Model):
    formentry_archive_id = models.IntegerField(primary_key=True)
    form_data = models.TextField()
    date_created = models.DateTimeField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    class Meta:
        db_table = u'formentry_archive'

class FormentryError(models.Model):
    formentry_error_id = models.IntegerField(primary_key=True)
    form_data = models.TextField()
    error = models.CharField(max_length=765)
    error_details = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    class Meta:
        db_table = u'formentry_error'

class FormentryQueue(models.Model):
    formentry_queue_id = models.IntegerField(primary_key=True)
    form_data = models.TextField()
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    class Meta:
        db_table = u'formentry_queue'

class FormentryXsn(models.Model):
    formentry_xsn_id = models.IntegerField(primary_key=True)
    form = models.ForeignKey(Form, related_name='+')
    xsn_data = models.TextField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    archived = models.IntegerField()
    archived_by = models.ForeignKey(Users, null=True, db_column='archived_by', blank=True, related_name='+')
    date_archived = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'formentry_xsn'

class GlobalProperty(models.Model):
    property = models.CharField(max_length=255, primary_key=True)
    property_value = models.TextField(blank=True)
    description = models.TextField(blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    datatype = models.CharField(max_length=765, blank=True)
    datatype_config = models.TextField(blank=True)
    preferred_handler = models.CharField(max_length=765, blank=True)
    handler_config = models.TextField(blank=True)
    class Meta:
        db_table = u'global_property'

class Hl7InArchive(models.Model):
    hl7_in_archive_id = models.IntegerField(primary_key=True)
    hl7_source = models.IntegerField()
    hl7_source_key = models.CharField(max_length=765, blank=True)
    hl7_data = models.TextField()
    date_created = models.DateTimeField()
    message_state = models.IntegerField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'hl7_in_archive'

class Hl7InError(models.Model):
    hl7_in_error_id = models.IntegerField(primary_key=True)
    hl7_source = models.IntegerField()
    hl7_source_key = models.TextField(blank=True)
    hl7_data = models.TextField()
    error = models.CharField(max_length=765)
    error_details = models.TextField(blank=True)
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'hl7_in_error'

class Hl7InQueue(models.Model):
    hl7_in_queue_id = models.IntegerField(primary_key=True)
    hl7_source = models.ForeignKey('Hl7Source', db_column='hl7_source', related_name='+')
    hl7_source_key = models.TextField(blank=True)
    hl7_data = models.TextField()
    message_state = models.IntegerField()
    date_processed = models.DateTimeField(null=True, blank=True)
    error_msg = models.TextField(blank=True)
    date_created = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'hl7_in_queue'

class Hl7Source(models.Model):
    hl7_source_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'hl7_source'

class HtmlformentryHtmlForm(models.Model):
    id = models.IntegerField(primary_key=True)
    form = models.ForeignKey(Form, null=True, blank=True, related_name='+')
    name = models.CharField(max_length=765, blank=True)
    xml_data = models.TextField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    uuid = models.CharField(max_length=114, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'htmlformentry_html_form'

class Liquibasechangelog(models.Model):
    id = models.CharField(max_length=189, primary_key=True, db_column='ID') # Field name made lowercase.
    author = models.CharField(max_length=189, primary_key=True, db_column='AUTHOR') # Field name made lowercase.
    filename = models.CharField(max_length=255, primary_key=True, db_column='FILENAME') # Field name made lowercase.
    dateexecuted = models.DateTimeField(db_column='DATEEXECUTED') # Field name made lowercase.
    md5sum = models.CharField(max_length=105, db_column='MD5SUM', blank=True) # Field name made lowercase.
    description = models.CharField(max_length=765, db_column='DESCRIPTION', blank=True) # Field name made lowercase.
    comments = models.CharField(max_length=765, db_column='COMMENTS', blank=True) # Field name made lowercase.
    tag = models.CharField(max_length=765, db_column='TAG', blank=True) # Field name made lowercase.
    liquibase = models.CharField(max_length=60, db_column='LIQUIBASE', blank=True) # Field name made lowercase.
    orderexecuted = models.IntegerField(db_column='ORDEREXECUTED') # Field name made lowercase.
    exectype = models.CharField(max_length=30, db_column='EXECTYPE') # Field name made lowercase.
    class Meta:
        db_table = u'liquibasechangelog'

class Liquibasechangeloglock(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    locked = models.IntegerField(db_column='LOCKED') # Field name made lowercase.
    lockgranted = models.DateTimeField(null=True, db_column='LOCKGRANTED', blank=True) # Field name made lowercase.
    lockedby = models.CharField(max_length=765, db_column='LOCKEDBY', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'liquibasechangeloglock'

class Location(models.Model):
    location_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765, blank=True)
    address1 = models.CharField(max_length=765, blank=True)
    address2 = models.CharField(max_length=765, blank=True)
    city_village = models.CharField(max_length=765, blank=True)
    state_province = models.CharField(max_length=765, blank=True)
    postal_code = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    latitude = models.CharField(max_length=150, blank=True)
    longitude = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    county_district = models.CharField(max_length=765, blank=True)
    address3 = models.CharField(max_length=765, blank=True)
    address6 = models.CharField(max_length=765, blank=True)
    address5 = models.CharField(max_length=765, blank=True)
    address4 = models.CharField(max_length=765, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    parent_location = models.ForeignKey('self', null=True, db_column='parent_location', blank=True, related_name='+')
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'location'

class LocationAttribute(models.Model):
    location_attribute_id = models.IntegerField(primary_key=True)
    location = models.ForeignKey(Location, related_name='+')
    attribute_type = models.ForeignKey('LocationAttributeType', related_name='+')
    value_reference = models.TextField()
    uuid = models.CharField(max_length=114, unique=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'location_attribute'

class LocationAttributeType(models.Model):
    location_attribute_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3072, blank=True)
    datatype = models.CharField(max_length=765, blank=True)
    datatype_config = models.TextField(blank=True)
    preferred_handler = models.CharField(max_length=765, blank=True)
    handler_config = models.TextField(blank=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'location_attribute_type'

class LocationTag(models.Model):
    location_tag_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'location_tag'

class LocationTagMap(models.Model):
    location = models.ForeignKey(Location, primary_key=True, related_name='+')
    location_tag = models.ForeignKey(LocationTag, related_name='+')
    class Meta:
        db_table = u'location_tag_map'

class LogicRuleDefinition(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=3000, blank=True)
    rule_content = models.CharField(max_length=6144)
    language = models.CharField(max_length=765)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'logic_rule_definition'

class LogicRuleToken(models.Model):
    logic_rule_token_id = models.IntegerField(primary_key=True)
    creator = models.ForeignKey(Person, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Person, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=1536)
    class_name = models.CharField(max_length=1536)
    state = models.CharField(max_length=1536, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'logic_rule_token'

class LogicRuleTokenTag(models.Model):
    logic_rule_token = models.ForeignKey(LogicRuleToken, related_name='+')
    tag = models.CharField(max_length=1536)
    class Meta:
        db_table = u'logic_rule_token_tag'

class LogicTokenRegistration(models.Model):
    token_registration_id = models.IntegerField(primary_key=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    token = models.CharField(max_length=1536)
    provider_class_name = models.CharField(max_length=1536)
    provider_token = models.CharField(max_length=1536)
    configuration = models.CharField(max_length=6000, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'logic_token_registration'

class LogicTokenRegistrationTag(models.Model):
    token_registration = models.ForeignKey(LogicTokenRegistration, related_name='+')
    tag = models.CharField(max_length=1536)
    class Meta:
        db_table = u'logic_token_registration_tag'

class MetadatasharingExportedPackage(models.Model):
    exported_package_id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    date_created = models.DateTimeField()
    name = models.CharField(max_length=192)
    description = models.CharField(max_length=768)
    group_uuid = models.CharField(max_length=114)
    version = models.IntegerField()
    content = models.TextField(blank=True)
    published = models.IntegerField()
    class Meta:
        db_table = u'metadatasharing_exported_package'

class MetadatasharingImportedItem(models.Model):
    imported_item_id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    classname = models.CharField(max_length=768)
    last_date_imported = models.DateTimeField(null=True, blank=True)
    existing_uuid = models.CharField(max_length=114, blank=True)
    import_type = models.IntegerField(null=True, blank=True)
    last_date_changed = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'metadatasharing_imported_item'

class MetadatasharingImportedPackage(models.Model):
    imported_package_id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    date_created = models.DateTimeField()
    date_imported = models.DateTimeField()
    name = models.CharField(max_length=192)
    description = models.CharField(max_length=768)
    group_uuid = models.CharField(max_length=114)
    version = models.IntegerField()
    class Meta:
        db_table = u'metadatasharing_imported_package'

class MetadatasharingSubscription(models.Model):
    subscription_id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    url = models.CharField(max_length=1536)
    status = models.IntegerField()
    name = models.CharField(max_length=192, blank=True)
    remote_package_version = models.IntegerField(null=True, blank=True)
    local_package_version = models.IntegerField(null=True, blank=True)
    group_uuid = models.CharField(max_length=114, unique=True, blank=True)
    class Meta:
        db_table = u'metadatasharing_subscription'

class Note(models.Model):
    note_id = models.IntegerField(primary_key=True)
    note_type = models.CharField(max_length=150, blank=True)
    patient = models.ForeignKey('Patient', null=True, blank=True, related_name='+')
    obs = models.ForeignKey('Obs', null=True, blank=True, related_name='+')
    encounter = models.ForeignKey(Encounter, null=True, blank=True, related_name='+')
    text = models.TextField()
    priority = models.IntegerField(null=True, blank=True)
    parent = models.ForeignKey('self', null=True, db_column='parent', blank=True, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'note'

class NotificationAlert(models.Model):
    alert_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=1536)
    satisfied_by_any = models.IntegerField()
    alert_read = models.IntegerField()
    date_to_expire = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'notification_alert'

class NotificationAlertRecipient(models.Model):
    alert = models.ForeignKey(NotificationAlert, related_name='+')
    user = models.ForeignKey(Users, related_name='+')
    alert_read = models.IntegerField()
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'notification_alert_recipient'

class NotificationTemplate(models.Model):
    template_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150, blank=True)
    template = models.TextField(blank=True)
    subject = models.CharField(max_length=300, blank=True)
    sender = models.CharField(max_length=765, blank=True)
    recipients = models.CharField(max_length=1536, blank=True)
    ordinal = models.IntegerField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'notification_template'

class Obs(models.Model):
    obs_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, related_name='+')
    concept = models.ForeignKey(Concept, related_name="concepts", to_field='concept_id') #, to_field="concept_id")
    encounter = models.ForeignKey(Encounter, null=True, blank=True) # , related_name='+')
    order = models.ForeignKey('Orders', null=True, blank=True, related_name='+')
    obs_datetime = models.DateTimeField()
    location = models.ForeignKey(Location, null=True, blank=True, related_name='+')
    obs_group = models.ForeignKey('self', null=True, blank=True, related_name='+')
    accession_number = models.CharField(max_length=765, blank=True)
    value_group_id = models.IntegerField(null=True, blank=True)
    value_boolean = models.IntegerField(null=True, blank=True)
    value_coded = models.ForeignKey(Concept, null=True, db_column='value_coded', blank=True, related_name='+')
    value_coded_name = models.ForeignKey(ConceptName, null=True, blank=True, related_name='+')
    value_drug = models.ForeignKey(Drug, null=True, db_column='value_drug', blank=True, related_name='+')
    value_datetime = models.DateTimeField(null=True, blank=True)
    value_numeric = models.FloatField(null=True, blank=True)
    value_modifier = models.CharField(max_length=6, blank=True)
    value_text = models.TextField(blank=True)
    comments = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    value_complex = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    # May not be in 1.8 previous_version = models.ForeignKey('self', null=True, db_column='previous_version', blank=True, related_name='+')
    class Meta:
        db_table = u'obs'

class OccConcept(models.Model):
    occ_concept_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, unique=True, related_name='+')
    original_occ_concept_uuid = models.CharField(max_length=114, unique=True)
    source_hl7_code = models.CharField(max_length=150)
    date_created = models.DateTimeField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'occ_concept'

class OrderType(models.Model):
    order_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=765)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'order_type'

class Orders(models.Model):
    order_id = models.IntegerField(primary_key=True)
    order_type = models.ForeignKey(OrderType, related_name='+')
    concept_id = models.IntegerField()
    orderer = models.ForeignKey(Users, null=True, db_column='orderer', blank=True, related_name='+')
    encounter = models.ForeignKey(Encounter, null=True, blank=True, related_name='+')
    instructions = models.TextField(blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    auto_expire_date = models.DateTimeField(null=True, blank=True)
    discontinued = models.IntegerField()
    discontinued_date = models.DateTimeField(null=True, blank=True)
    discontinued_by = models.ForeignKey(Users, null=True, db_column='discontinued_by', blank=True, related_name='+')
    discontinued_reason = models.ForeignKey(Concept, null=True, db_column='discontinued_reason', blank=True, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    patient = models.ForeignKey('Patient', related_name='+')
    accession_number = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    discontinued_reason_non_coded = models.CharField(max_length=765, blank=True)
    urgency = models.CharField(max_length=150)
    class Meta:
        db_table = u'orders'

class Patient(models.Model):
    patient = models.ForeignKey(Person, primary_key=True)
    # maybe new in 1.8 tribe = models.ForeignKey('Tribe', null=True, db_column='tribe', blank=True, related_name='+')
    # Adding so we don't have to fetch the entire patient and person to get their ID
    #patient_id = models.IntegerField(db_column='patient_id')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'patient'

class PatientIdentifier(models.Model):
    patient_identifier_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient) #, related_name='+')
    identifier = models.CharField(max_length=150)
    identifier_type = models.ForeignKey('PatientIdentifierType', db_column='identifier_type')
    preferred = models.IntegerField()
    location = models.ForeignKey(Location, null=True, blank=True, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    # Maybe not in 1.8? date_changed = models.DateTimeField(null=True, blank=True)
    # Maybe not in 1.8? changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    class Meta:
        db_table = u'patient_identifier'

class PatientIdentifierType(models.Model):
    patient_identifier_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    format = models.CharField(max_length=765, blank=True)
    check_digit = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    required = models.IntegerField()
    format_description = models.CharField(max_length=765, blank=True)
    validator = models.CharField(max_length=600, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    # Maybe not in 1.8? location_behavior = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'patient_identifier_type'

class PatientProgram(models.Model):
    patient_program_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='+')
    program = models.ForeignKey('Program', related_name='+')
    date_enrolled = models.DateTimeField(null=True, blank=True)
    date_completed = models.DateTimeField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    location = models.ForeignKey(Location, null=True, blank=True, related_name='+')
    outcome_concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    class Meta:
        db_table = u'patient_program'

class PatientState(models.Model):
    patient_state_id = models.IntegerField(primary_key=True)
    patient_program = models.ForeignKey(PatientProgram, related_name='+')
    state = models.ForeignKey('ProgramWorkflowState', db_column='state', related_name='+')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'patient_state'

class PatientflagsDisplaypoint(models.Model):
    displaypoint_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(null=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(null=True, blank=True)
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'patientflags_displaypoint'

class PatientflagsFlag(models.Model):
    flag_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    criteria = models.CharField(max_length=15000)
    message = models.CharField(max_length=765)
    enabled = models.IntegerField()
    evaluator = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(null=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(null=True, blank=True)
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    priority_id = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'patientflags_flag'

class PatientflagsFlagTag(models.Model):
    flag = models.ForeignKey(PatientflagsFlag, related_name='+')
    tag = models.ForeignKey('PatientflagsTag', related_name='+')
    class Meta:
        db_table = u'patientflags_flag_tag'

class PatientflagsPriority(models.Model):
    priority_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    style = models.CharField(max_length=765)
    rank = models.IntegerField()
    description = models.CharField(max_length=3000, blank=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(null=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(null=True, blank=True)
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'patientflags_priority'

class PatientflagsTag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    description = models.CharField(max_length=3000, blank=True)
    creator = models.IntegerField()
    date_created = models.DateTimeField()
    changed_by = models.IntegerField(null=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.IntegerField(null=True, blank=True)
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'patientflags_tag'

class PatientflagsTagDisplaypoint(models.Model):
    tag = models.ForeignKey(PatientflagsTag, related_name='+')
    displaypoint = models.ForeignKey(PatientflagsDisplaypoint, related_name='+')
    class Meta:
        db_table = u'patientflags_tag_displaypoint'

class PatientflagsTagRole(models.Model):
    tag = models.ForeignKey(PatientflagsTag, related_name='+')
    role = models.ForeignKey('Role', db_column='role', related_name='+')
    class Meta:
        db_table = u'patientflags_tag_role'

class PersonAddress(models.Model):
    person_address_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, null=True, blank=True, related_name='+')
    preferred = models.IntegerField()
    address1 = models.CharField(max_length=765, blank=True)
    address2 = models.CharField(max_length=765, blank=True)
    city_village = models.CharField(max_length=765, blank=True)
    state_province = models.CharField(max_length=765, blank=True)
    postal_code = models.CharField(max_length=150, blank=True)
    country = models.CharField(max_length=150, blank=True)
    latitude = models.CharField(max_length=150, blank=True)
    longitude = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    county_district = models.CharField(max_length=765, blank=True)
    address3 = models.CharField(max_length=765, blank=True)
    address6 = models.CharField(max_length=765, blank=True)
    address5 = models.CharField(max_length=765, blank=True)
    address4 = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'person_address'

class PersonAttribute(models.Model):
    person_attribute_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, related_name='+')
    value = models.CharField(max_length=150)
    person_attribute_type = models.ForeignKey('PersonAttributeType', related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'person_attribute'

class PersonAttributeType(models.Model):
    person_attribute_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField()
    format = models.CharField(max_length=150, blank=True)
    foreign_key = models.IntegerField(null=True, blank=True)
    searchable = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    edit_privilege = models.ForeignKey('Privilege', null=True, db_column='edit_privilege', blank=True, related_name='+')
    uuid = models.CharField(max_length=114, unique=True)
    sort_weight = models.FloatField(null=True, blank=True)
    class Meta:
        db_table = u'person_attribute_type'

class PersonMergeLog(models.Model):
    person_merge_log_id = models.IntegerField(primary_key=True)
    winner_person = models.ForeignKey(Person, related_name='+')
    loser_person = models.ForeignKey(Person, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    merged_data = models.TextField()
    uuid = models.CharField(max_length=114, unique=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'person_merge_log'

class PersonName(models.Model):
    person_name_id = models.IntegerField(primary_key=True)
    preferred = models.IntegerField()
    person = models.ForeignKey(Person, related_name='+')
    prefix = models.CharField(max_length=150, blank=True)
    given_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=150, blank=True)
    family_name_prefix = models.CharField(max_length=150, blank=True)
    family_name = models.CharField(max_length=150, blank=True)
    family_name2 = models.CharField(max_length=150, blank=True)
    family_name_suffix = models.CharField(max_length=150, blank=True)
    degree = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    changed_by = models.IntegerField(null=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'person_name'

class Privilege(models.Model):
    privilege = models.CharField(max_length=150, primary_key=True)
    description = models.CharField(max_length=750)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'privilege'

class Program(models.Model):
    program_id = models.IntegerField(primary_key=True)
    concept = models.ForeignKey(Concept, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1500, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    outcomes_concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    class Meta:
        db_table = u'program'

class ProgramWorkflow(models.Model):
    program_workflow_id = models.IntegerField(primary_key=True)
    program = models.ForeignKey(Program, related_name='+')
    concept = models.ForeignKey(Concept, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'program_workflow'

class ProgramWorkflowState(models.Model):
    program_workflow_state_id = models.IntegerField(primary_key=True)
    program_workflow = models.ForeignKey(ProgramWorkflow, related_name='+')
    concept = models.ForeignKey(Concept, related_name='+')
    initial = models.IntegerField()
    terminal = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    retired = models.IntegerField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'program_workflow_state'

class Provider(models.Model):
    provider_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, null=True, blank=True, related_name='+')
    name = models.CharField(max_length=765, blank=True)
    identifier = models.CharField(max_length=765, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'provider'

class ProviderAttribute(models.Model):
    provider_attribute_id = models.IntegerField(primary_key=True)
    provider = models.ForeignKey(Provider, related_name='+')
    attribute_type = models.ForeignKey('ProviderAttributeType', related_name='+')
    value_reference = models.TextField()
    uuid = models.CharField(max_length=114, unique=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'provider_attribute'

class ProviderAttributeType(models.Model):
    provider_attribute_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3072, blank=True)
    datatype = models.CharField(max_length=765, blank=True)
    datatype_config = models.TextField(blank=True)
    preferred_handler = models.CharField(max_length=765, blank=True)
    handler_config = models.TextField(blank=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'provider_attribute_type'

class Province(models.Model):
    code = models.CharField(max_length=765)
    province = models.CharField(max_length=765)
    class Meta:
        db_table = u'province'

class Relationship(models.Model):
    relationship_id = models.IntegerField(primary_key=True)
    person_a = models.ForeignKey(Person, db_column='person_a', related_name='+')
    relationship = models.ForeignKey('RelationshipType', db_column='relationship', related_name='+')
    person_b = models.ForeignKey(Person, db_column='person_b', related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True, blank=True)
    date_changed = models.DateTimeField(null=True, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'relationship'

class RelationshipType(models.Model):
    relationship_type_id = models.IntegerField(primary_key=True)
    a_is_to_b = models.CharField(max_length=150)
    b_is_to_a = models.CharField(max_length=150)
    preferred = models.IntegerField()
    weight = models.IntegerField()
    description = models.CharField(max_length=765)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    uuid = models.CharField(max_length=114, unique=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'relationship_type'

class ReportObject(models.Model):
    report_object_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    report_object_type = models.CharField(max_length=765)
    report_object_sub_type = models.CharField(max_length=765)
    xml_data = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'report_object'

class ReportSchemaXml(models.Model):
    report_schema_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.TextField()
    xml_data = models.TextField()
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'report_schema_xml'

class ReportingReportDesign(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    report_definition = models.ForeignKey('SerializedObject', related_name='+')
    renderer_type = models.CharField(max_length=765)
    properties = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'reporting_report_design'

class ReportingReportDesignResource(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    report_design = models.ForeignKey(ReportingReportDesign, related_name='+')
    content_type = models.CharField(max_length=150, blank=True)
    extension = models.CharField(max_length=60, blank=True)
    contents = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'reporting_report_design_resource'

class ReportingReportProcessor(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3000, blank=True)
    processor_type = models.CharField(max_length=765)
    configuration = models.TextField(blank=True)
    run_on_success = models.IntegerField()
    run_on_error = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    report_design = models.ForeignKey(ReportingReportDesign, null=True, blank=True, related_name='+')
    processor_mode = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'reporting_report_processor'

class ReportingReportRequest(models.Model):
    id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=114)
    base_cohort_uuid = models.CharField(max_length=114, blank=True)
    base_cohort_parameters = models.TextField(blank=True)
    report_definition_uuid = models.CharField(max_length=114)
    report_definition_parameters = models.TextField(blank=True)
    renderer_type = models.CharField(max_length=765)
    renderer_argument = models.CharField(max_length=765, blank=True)
    requested_by = models.ForeignKey(Users, db_column='requested_by', related_name='+')
    request_datetime = models.DateTimeField()
    priority = models.CharField(max_length=765)
    status = models.CharField(max_length=765)
    evaluation_start_datetime = models.DateTimeField(null=True, blank=True)
    evaluation_complete_datetime = models.DateTimeField(null=True, blank=True)
    render_complete_datetime = models.DateTimeField(null=True, blank=True)
    description = models.CharField(max_length=3000, blank=True)
    schedule = models.CharField(max_length=300, blank=True)
    process_automatically = models.IntegerField()
    class Meta:
        db_table = u'reporting_report_request'

class Role(models.Model):
    role = models.CharField(max_length=150, primary_key=True)
    description = models.CharField(max_length=765)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'role'

class RolePrivilege(models.Model):
    role = models.ForeignKey(Role, db_column='role', related_name='+')
    privilege = models.ForeignKey(Privilege, primary_key=True, db_column='privilege', related_name='+')
    class Meta:
        db_table = u'role_privilege'

class RoleRole(models.Model):
    parent_role = models.ForeignKey(Role, primary_key=True, db_column='parent_role', related_name='+')
    child_role = models.ForeignKey(Role, db_column='child_role', related_name='+')
    class Meta:
        db_table = u'role_role'

class RoomTemperature(models.Model):
    room_temperature_id = models.IntegerField(primary_key=True)
    time = models.DateTimeField()
    temp = models.IntegerField()
    uuid = models.CharField(max_length=114)
    class Meta:
        db_table = u'room_temperature'

class SchedulerTaskConfig(models.Model):
    task_config_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3072, blank=True)
    schedulable_class = models.TextField(blank=True)
    start_time = models.DateTimeField(null=True, blank=True)
    start_time_pattern = models.CharField(max_length=150, blank=True)
    repeat_interval = models.IntegerField()
    start_on_startup = models.IntegerField()
    started = models.IntegerField()
    created_by = models.ForeignKey(Users, null=True, db_column='created_by', blank=True, related_name='+')
    date_created = models.DateTimeField(null=True, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    last_execution_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        db_table = u'scheduler_task_config'

class SchedulerTaskConfigProperty(models.Model):
    task_config_property_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    value = models.TextField(blank=True)
    task_config = models.ForeignKey(SchedulerTaskConfig, null=True, blank=True, related_name='+')
    class Meta:
        db_table = u'scheduler_task_config_property'

class SerializedObject(models.Model):
    serialized_object_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=15000, blank=True)
    type = models.CharField(max_length=765)
    subtype = models.CharField(max_length=765)
    serialization_class = models.CharField(max_length=765)
    serialized_data = models.TextField()
    date_created = models.DateTimeField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    retired = models.IntegerField()
    date_retired = models.DateTimeField(null=True, blank=True)
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    retire_reason = models.CharField(max_length=3000, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'serialized_object'

class SmartcontainerActivity(models.Model):
    smartcontainer_activity_id = models.IntegerField(primary_key=True)
    activity_name = models.CharField(max_length=765, blank=True)
    activity_url = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'smartcontainer_activity'

class SmartcontainerApp(models.Model):
    smartcontainer_app_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765, blank=True)
    description = models.TextField(blank=True)
    author = models.CharField(max_length=765, blank=True)
    mode = models.CharField(max_length=765, blank=True)
    version = models.CharField(max_length=765, blank=True)
    base_url = models.CharField(max_length=765, blank=True)
    icon = models.CharField(max_length=765, blank=True)
    smart_id = models.CharField(max_length=765, blank=True)
    default_app = models.IntegerField(null=True, blank=True)
    manifest = models.TextField(blank=True)
    activity = models.ForeignKey(SmartcontainerActivity, null=True, blank=True, related_name='+')
    webhook = models.ForeignKey('SmartcontainerWebhook', null=True, blank=True, related_name='+')
    retire = models.IntegerField()
    class Meta:
        db_table = u'smartcontainer_app'

class SmartcontainerUser(models.Model):
    smartcontainer_user_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(Users, related_name='+')
    class Meta:
        db_table = u'smartcontainer_user'

class SmartcontainerUserHiddenApp(models.Model):
    smartcontainer_user = models.ForeignKey(SmartcontainerUser, related_name='+')
    smartcontainer_app = models.ForeignKey(SmartcontainerApp, primary_key=True, related_name='+')
    class Meta:
        db_table = u'smartcontainer_user_hidden_app'

class SmartcontainerWebhook(models.Model):
    smartcontainer_webhook_id = models.IntegerField(primary_key=True)
    webhook_name = models.CharField(max_length=765, blank=True)
    webhook_url = models.CharField(max_length=765, blank=True)
    webhook_description = models.TextField(blank=True)
    class Meta:
        db_table = u'smartcontainer_webhook'

class SyncClass(models.Model):
    class_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    default_send_to = models.IntegerField()
    default_receive_from = models.IntegerField()
    class Meta:
        db_table = u'sync_class'

class SyncImport(models.Model):
    sync_import_id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=108)
    creator = models.CharField(max_length=108, blank=True)
    database_version = models.CharField(max_length=60, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    retry_count = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=96, blank=True)
    payload = models.TextField(blank=True)
    error_message = models.CharField(max_length=765, blank=True)
    source_server = models.ForeignKey('SyncServer', null=True, blank=True, related_name='+')
    class Meta:
        db_table = u'sync_import'

class SyncRecord(models.Model):
    record_id = models.IntegerField(primary_key=True)
    uuid = models.CharField(max_length=108, unique=True)
    creator = models.CharField(max_length=108, blank=True)
    database_version = models.CharField(max_length=60, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    retry_count = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=96, blank=True)
    payload = models.TextField(blank=True)
    contained_classes = models.CharField(max_length=3000, blank=True)
    original_uuid = models.CharField(max_length=108)
    class Meta:
        db_table = u'sync_record'

class SyncServer(models.Model):
    server_id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=765, blank=True)
    address = models.CharField(max_length=765)
    server_type = models.CharField(max_length=60)
    username = models.CharField(max_length=765, blank=True)
    password = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=108, blank=True)
    last_sync = models.DateTimeField(null=True, blank=True)
    last_sync_state = models.CharField(max_length=150, blank=True)
    disabled = models.IntegerField()
    child_username = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'sync_server'

class SyncServerClass(models.Model):
    server_class_id = models.IntegerField(primary_key=True)
    class_field = models.ForeignKey(SyncClass, db_column="class_id", related_name='+') # Field renamed because it was a Python reserved word. SWG Fixed
    server = models.ForeignKey(SyncServer, related_name='+')
    send_to = models.IntegerField()
    receive_from = models.IntegerField()
    class Meta:
        db_table = u'sync_server_class'

class SyncServerRecord(models.Model):
    server_record_id = models.IntegerField(primary_key=True)
    server = models.ForeignKey(SyncServer, related_name='+')
    record = models.ForeignKey(SyncRecord, related_name='+')
    state = models.CharField(max_length=96, blank=True)
    retry_count = models.IntegerField(null=True, blank=True)
    error_message = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'sync_server_record'

class TestOrder(models.Model):
    order = models.ForeignKey(Orders, primary_key=True, related_name='+')
    specimen_source = models.ForeignKey(Concept, null=True, db_column='specimen_source', blank=True, related_name='+')
    laterality = models.CharField(max_length=60, blank=True)
    clinical_history = models.TextField(blank=True)
    class Meta:
        db_table = u'test_order'

class Tribe(models.Model):
    tribe_id = models.IntegerField(primary_key=True)
    retired = models.IntegerField()
    name = models.CharField(max_length=150)
    class Meta:
        db_table = u'tribe'

class UserProperty(models.Model):
    user = models.ForeignKey(Users, primary_key=True, related_name='+')
    property = models.CharField(max_length=255, primary_key=True)
    property_value = models.CharField(max_length=765)
    class Meta:
        db_table = u'user_property'

class UserRole(models.Model):
    user = models.ForeignKey(Users, related_name='+')
    role = models.ForeignKey(Role, primary_key=True, db_column='role', related_name='+')
    class Meta:
        db_table = u'user_role'

class Visit(models.Model):
    visit_id = models.IntegerField(primary_key=True)
    patient = models.ForeignKey(Patient, related_name='+')
    visit_type = models.ForeignKey('VisitType', related_name='+')
    date_started = models.DateTimeField()
    date_stopped = models.DateTimeField(null=True, blank=True)
    indication_concept = models.ForeignKey(Concept, null=True, blank=True, related_name='+')
    location = models.ForeignKey(Location, null=True, blank=True, related_name='+')
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'visit'

class VisitAttribute(models.Model):
    visit_attribute_id = models.IntegerField(primary_key=True)
    visit = models.ForeignKey(Visit, related_name='+')
    attribute_type = models.ForeignKey('VisitAttributeType', related_name='+')

    uuid = models.CharField(max_length=114, unique=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'visit_attribute'

class VisitAttributeType(models.Model):
    visit_attribute_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3072, blank=True)
    datatype = models.CharField(max_length=765, blank=True)
    datatype_config = models.TextField(blank=True)
    preferred_handler = models.CharField(max_length=765, blank=True)
    handler_config = models.TextField(blank=True)
    min_occurs = models.IntegerField()
    max_occurs = models.IntegerField(null=True, blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    class Meta:
        db_table = u'visit_attribute_type'

class VisitType(models.Model):
    visit_type_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    description = models.CharField(max_length=3072, blank=True)
    uuid = models.CharField(max_length=114, unique=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    retired = models.IntegerField()
    retired_by = models.ForeignKey(Users, null=True, db_column='retired_by', blank=True, related_name='+')
    date_retired = models.DateTimeField(null=True, blank=True)
    retire_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'visit_type'

class XformsMedicalHistoryField(models.Model):
    field_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=765)
    tabindex = models.IntegerField(null=True, db_column='tabIndex', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'xforms_medical_history_field'

class XformsPersonRepeatAttribute(models.Model):
    person_repeat_attribute_id = models.IntegerField(primary_key=True)
    person = models.ForeignKey(Person, related_name='+')
    value = models.CharField(max_length=150)
    person_attribute_type = models.ForeignKey(PersonAttributeType, related_name='+')
    value_id = models.IntegerField()
    value_id_type = models.IntegerField()
    value_display_order = models.IntegerField()
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    voided = models.IntegerField()
    voided_by = models.ForeignKey(Users, null=True, db_column='voided_by', blank=True, related_name='+')
    date_voided = models.DateTimeField(null=True, blank=True)
    void_reason = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'xforms_person_repeat_attribute'

class XformsXform(models.Model):
    form_id = models.IntegerField()
    xform_xml = models.TextField(blank=True)
    layout_xml = models.TextField(blank=True)
    creator = models.ForeignKey(Users, db_column='creator', related_name='+')
    date_created = models.DateTimeField()
    changed_by = models.ForeignKey(Users, null=True, db_column='changed_by', blank=True, related_name='+')
    date_changed = models.DateTimeField(null=True, blank=True)
    locale_xml = models.TextField(blank=True)
    javascript_src = models.TextField(blank=True)
    uuid = models.CharField(max_length=114, blank=True)
    class Meta:
        db_table = u'xforms_xform'

