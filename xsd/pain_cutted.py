# .\pain_cutted.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:7185ec3dae8c7f9916e615f973a3cc238712b891
# Generated 2016-03-22 16:48:47.530000 by PyXB version 1.2.4 using Python 2.7.6.final.0
# Namespace http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd

from __future__ import unicode_literals
import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys
import pyxb.utils.six as _six

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:90a01c8f-f045-11e5-b846-ac7ba197a305')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.4'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI('http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd',
                                           create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

# custom added 
# location = 'C:\\Users\\modzelwo\\PycharmProjects\\xsd_cutted_pyxb\\xsd\\pain_cutted.xsd'
location = '/Users/wojtek/PycharmProjects/xsd_cutted_pyxb1/pain_cutted.xsd'

def CreateFromDocument(xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement, default_namespace=default_namespace)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, _six.text_type):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance


def CreateFromDOM(node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}AnyBICIdentifier
class AnyBICIdentifier(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'AnyBICIdentifier')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 91, 1)
    _Documentation = None


AnyBICIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
AnyBICIdentifier._CF_pattern.addPattern(pattern='[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}')
AnyBICIdentifier._InitializeFacetMap(AnyBICIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'AnyBICIdentifier', AnyBICIdentifier)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}DecimalNumber
class DecimalNumber(pyxb.binding.datatypes.decimal):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DecimalNumber')
    _XSDLocation = pyxb.utils.utility.Location(location, 96, 1)
    _Documentation = None


DecimalNumber._CF_fractionDigits = pyxb.binding.facets.CF_fractionDigits(
    value=pyxb.binding.datatypes.nonNegativeInteger(17))
DecimalNumber._CF_totalDigits = pyxb.binding.facets.CF_totalDigits(value=pyxb.binding.datatypes.positiveInteger(18))
DecimalNumber._InitializeFacetMap(DecimalNumber._CF_fractionDigits,
                                  DecimalNumber._CF_totalDigits)
Namespace.addCategoryObject('typeBinding', 'DecimalNumber', DecimalNumber)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}BasicText-CH
class BasicText_CH(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicText-CH')
    _XSDLocation = pyxb.utils.utility.Location(location, 103, 1)
    _Documentation = None


BasicText_CH._CF_pattern = pyxb.binding.facets.CF_pattern()
BasicText_CH._CF_pattern.addPattern(
    pattern='([a-zA-Z0-9\\.,;:\'\\+\\-/\\(\\)?\\*\\[\\]\\{\\}\\\\`\xb4~ ]|[!"#%&<>\xf7=@_$\xa3]|[\xe0\xe1\xe2\xe4\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf1\xf2\xf3\xf4\xf6\xf9\xfa\xfb\xfc\xfd\xdf\xc0\xc1\xc2\xc4\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd2\xd3\xd4\xd6\xd9\xda\xdb\xdc\xd1])*')
BasicText_CH._InitializeFacetMap(BasicText_CH._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BasicText-CH', BasicText_CH)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}BasicText-Swift
class BasicText_Swift(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BasicText-Swift')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 109, 1)
    _Documentation = None


BasicText_Swift._CF_pattern = pyxb.binding.facets.CF_pattern()
BasicText_Swift._CF_pattern.addPattern(pattern="([A-Za-z0-9]|[+|\\?|/|\\-|:|\\(|\\)|\\.|,|'|\\p{Zs}])*")
BasicText_Swift._InitializeFacetMap(BasicText_Swift._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BasicText-Swift', BasicText_Swift)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}BICIdentifier
class BICIdentifier(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'BICIdentifier')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 114, 1)
    _Documentation = None


BICIdentifier._CF_pattern = pyxb.binding.facets.CF_pattern()
BICIdentifier._CF_pattern.addPattern(pattern='[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}')
BICIdentifier._InitializeFacetMap(BICIdentifier._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'BICIdentifier', BICIdentifier)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ISODate
class ISODate(pyxb.binding.datatypes.date):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODate')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 119, 1)
    _Documentation = None


ISODate._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODate', ISODate)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ISODateTime
class ISODateTime(pyxb.binding.datatypes.dateTime):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ISODateTime')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 122, 1)
    _Documentation = None


ISODateTime._InitializeFacetMap()
Namespace.addCategoryObject('typeBinding', 'ISODateTime', ISODateTime)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max15NumericText
class Max15NumericText(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max15NumericText')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 137, 1)
    _Documentation = None


Max15NumericText._CF_pattern = pyxb.binding.facets.CF_pattern()
Max15NumericText._CF_pattern.addPattern(pattern='[0-9]{1,15}')
Max15NumericText._InitializeFacetMap(Max15NumericText._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'Max15NumericText', Max15NumericText)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CountryCode
class CountryCode(pyxb.binding.datatypes.string):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CountryCode')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 185, 1)
    _Documentation = None


CountryCode._CF_pattern = pyxb.binding.facets.CF_pattern()
CountryCode._CF_pattern.addPattern(pattern='[A-Z]{2,2}')
CountryCode._InitializeFacetMap(CountryCode._CF_pattern)
Namespace.addCategoryObject('typeBinding', 'CountryCode', CountryCode)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max10Text
class Max10Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max10Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 125, 1)
    _Documentation = None


Max10Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(10))
Max10Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max10Text._InitializeFacetMap(Max10Text._CF_maxLength,
                              Max10Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max10Text', Max10Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max140Text
class Max140Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max140Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 131, 1)
    _Documentation = None


Max140Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(140))
Max140Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max140Text._InitializeFacetMap(Max140Text._CF_maxLength,
                               Max140Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max140Text', Max140Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max16Text
class Max16Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max16Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 142, 1)
    _Documentation = None


Max16Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(16))
Max16Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max16Text._InitializeFacetMap(Max16Text._CF_maxLength,
                              Max16Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max16Text', Max16Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max2048Text
class Max2048Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max2048Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 148, 1)
    _Documentation = None


Max2048Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(2048))
Max2048Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max2048Text._InitializeFacetMap(Max2048Text._CF_maxLength,
                                Max2048Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max2048Text', Max2048Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max34Text
class Max34Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max34Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 154, 1)
    _Documentation = None


Max34Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(34))
Max34Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max34Text._InitializeFacetMap(Max34Text._CF_maxLength,
                              Max34Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max34Text', Max34Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max35Text
class Max35Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 160, 1)
    _Documentation = None


Max35Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
Max35Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max35Text._InitializeFacetMap(Max35Text._CF_maxLength,
                              Max35Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max35Text', Max35Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max35Text-Swift
class Max35Text_Swift(BasicText_Swift):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max35Text-Swift')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 167, 1)
    _Documentation = None


Max35Text_Swift._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(35))
Max35Text_Swift._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max35Text_Swift._InitializeFacetMap(Max35Text_Swift._CF_maxLength,
                                    Max35Text_Swift._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max35Text-Swift', Max35Text_Swift)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max4Text
class Max4Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max4Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 173, 1)
    _Documentation = None


Max4Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(4))
Max4Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max4Text._InitializeFacetMap(Max4Text._CF_maxLength,
                             Max4Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max4Text', Max4Text)


# Atomic simple type: {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Max70Text
class Max70Text(BasicText_CH):
    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Max70Text')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 179, 1)
    _Documentation = None


Max70Text._CF_maxLength = pyxb.binding.facets.CF_maxLength(value=pyxb.binding.datatypes.nonNegativeInteger(70))
Max70Text._CF_minLength = pyxb.binding.facets.CF_minLength(value=pyxb.binding.datatypes.nonNegativeInteger(1))
Max70Text._InitializeFacetMap(Max70Text._CF_maxLength,
                              Max70Text._CF_minLength)
Namespace.addCategoryObject('typeBinding', 'Max70Text', Max70Text)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Document with content type ELEMENT_ONLY
class Document_(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Document with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Document')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 4, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CstmrCdtTrfInitn uses Python identifier CstmrCdtTrfInitn
    __CstmrCdtTrfInitn = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, 'CstmrCdtTrfInitn'), 'CstmrCdtTrfInitn',
        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_Document__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCstmrCdtTrfInitn',
        False,
        pyxb.utils.utility.Location(location, 6,
                                    3), )

    CstmrCdtTrfInitn = property(__CstmrCdtTrfInitn.value, __CstmrCdtTrfInitn.set, None, None)

    _ElementMap.update({
        __CstmrCdtTrfInitn.name(): __CstmrCdtTrfInitn
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'Document', Document_)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CustomerCreditTransferInitiationV03-CH with content type ELEMENT_ONLY
class CustomerCreditTransferInitiationV03_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CustomerCreditTransferInitiationV03-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'CustomerCreditTransferInitiationV03-CH')
    _XSDLocation = pyxb.utils.utility.Location(location, 9, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}GrpHdr uses Python identifier GrpHdr
    __GrpHdr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), 'GrpHdr',
                                                       '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_CustomerCreditTransferInitiationV03_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdGrpHdr',
                                                       False, pyxb.utils.utility.Location(location, 11, 3),)

    GrpHdr = property(__GrpHdr.value, __GrpHdr.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PmtInf uses Python identifier PmtInf
    __PmtInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtInf'), 'PmtInf',
                                                       '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_CustomerCreditTransferInitiationV03_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdPmtInf',
                                                       True, pyxb.utils.utility.Location(
            location, 12, 3), )

    PmtInf = property(__PmtInf.value, __PmtInf.set, None, None)

    _ElementMap.update({
        __GrpHdr.name(): __GrpHdr,
        __PmtInf.name(): __PmtInf
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'CustomerCreditTransferInitiationV03-CH',
                            CustomerCreditTransferInitiationV03_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PaymentInstructionInformation3-CH with content type ELEMENT_ONLY
class PaymentInstructionInformation3_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PaymentInstructionInformation3-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PaymentInstructionInformation3-CH')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 16, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PmtInfId uses Python identifier PmtInfId
    __PmtInfId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId'), 'PmtInfId',
                                                         '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdPmtInfId',
                                                         False, pyxb.utils.utility.Location(
            location, 19, 3), )

    PmtInfId = property(__PmtInfId.value, __PmtInfId.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PmtMtd uses Python identifier PmtMtd
    __PmtMtd = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd'), 'PmtMtd',
                                                       '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdPmtMtd',
                                                       False, pyxb.utils.utility.Location(
            location, 20, 3), )

    PmtMtd = property(__PmtMtd.value, __PmtMtd.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}BtchBookg uses Python identifier BtchBookg
    __BtchBookg = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg'),
                                                          'BtchBookg',
                                                          '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdBtchBookg',
                                                          False, pyxb.utils.utility.Location(
            location, 21, 3), )

    BtchBookg = property(__BtchBookg.value, __BtchBookg.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}NbOfTxs uses Python identifier NbOfTxs
    __NbOfTxs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), 'NbOfTxs',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdNbOfTxs',
                                                        False, pyxb.utils.utility.Location(
            location, 22, 3), )

    NbOfTxs = property(__NbOfTxs.value, __NbOfTxs.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CtrlSum uses Python identifier CtrlSum
    __CtrlSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), 'CtrlSum',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCtrlSum',
                                                        False, pyxb.utils.utility.Location(
            location, 23, 3), )

    CtrlSum = property(__CtrlSum.value, __CtrlSum.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PmtTpInf uses Python identifier PmtTpInf
    __PmtTpInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), 'PmtTpInf',
                                                         '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdPmtTpInf',
                                                         False, pyxb.utils.utility.Location(
            location, 24, 3), )

    PmtTpInf = property(__PmtTpInf.value, __PmtTpInf.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ReqdExctnDt uses Python identifier ReqdExctnDt
    __ReqdExctnDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt'),
                                                            'ReqdExctnDt',
                                                            '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdReqdExctnDt',
                                                            False, pyxb.utils.utility.Location(
            location, 25, 3), )

    ReqdExctnDt = property(__ReqdExctnDt.value, __ReqdExctnDt.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Dbtr uses Python identifier Dbtr
    __Dbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), 'Dbtr',
                                                     '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdDbtr',
                                                     False, pyxb.utils.utility.Location(
            location, 26, 3), )

    Dbtr = property(__Dbtr.value, __Dbtr.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}DbtrAcct uses Python identifier DbtrAcct
    __DbtrAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct'), 'DbtrAcct',
                                                         '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdDbtrAcct',
                                                         False, pyxb.utils.utility.Location(
            location, 27, 3), )

    DbtrAcct = property(__DbtrAcct.value, __DbtrAcct.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}DbtrAgt uses Python identifier DbtrAgt
    __DbtrAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt'), 'DbtrAgt',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdDbtrAgt',
                                                        False, pyxb.utils.utility.Location(
            location, 28, 3), )

    DbtrAgt = property(__DbtrAgt.value, __DbtrAgt.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}UltmtDbtr uses Python identifier UltmtDbtr
    __UltmtDbtr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'),
                                                          'UltmtDbtr',
                                                          '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdUltmtDbtr',
                                                          False, pyxb.utils.utility.Location(
            location, 29, 3), )

    UltmtDbtr = property(__UltmtDbtr.value, __UltmtDbtr.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ChrgBr uses Python identifier ChrgBr
    __ChrgBr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr'), 'ChrgBr',
                                                       '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdChrgBr',
                                                       False, pyxb.utils.utility.Location(
            location, 30, 3), )

    ChrgBr = property(__ChrgBr.value, __ChrgBr.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ChrgsAcct uses Python identifier ChrgsAcct
    __ChrgsAcct = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct'),
                                                          'ChrgsAcct',
                                                          '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdChrgsAcct',
                                                          False, pyxb.utils.utility.Location(
            location, 31, 3), )

    ChrgsAcct = property(__ChrgsAcct.value, __ChrgsAcct.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CdtTrfTxInf uses Python identifier CdtTrfTxInf
    __CdtTrfTxInf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf'),
                                                            'CdtTrfTxInf',
                                                            '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PaymentInstructionInformation3_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCdtTrfTxInf',
                                                            True, pyxb.utils.utility.Location(
            location, 32, 3), )

    CdtTrfTxInf = property(__CdtTrfTxInf.value, __CdtTrfTxInf.set, None, None)

    _ElementMap.update({
        __PmtInfId.name(): __PmtInfId,
        __PmtMtd.name(): __PmtMtd,
        __BtchBookg.name(): __BtchBookg,
        __NbOfTxs.name(): __NbOfTxs,
        __CtrlSum.name(): __CtrlSum,
        __PmtTpInf.name(): __PmtTpInf,
        __ReqdExctnDt.name(): __ReqdExctnDt,
        __Dbtr.name(): __Dbtr,
        __DbtrAcct.name(): __DbtrAcct,
        __DbtrAgt.name(): __DbtrAgt,
        __UltmtDbtr.name(): __UltmtDbtr,
        __ChrgBr.name(): __ChrgBr,
        __ChrgsAcct.name(): __ChrgsAcct,
        __CdtTrfTxInf.name(): __CdtTrfTxInf
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'PaymentInstructionInformation3-CH', PaymentInstructionInformation3_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}GroupHeader32-CH with content type ELEMENT_ONLY
class GroupHeader32_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}GroupHeader32-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'GroupHeader32-CH')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 36, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}MsgId uses Python identifier MsgId
    __MsgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), 'MsgId',
                                                      '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_GroupHeader32_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdMsgId',
                                                      False, pyxb.utils.utility.Location(
            location, 38, 3), )

    MsgId = property(__MsgId.value, __MsgId.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CreDtTm uses Python identifier CreDtTm
    __CreDtTm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), 'CreDtTm',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_GroupHeader32_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCreDtTm',
                                                        False, pyxb.utils.utility.Location(
            location, 39, 3), )

    CreDtTm = property(__CreDtTm.value, __CreDtTm.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}NbOfTxs uses Python identifier NbOfTxs
    __NbOfTxs = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), 'NbOfTxs',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_GroupHeader32_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdNbOfTxs',
                                                        False, pyxb.utils.utility.Location(
            location, 40, 3), )

    NbOfTxs = property(__NbOfTxs.value, __NbOfTxs.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CtrlSum uses Python identifier CtrlSum
    __CtrlSum = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), 'CtrlSum',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_GroupHeader32_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCtrlSum',
                                                        False, pyxb.utils.utility.Location(
            location, 41, 3), )

    CtrlSum = property(__CtrlSum.value, __CtrlSum.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}InitgPty uses Python identifier InitgPty
    __InitgPty = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'InitgPty'), 'InitgPty',
                                                         '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_GroupHeader32_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdInitgPty',
                                                         False, pyxb.utils.utility.Location(
            location, 42, 3), )

    InitgPty = property(__InitgPty.value, __InitgPty.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}FwdgAgt uses Python identifier FwdgAgt
    __FwdgAgt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt'), 'FwdgAgt',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_GroupHeader32_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdFwdgAgt',
                                                        False, pyxb.utils.utility.Location(
            location, 44, 3), )

    FwdgAgt = property(__FwdgAgt.value, __FwdgAgt.set, None, None)

    _ElementMap.update({
        __MsgId.name(): __MsgId,
        __CreDtTm.name(): __CreDtTm,
        __NbOfTxs.name(): __NbOfTxs,
        __CtrlSum.name(): __CtrlSum,
        __InitgPty.name(): __InitgPty,
        __FwdgAgt.name(): __FwdgAgt
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'GroupHeader32-CH', GroupHeader32_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PartyIdentification32-CH_NameAndId with content type ELEMENT_ONLY
class PartyIdentification32_CH_NameAndId(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PartyIdentification32-CH_NameAndId with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PartyIdentification32-CH_NameAndId')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 47, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm',
                                                   '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PartyIdentification32_CH_NameAndId_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdNm',
                                                   False, pyxb.utils.utility.Location(
            location, 49, 3), )

    Nm = property(__Nm.value, __Nm.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Id uses Python identifier Id
    __Id = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Id'), 'Id',
                                                   '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PartyIdentification32_CH_NameAndId_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdId',
                                                   False, pyxb.utils.utility.Location(
            location, 50, 3), )

    Id = property(__Id.value, __Id.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CtctDtls uses Python identifier CtctDtls
    __CtctDtls = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls'), 'CtctDtls',
                                                         '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PartyIdentification32_CH_NameAndId_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCtctDtls',
                                                         False, pyxb.utils.utility.Location(
            location, 52, 3), )

    CtctDtls = property(__CtctDtls.value, __CtctDtls.set, None, None)

    _ElementMap.update({
        __Nm.name(): __Nm,
        __Id.name(): __Id,
        __CtctDtls.name(): __CtctDtls
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'PartyIdentification32-CH_NameAndId', PartyIdentification32_CH_NameAndId)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Party6Choice-CH with content type ELEMENT_ONLY
class Party6Choice_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Party6Choice-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'Party6Choice-CH')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 55, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}OrgId uses Python identifier OrgId
    __OrgId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), 'OrgId',
                                                      '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_Party6Choice_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdOrgId',
                                                      False, pyxb.utils.utility.Location(
            location, 58, 4), )

    OrgId = property(__OrgId.value, __OrgId.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PrvtId uses Python identifier PrvtId
    __PrvtId = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), 'PrvtId',
                                                       '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_Party6Choice_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdPrvtId',
                                                       False, pyxb.utils.utility.Location(
            location, 59, 4), )

    PrvtId = property(__PrvtId.value, __PrvtId.set, None, None)

    _ElementMap.update({
        __OrgId.name(): __OrgId,
        __PrvtId.name(): __PrvtId
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'Party6Choice-CH', Party6Choice_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ContactDetails2-CH with content type ELEMENT_ONLY
class ContactDetails2_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}ContactDetails2-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'ContactDetails2-CH')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 63, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Nm uses Python identifier Nm
    __Nm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Nm'), 'Nm',
                                                   '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_ContactDetails2_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdNm',
                                                   False, pyxb.utils.utility.Location(
            location, 65, 3), )

    Nm = property(__Nm.value, __Nm.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr',
                                                     '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_ContactDetails2_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdOthr',
                                                     False, pyxb.utils.utility.Location(
            location, 66, 3), )

    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __Nm.name(): __Nm,
        __Othr.name(): __Othr
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'ContactDetails2-CH', ContactDetails2_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}OrganisationIdentification4-CH with content type ELEMENT_ONLY
class OrganisationIdentification4_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}OrganisationIdentification4-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'OrganisationIdentification4-CH')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 69, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}BICOrBEI uses Python identifier BICOrBEI
    __BICOrBEI = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), 'BICOrBEI',
                                                         '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_OrganisationIdentification4_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdBICOrBEI',
                                                         False, pyxb.utils.utility.Location(
            location, 71, 3), )

    BICOrBEI = property(__BICOrBEI.value, __BICOrBEI.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr',
                                                     '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_OrganisationIdentification4_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdOthr',
                                                     False, pyxb.utils.utility.Location(
            location, 73, 3), )

    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __BICOrBEI.name(): __BICOrBEI,
        __Othr.name(): __Othr
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'OrganisationIdentification4-CH', OrganisationIdentification4_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PersonIdentification5-CH with content type ELEMENT_ONLY
class PersonIdentification5_CH(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PersonIdentification5-CH with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'PersonIdentification5-CH')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 76, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}DtAndPlcOfBirth uses Python identifier DtAndPlcOfBirth
    __DtAndPlcOfBirth = pyxb.binding.content.ElementDeclaration(
        pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth'), 'DtAndPlcOfBirth',
        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PersonIdentification5_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdDtAndPlcOfBirth',
        False,
        pyxb.utils.utility.Location(location, 78,
                                    3), )

    DtAndPlcOfBirth = property(__DtAndPlcOfBirth.value, __DtAndPlcOfBirth.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}Othr uses Python identifier Othr
    __Othr = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'Othr'), 'Othr',
                                                     '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_PersonIdentification5_CH_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdOthr',
                                                     False, pyxb.utils.utility.Location(
            location, 80, 3), )

    Othr = property(__Othr.value, __Othr.set, None, None)

    _ElementMap.update({
        __DtAndPlcOfBirth.name(): __DtAndPlcOfBirth,
        __Othr.name(): __Othr
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'PersonIdentification5-CH', PersonIdentification5_CH)


# Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}DateAndPlaceOfBirth with content type ELEMENT_ONLY
class DateAndPlaceOfBirth(pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}DateAndPlaceOfBirth with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, 'DateAndPlaceOfBirth')
    _XSDLocation = pyxb.utils.utility.Location(
        location, 83, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}BirthDt uses Python identifier BirthDt
    __BirthDt = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'BirthDt'), 'BirthDt',
                                                        '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_DateAndPlaceOfBirth_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdBirthDt',
                                                        False, pyxb.utils.utility.Location(
            location, 85, 3), )

    BirthDt = property(__BirthDt.value, __BirthDt.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}PrvcOfBirth uses Python identifier PrvcOfBirth
    __PrvcOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth'),
                                                            'PrvcOfBirth',
                                                            '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_DateAndPlaceOfBirth_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdPrvcOfBirth',
                                                            False, pyxb.utils.utility.Location(
            location, 86, 3), )

    PrvcOfBirth = property(__PrvcOfBirth.value, __PrvcOfBirth.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CityOfBirth uses Python identifier CityOfBirth
    __CityOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth'),
                                                            'CityOfBirth',
                                                            '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_DateAndPlaceOfBirth_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCityOfBirth',
                                                            False, pyxb.utils.utility.Location(
            location, 87, 3), )

    CityOfBirth = property(__CityOfBirth.value, __CityOfBirth.set, None, None)

    # Element {http://www.six-interbank-clearing.com/de/pain.001.001.03.ch.02.xsd}CtryOfBirth uses Python identifier CtryOfBirth
    __CtryOfBirth = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth'),
                                                            'CtryOfBirth',
                                                            '__httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsd_DateAndPlaceOfBirth_httpwww_six_interbank_clearing_comdepain_001_001_03_ch_02_xsdCtryOfBirth',
                                                            False, pyxb.utils.utility.Location(
            location, 88, 3), )

    CtryOfBirth = property(__CtryOfBirth.value, __CtryOfBirth.set, None, None)

    _ElementMap.update({
        __BirthDt.name(): __BirthDt,
        __PrvcOfBirth.name(): __PrvcOfBirth,
        __CityOfBirth.name(): __CityOfBirth,
        __CtryOfBirth.name(): __CtryOfBirth
    })
    _AttributeMap.update({

    })


Namespace.addCategoryObject('typeBinding', 'DateAndPlaceOfBirth', DateAndPlaceOfBirth)

Document = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Document'), Document_,
                                      location=pyxb.utils.utility.Location(
                                          location,
                                          3, 1))
Namespace.addCategoryObject('elementBinding', Document.name().localName(), Document)

Document_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CstmrCdtTrfInitn'),
                                                 CustomerCreditTransferInitiationV03_CH, scope=Document_,
                                                 location=pyxb.utils.utility.Location(
                                                     location,
                                                     6, 3)))


def _BuildAutomaton():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Document_._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CstmrCdtTrfInitn')),
        pyxb.utils.utility.Location(location, 6,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Document_._Automaton = _BuildAutomaton()

CustomerCreditTransferInitiationV03_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr'), GroupHeader32_CH,
                               scope=CustomerCreditTransferInitiationV03_CH, location=pyxb.utils.utility.Location(
            location, 11, 3)))

CustomerCreditTransferInitiationV03_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtInf'), PaymentInstructionInformation3_CH,
                               scope=CustomerCreditTransferInitiationV03_CH, location=pyxb.utils.utility.Location(
            location, 12, 3)))


def _BuildAutomaton_():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        CustomerCreditTransferInitiationV03_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'GrpHdr')),
        pyxb.utils.utility.Location(location, 11,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        CustomerCreditTransferInitiationV03_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtInf')),
        pyxb.utils.utility.Location(location, 12,
                                    3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


CustomerCreditTransferInitiationV03_CH._Automaton = _BuildAutomaton_()

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId'), Max35Text_Swift,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 19, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 20, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 21, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), Max15NumericText,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 22, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), DecimalNumber,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 23, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 24, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt'), ISODate,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 25, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Dbtr'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 26, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 27, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 28, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 29, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 30, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 31, 3)))

PaymentInstructionInformation3_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf'), Max70Text,
                               scope=PaymentInstructionInformation3_CH, location=pyxb.utils.utility.Location(
            location, 32, 3)))


def _BuildAutomaton_2():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 21, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 22, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 23, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 24, 3))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 29, 3))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 30, 3))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 31, 3))
    counters.add(cc_6)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtInfId')),
        pyxb.utils.utility.Location(location, 19,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtMtd')),
        pyxb.utils.utility.Location(location, 20,
                                    3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BtchBookg')),
        pyxb.utils.utility.Location(location, 21,
                                    3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs')),
        pyxb.utils.utility.Location(location, 22,
                                    3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum')),
        pyxb.utils.utility.Location(location, 23,
                                    3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PmtTpInf')),
        pyxb.utils.utility.Location(location, 24,
                                    3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ReqdExctnDt')),
        pyxb.utils.utility.Location(location, 25,
                                    3))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Dbtr')),
        pyxb.utils.utility.Location(location, 26,
                                    3))
    st_7 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrAcct')),
        pyxb.utils.utility.Location(location, 27,
                                    3))
    st_8 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DbtrAgt')),
        pyxb.utils.utility.Location(location, 28,
                                    3))
    st_9 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'UltmtDbtr')),
        pyxb.utils.utility.Location(location, 29,
                                    3))
    st_10 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChrgBr')),
        pyxb.utils.utility.Location(location, 30,
                                    3))
    st_11 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'ChrgsAcct')),
        pyxb.utils.utility.Location(location, 31,
                                    3))
    st_12 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        PaymentInstructionInformation3_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CdtTrfTxInf')),
        pyxb.utils.utility.Location(location, 32,
                                    3))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    transitions.append(fac.Transition(st_5, [
    ]))
    transitions.append(fac.Transition(st_6, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False)]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, True)]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False)]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True)]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False)]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
    ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
    ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
    ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
    ]))
    transitions.append(fac.Transition(st_11, [
    ]))
    transitions.append(fac.Transition(st_12, [
    ]))
    transitions.append(fac.Transition(st_13, [
    ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, True)]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_4, False)]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, True)]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_5, False)]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, True)]))
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_6, False)]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
    ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


PaymentInstructionInformation3_CH._Automaton = _BuildAutomaton_2()

GroupHeader32_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'MsgId'), Max35Text_Swift, scope=GroupHeader32_CH,
                               location=pyxb.utils.utility.Location(
                                   location, 38,
                                   3)))

GroupHeader32_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm'), ISODateTime, scope=GroupHeader32_CH,
                               location=pyxb.utils.utility.Location(
                                   location, 39,
                                   3)))

GroupHeader32_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs'), Max15NumericText,
                               scope=GroupHeader32_CH, location=pyxb.utils.utility.Location(
            location, 40, 3)))

GroupHeader32_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum'), DecimalNumber, scope=GroupHeader32_CH,
                               location=pyxb.utils.utility.Location(
                                   location, 41,
                                   3)))

GroupHeader32_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'InitgPty'), PartyIdentification32_CH_NameAndId,
                               scope=GroupHeader32_CH, location=pyxb.utils.utility.Location(
            location, 42, 3)))

GroupHeader32_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt'), Max70Text, scope=GroupHeader32_CH,
                               location=pyxb.utils.utility.Location(
                                   location, 44,
                                   3)))


def _BuildAutomaton_3():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 41, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 44, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        GroupHeader32_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'MsgId')),
        pyxb.utils.utility.Location(location, 38,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        GroupHeader32_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CreDtTm')),
        pyxb.utils.utility.Location(location, 39,
                                    3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        GroupHeader32_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'NbOfTxs')),
        pyxb.utils.utility.Location(location, 40,
                                    3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        GroupHeader32_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtrlSum')),
        pyxb.utils.utility.Location(location, 41,
                                    3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        GroupHeader32_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'InitgPty')),
        pyxb.utils.utility.Location(location, 42,
                                    3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        GroupHeader32_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'FwdgAgt')),
        pyxb.utils.utility.Location(location, 44,
                                    3))
    st_5 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
    ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    transitions.append(fac.Transition(st_4, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False)]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
    ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, True)]))
    st_5._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


GroupHeader32_CH._Automaton = _BuildAutomaton_3()

PartyIdentification32_CH_NameAndId._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text,
                               scope=PartyIdentification32_CH_NameAndId, location=pyxb.utils.utility.Location(
            location, 49, 3)))

PartyIdentification32_CH_NameAndId._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Id'), Party6Choice_CH,
                               scope=PartyIdentification32_CH_NameAndId, location=pyxb.utils.utility.Location(
            location, 50, 3)))

PartyIdentification32_CH_NameAndId._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls'), ContactDetails2_CH,
                               scope=PartyIdentification32_CH_NameAndId, location=pyxb.utils.utility.Location(
            location, 52, 3)))


def _BuildAutomaton_4():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 49, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 50, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 52, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        PartyIdentification32_CH_NameAndId._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')),
        pyxb.utils.utility.Location(location, 49,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        PartyIdentification32_CH_NameAndId._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Id')),
        pyxb.utils.utility.Location(location, 50,
                                    3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(
        PartyIdentification32_CH_NameAndId._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtctDtls')),
        pyxb.utils.utility.Location(location, 52,
                                    3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True)]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


PartyIdentification32_CH_NameAndId._Automaton = _BuildAutomaton_4()

Party6Choice_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'OrgId'), OrganisationIdentification4_CH,
                               scope=Party6Choice_CH, location=pyxb.utils.utility.Location(
            location, 58, 4)))

Party6Choice_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvtId'), PersonIdentification5_CH,
                               scope=Party6Choice_CH, location=pyxb.utils.utility.Location(
            location, 59, 4)))


def _BuildAutomaton_5():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Party6Choice_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'OrgId')),
        pyxb.utils.utility.Location(location, 58,
                                    4))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        Party6Choice_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvtId')),
        pyxb.utils.utility.Location(location, 59,
                                    4))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


Party6Choice_CH._Automaton = _BuildAutomaton_5()

ContactDetails2_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Nm'), Max70Text, scope=ContactDetails2_CH,
                               location=pyxb.utils.utility.Location(
                                   location, 65,
                                   3)))

ContactDetails2_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), Max35Text, scope=ContactDetails2_CH,
                               location=pyxb.utils.utility.Location(
                                   location, 66,
                                   3)))


def _BuildAutomaton_6():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 65, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 66, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        ContactDetails2_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Nm')),
        pyxb.utils.utility.Location(location, 65,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        ContactDetails2_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')),
        pyxb.utils.utility.Location(location, 66,
                                    3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


ContactDetails2_CH._Automaton = _BuildAutomaton_6()

OrganisationIdentification4_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI'), AnyBICIdentifier,
                               scope=OrganisationIdentification4_CH, location=pyxb.utils.utility.Location(
            location, 71, 3)))

OrganisationIdentification4_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), Max70Text,
                               scope=OrganisationIdentification4_CH, location=pyxb.utils.utility.Location(
            location, 73, 3)))


def _BuildAutomaton_7():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 71, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 73, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        OrganisationIdentification4_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BICOrBEI')),
        pyxb.utils.utility.Location(location, 71,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        OrganisationIdentification4_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')),
        pyxb.utils.utility.Location(location, 73,
                                    3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


OrganisationIdentification4_CH._Automaton = _BuildAutomaton_7()

PersonIdentification5_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth'), DateAndPlaceOfBirth,
                               scope=PersonIdentification5_CH, location=pyxb.utils.utility.Location(
            location, 78, 3)))

PersonIdentification5_CH._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'Othr'), Max70Text,
                               scope=PersonIdentification5_CH, location=pyxb.utils.utility.Location(
            location, 80, 3)))


def _BuildAutomaton_8():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 78, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 80, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(
        PersonIdentification5_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'DtAndPlcOfBirth')),
        pyxb.utils.utility.Location(location, 78,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(
        PersonIdentification5_CH._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'Othr')),
        pyxb.utils.utility.Location(location, 80,
                                    3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False)]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True)]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)


PersonIdentification5_CH._Automaton = _BuildAutomaton_8()

DateAndPlaceOfBirth._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'BirthDt'), ISODate, scope=DateAndPlaceOfBirth,
                               location=pyxb.utils.utility.Location(
                                   location, 85,
                                   3)))

DateAndPlaceOfBirth._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth'), Max35Text,
                               scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location(
            location, 86, 3)))

DateAndPlaceOfBirth._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth'), Max35Text,
                               scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location(
            location, 87, 3)))

DateAndPlaceOfBirth._AddElement(
    pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth'), CountryCode,
                               scope=DateAndPlaceOfBirth, location=pyxb.utils.utility.Location(
            location, 88, 3)))


def _BuildAutomaton_9():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(
        location, 86, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'BirthDt')),
        pyxb.utils.utility.Location(location, 85,
                                    3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'PrvcOfBirth')),
        pyxb.utils.utility.Location(location, 86,
                                    3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(
        DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CityOfBirth')),
        pyxb.utils.utility.Location(location, 87,
                                    3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(
        DateAndPlaceOfBirth._UseForTag(pyxb.namespace.ExpandedName(Namespace, 'CtryOfBirth')),
        pyxb.utils.utility.Location(location, 88,
                                    3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
    ]))
    transitions.append(fac.Transition(st_2, [
    ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True)]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False)]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
    ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)


DateAndPlaceOfBirth._Automaton = _BuildAutomaton_9()
