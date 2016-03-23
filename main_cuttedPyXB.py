from __future__ import print_function
from pyxb import BIND
from xsd import pain_cutted as pain
from datetime import datetime
import xml.dom.minidom
import pyxb.utils.domutils

# read it:
# http://pyxb.sourceforge.net/userref_index.html#userreference
# http://pyxb.sourceforge.net/arch_binding.html
# http://stackoverflow.com/questions/17309125/end-to-end-example-with-pyxb-from-an-xsd-schema-to-an-xml-document
# http://pyxb.sourceforge.net/userref_usebind.html
# http://stackoverflow.com/questions/17584287/unable-to-bind-to-pyxb-classes-with-nested-anonymous-types
# http://pyxb.sourceforge.net/userref_pyxbgen.html#pyxbgen
# http://hanjun.me/software/2013/11/30/python_and_xsd.html


grpHdr = pain.GroupHeader32_CH()
grpHdr.MsgId = "MSG-01"
grpHdr.NbOfTxs = "123456789012345"
grpHdr.CreDtTm = datetime.strptime("2010-02-15T07:30:00", '%Y-%m-%dT%H:%M:%S')
grpHdr.CtrlSum = float(15850.00)  # optional

# create complex InitgPty
initgpty = pain.PartyIdentification32_CH_NameAndId()
# create complex CtctDtls
cntdts = pain.ContactDetails2_CH()
cntdts.Nm = "Contact Name"   # set simple
cntdts.Othr = "Other Value"  # set simple

initgpty.Nm = "Some name for tag Nm"  # add simple
initgpty.CtctDtls = cntdts            # add complex CtctDtls

grpHdr.InitgPty = initgpty            # add complex InitgPty

# print(grpHdr.toxml("utf-8", element_name='GrpHdr'))  # works! generates namespace as "ns1" a bit ugly..


# create complex PmtInf
pmtinf = pain.PaymentInstructionInformation3_CH()
pmtinf.PmtInfId="PayID"
pmtinf.PmtMtd="PayMethod"
pmtinf.ReqdExctnDt = datetime.strptime("2016-03-23", '%Y-%m-%d')
pmtinf.Dbtr="PayDbtr"
pmtinf.DbtrAcct="PayAccount"
pmtinf.DbtrAgt="PayDbtrAgent"
pmtinf.CdtTrfTxInf="PayCdtTrfTxInfo"


# create complex CstmrCdtTrfInitn
cstmrCdT = pain.CustomerCreditTransferInitiationV03_CH()

# here comes DIFFICULT PART

# cstmrCdT.append(BIND(grpHdr))
# cstmrCdT.append(BIND(pmtinf))
# cstmrCdT.GrpHdr = grpHdr    # add complex GrpHdr
# cstmrCdT.PmtInf = pmtinf    # add complex PmtInf
#
# print(cstmrCdT.toxml("utf-8", element_name='CstmrCdtTrfInitn'))  # UnrecognizedContentError: Invalid content

# here comes more DIFFICULT PART

# create complex Document (main tag for output XML)
doc = pain.Document_()
# doc.CstmrCdtTrfInitn = cstmrCdT  # add GrpHdr and PmtInf
doc.append(cstmrCdT)

# wish to do
# doc.toxml('utf-8')

# fancy printing

# dom = xml.dom.minidom.parseString(doc.toxml("utf-8", element_name='GroupHeader32-CH'))
# dom = xml.dom.minidom.parseString(doc.toxml("utf-8", element_name='CstmrCdtTrfInitn'))
# print(dom.toprettyxml())
