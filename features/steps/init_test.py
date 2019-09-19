from behave import given, when, then #pylint: disable=no-name-in-module
from koffie2 import Cup

@given(u'we want to create a cup of {smaaknummer:d}')
def test_smaaknummer(context, smaaknummer):
    context.cup = Cup(smaaknummer)

@when(u'we create that cup')
def test_create(context):
    pass

@then(u'it should contain {smaak:w}')
def test_smaak(context, smaak):
    assert context.cup.smaak == smaak