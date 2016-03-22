from __future__ import print_function
from pprint import pprint
from pyxb import BIND
from xsd import pain_cutted as pain
from datetime import datetime
import xml.dom.minidom

# http://pyxb.sourceforge.net/userref_index.html#userreference

# http://pyxb.sourceforge.net/arch_binding.html
# http://stackoverflow.com/questions/17309125/end-to-end-example-with-pyxb-from-an-xsd-schema-to-an-xml-document
# http://pyxb.sourceforge.net/userref_usebind.html
# http://stackoverflow.com/questions/17584287/unable-to-bind-to-pyxb-classes-with-nested-anonymous-types
# http://pyxb.sourceforge.net/userref_pyxbgen.html#pyxbgen

# http://hanjun.me/software/2013/11/30/python_and_xsd.html


doc = pain.Document_()
doc.CstmrCdtTrfInitn = BIND()
header = pain.GroupHeader32_CH()
header.MsgId = "ASDaa"
header.NbOfTxs = "123456789012345"
header.CreDtTm = datetime.strptime("2010-02-15T07:30:00", '%Y-%m-%dT%H:%M:%S')
header.CtrlSum = 1231231
header.InitgPty = BIND()
header.InitgPty = "axxxxx"
dom = xml.dom.minidom.parseString(header.toxml("utf-8", element_name='GroupHeader32-CH'))
print(dom.toprettyxml())

# cst = pain.CustomerCreditTransferInitiationV03_CH()
# xml = pain.Document_()
# print_function(xml.toxml('utf-8'))