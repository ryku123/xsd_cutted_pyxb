import pyxb
from xsd import pain_cutted as pain
from datetime import datetime

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
grpHdr.CtrlSum = "123.333333.4"

pmtinf = pain.PaymentInstructionInformation3_CH()
pmtinf.PmtInfId="PayID"
pmtinf.PmtMtd="PayMethod"
pmtinf.ReqdExctnDt = datetime.strptime("2016-03-23", '%Y-%m-%d')
pmtinf.Dbtr="PayDbtr"
pmtinf.DbtrAcct="PayAccount"
pmtinf.DbtrAgt="PayDbtrAgent"
pmtinf.CdtTrfTxInf="PayCdtTrfTxInfo"

cstmrCdT = pain.CustomerCreditTransferInitiationV03_CH()
cstmrCdT.GrpHdr = grpHdr
# PmtInf is a multi-valued element so it's a list: append the new value
print "type(cstmrCdT): ", type(cstmrCdT)
print "type(cstmrCdT.PmtInf): ", type(cstmrCdT.PmtInf)
cstmrCdT.PmtInf.append(pmtinf)

doc = pain.Document()
doc.CstmrCdtTrfInitn = cstmrCdT

# Missing piece:
# grpHdr.InitgPty = pain.PartyIdentification32_CH_NameAndId('name',pain.Party6Choice_CH(pain.OrganisationIdentification4_CH('org')))
# or
# grpHdr.InitgPty = pyxb.BIND('name', pyxb.BIND());
# grpHdr.InitgPty.Id = pyxb.BIND();
# grpHdr.InitgPty.Id.OrgId = 'org';

try:
    doc.validateBinding()
    print doc.toDOM().toprettyxml()
except pyxb.ValidationError as e:
    print(e.details())