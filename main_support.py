import pyxb
from xsd import pain_cutted as pain
from datetime import datetime
import pyxb.utils.domutils
import xml.dom.minidom

import pyxb.binding.datatypes as xs

# def int_to_decimal_str(integer):
#         '''
#         Helper to convert integers (representing cents) into decimal currency
#         string. WARNING: DO NOT TRY TO DO THIS BY DIVISION, FLOATING POINT
#         ERRORS ARE NO FUN IN FINANCIAL SYSTEMS.
#         @param integer The amount in cents
#         @return string The amount in currency with full stop decimal separator
#         '''
#         int_string = str(integer)
#         if len(int_string) < 2:
#             return "0." + int_string.zfill(2)
#         else:
#             return int_string[:-2] + "." + int_string[-2:]
#
# print int_to_decimal_str(1)

grpHdr = pain.GroupHeader32_CH()
grpHdr.MsgId = "MSG-01"
grpHdr.NbOfTxs = "123456789012345"
grpHdr.CreDtTm = datetime.strptime("2010-02-15T07:30:00", '%Y-%m-%dT%H:%M:%S')
grpHdr.CtrlSum = "123.3333334"

pmtinf = pain.PaymentInstructionInformation3_CH()
pmtinf.PmtInfId = "PayID"
pmtinf.PmtMtd = "PayMethod"
pmtinf.ReqdExctnDt = datetime.strptime("2016-03-23", '%Y-%m-%d')
pmtinf.Dbtr = "PayDbtr"
pmtinf.DbtrAcct = "PayAccount"
pmtinf.DbtrAgt = "PayDbtrAgent"
pmtinf.CdtTrfTxInf = ['Dupa', 'Sraka']

# the default value for minOccurs is 1 -> http://www.w3schools.com/xml/schema_complex_indicators.asp


### OrgId ###

_orgidVal = pain.OrganisationIdentification4_CH(BICOrBEI="KBBECH22", Othr="SomeOherValue") # dziala to
# _orgidVal = pain.OrganisationIdentification4_CH()     # takie
# _orgidVal.BICOrBEI = "KBBECH22321"                    # tez
# _orgidVal.Othr = "SomeOherValue"                      # dziala

_orgid = pain.Party6Choice_CH(_orgidVal)      # OrgID

### PrvtId ###

_prvtidVal = pain.PersonIdentification5_CH()  # PrvtId
_prvtidVal.Othr = "wojtek"
_prvtidVal.DtAndPlcOfBirth = pain.DateAndPlaceOfBirth(BirthDt="2016-03-30",
                                                      PrvcOfBirth=None,       # optional
                                                      CityOfBirth="Stalowka",
                                                      CtryOfBirth="CH")

_prvtid = pain.Party6Choice_CH(_prvtidVal)  # super wazne! dodajesz do Id wiec musi to byc insancja klasy podrzednej!


# grpHdr.InitgPty = pain.PartyIdentification32_CH_NameAndId(Nm='nazwa', Id=_orgid)
grpHdr.InitgPty = pain.PartyIdentification32_CH_NameAndId(Nm='nazwa', Id=_prvtid)  # wejdzie ostatni jesli w sekwencji

# albo i tak
# grpHdr.InitgPty = pain.PartyIdentification32_CH_NameAndId(Nm='nazwa', Id=pain.Party6Choice_CH(pain.OrganisationIdentification4_CH('org_bo_nie_BIC')))


# whaaat? sprawdz to
# grpHdr.InitgPty = pain.PartyIdentification32_CH_NameAndId(Nm='nazwa', Id=pain.Party6Choice_CH(pain.PersonIdentification5_CH('other_bo_nie_date')))

# or
# grpHdr.InitgPty = pyxb.BIND('name', pyxb.BIND());
# grpHdr.InitgPty.Id = pyxb.BIND();
# grpHdr.InitgPty.Id.OrgId = 'org';

pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace("http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd")
# pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace("urn:iso:std:iso:20022:tech:xsd:pain.001.003.03")

# pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(xs.Namespace)
# pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(pain.Namespace)

# ns2 = pyxb.namespace.NamespaceForURI('urn:iso:std:iso:20022:tech:xsd:pain.001.003.03')



# print "CdtTrfTxInf list? :", type(pmtinf.CdtTrfTxInf)
cstmrCdT = pain.CustomerCreditTransferInitiationV03_CH()    # CstmrCdtTrfInitn TAG
cstmrCdT.GrpHdr = grpHdr

# PmtInf is a multi-valued element so it's a list: append the new value
print "type(cstmrCdT): ", type(cstmrCdT)
print "type(cstmrCdT.PmtInf): ", type(cstmrCdT.PmtInf)
cstmrCdT.PmtInf.append(pmtinf)

doc = pain.Document()
doc.CstmrCdtTrfInitn = cstmrCdT


xxx = doc.toDOM()
domobj = xml.dom.minidom.Document()

print "xxx   ", xxx.__class__
print "domobj", domobj.__class__
# TODO: dlaczego nie rozwia mi nazw xxx.CokoLwiek ? Pycharm nie widzi xxx jako obiektu klasy minidom.Document hmmm
# TODO: read http://www.boddie.org.uk/python/XML_intro.html

# pyxb.utils.domutils.BindingDOMSupport.addXMLNSDeclaration(element='Document', namespace=ns2)

# xxx.setAttribute("xmlns", "http://example.net/ns")
# pyxb.utils.domutils.BindingDOMSupport.DeclareNamespace(pain.Namespace, 'xxx')

print xxx.toprettyxml(encoding='utf-8')

try:
    doc.validateBinding()
    # print doc.toDOM().toprettyxml(encoding='utf-8')
except pyxb.ValidationError as e:
    print(e.details())

# g = pain.GroupHeader32_CH('MSG-01',
#                           datetime.strptime("2010-02-15T07:30:00", '%Y-%m-%dT%H:%M:%S'),
#                           '123456789012345',
#                           15850.0,
#                           pain.PartyIdentification32_CH_NameAndId('name',
#                                                                   pain.Party6Choice_CH(pain.OrganisationIdentification4_CH('org'))))
# p = pain.PaymentInstructionInformation3_CH(PmtInfId='PayID',
#                                            PmtMtd='PayMethod',
#                                            ReqdExctnDt=datetime.strptime("2016-03-23", '%Y-%m-%d'),
#                                            Dbtr='PayDbtr',
#                                            DbtrAcct='Payaccount',
#                                            DbtrAgt='PayDbtrAgent',
#                                            CdtTrfTxInf = ['PayCdtTrfTxInfo'])
#
# doc = pain.Document(pain.CustomerCreditTransferInitiationV03_CH(g, p));