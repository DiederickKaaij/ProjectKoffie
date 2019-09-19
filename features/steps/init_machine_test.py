from behave import given, when, then #pylint: disable=no-name-in-module
from koffie2 import KoffieAutomaat

@given(u'we want to start a {merk:w} machine')
def test_merk(context, merk):
    context.merk = merk

@given(u'it should have {amount:d} cups')
def test_amount(context, amount):
    context.amount = amount

@when(u'we start the machine')
def test_start(context):
    context.automaat = KoffieAutomaat(context.merk, context.amount)

@then(u'it should be a {merk:w}')
def test_merk2(context, merk):
    assert context.automaat.merk == merk

@then(u'it should have the cups {presentCups:w}')
def test_cups(context, presentCups):
    lijst = ""
    for i in range(0, len(context.automaat.cups)):
        lijst += context.automaat.cups[i].smaak
        i += 1
    assert lijst == presentCups