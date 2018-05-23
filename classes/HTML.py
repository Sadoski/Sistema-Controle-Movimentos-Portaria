import io
import os
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class TAG:
    """Generic class for tags"""
    def __init__(self, inner_HTML="", **attrs):
        self.tag = self.__class__.__name__
        self.inner_HTML = inner_HTML
        self.attrs = attrs
        self.children = []
        self.brothers = []

    def __str__(self):
        res=io.StringIO()
        w=res.write
        if self.tag != "TEXT":
            w("<%s" %self.tag)
            # attributes which will produce arg = "val"
            attr1 = [ k for k in self.attrs
                if not isinstance(self.attrs[k],bool) ]
            w("".join([' %s="%s"'
                %(k.replace('_','-'),self.attrs[k]) for k in attr1]))
            # attributes with no argument
            # if value is False, don't generate anything
            attr2 = [ k for k in self.attrs if self.attrs[k] is True ]
            w("".join([' %s' %k for k in attr2]))
            w(">")
        if self.tag in ONE_LINE:
            w('\n')
        w(str(self.inner_HTML))
        for child in self.children:
            w(str(child))
        if self.tag in CLOSING_TAGS:
            w("</%s>" %self.tag)
        if self.tag in LINE_BREAK_AFTER:
            w('\n')
        if hasattr(self,"brothers"):
            for brother in self.brothers:
                w(str(brother))
        return res.getvalue()

    def __le__(self,other):
        """Add a child"""
        if isinstance(other,str):
            other = TEXT(other)
        self.children.append(other)
        other.parent = self
        return self

    def __add__(self,other):
        """Return a new instance : concatenation of self and another tag"""
        res = TAG()
        res.tag = self.tag
        res.inner_HTML = self.inner_HTML
        res.attrs = self.attrs
        res.children = self.children
        res.brothers = self.brothers + [other]
        return res

    def __radd__(self,other):
        """Used to add a tag to a string"""
        if isinstance(other,str):
            return TEXT(other)+self
        else:
            raise ValueError("Can't concatenate %s and instance") %other

    def __mul__(self,n):
        """Replicate self n times, with tag first : TAG * n"""
        res = TAG()
        res.tag = self.tag
        res.inner_HTML = self.inner_HTML
        res.attrs = self.attrs
        for i in range(n-1):
            res += self
        return res

    def __rmul__(self,n):
        """Replicate self n times, with n first : n * TAG"""
        return self*n

    def gerar(dados):
        head = HEAD(TITLE('Relatório Pessoa Fisíca'))
        head <= STYLE("table{width: 90%; margin: 0 auto; text-align: justify; border: 1px solid black; border-collapse: collapse; white-space: pre-line; table-layout: auto; width: content-box; height: content-box;} th{border: 2px solid black; background-color: #D3D3D3; text-align: center; heigt: 100%} td{border: 1px solid black; text-align: justify; }")
        body = BODY()
        body <= H1('Relatório Pessoa Fisíca')
        tab = TABLE()
        body <= tab
        thead = THEAD()
        tab <= thead
        tr = TR()
        thead <= tr
        tr <= TH("Codigo")
        tr <= TH("Nome")
        tr <= TH("Sobrenome")
        tr <= TH("CPF")
        tr <= TH("RG")
        tr <= TH("Expeditor")
        tr <= TH("UF")
        tr <= TH("Nascimento")
        tr <= TH("Gênero")
        tr <= TH("Mãe")
        tr <= TH("Pai")
        tr <= TH("Endereco")
        tr <= TH("Numero")
        tr <= TH("Complemento")
        tr <= TH("Bairro")
        tr <= TH("Cidade")
        tr <= TH("Estado")
        tr <= TH("CEP")
        tbody = TBODY()
        tab <= tbody
        trr = TR()
        tbody <= trr
        for a in dados:
            trr = TR()
            tbody <= trr
            trr <= TD(a[0])
            trr <= TD(a[1])
            trr <= TD(a[2])
            trr <= TD(a[3])
            trr <= TD(a[4])
            trr <= TD(a[5])
            trr <= TD(a[6])
            trr <= TD(a[7])
            trr <= TD(a[8])
            trr <= TD(a[9])
            trr <= TD(a[10])
            trr <= TD(a[11])
            trr <= TD(a[12])
            trr <= TD(a[13])
            trr <= TD(a[14])
            trr <= TD(a[15])
            trr <= TD(a[16])
            trr <= TD(a[17])

        dir = salvar()
        if dir:
            with open(dir, 'w') as html:
                html.write(str(HTML(head + body)))
                html.close()


# list of tags, from the HTML 4.01 specification

CLOSING_TAGS =  ['A', 'ABBR', 'ACRONYM', 'ADDRESS', 'APPLET',
            'B', 'BDO', 'BIG', 'BLOCKQUOTE', 'BUTTON',
            'CAPTION', 'CENTER', 'CITE', 'CODE',
            'DEL', 'DFN', 'DIR', 'DIV', 'DL',
            'EM', 'FIELDSET', 'FONT', 'FORM', 'FRAMESET',
            'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
            'I', 'IFRAME', 'INS', 'KBD', 'LABEL', 'LEGEND',
            'MAP', 'MENU', 'NOFRAMES', 'NOSCRIPT', 'OBJECT',
            'OL', 'OPTGROUP', 'PRE', 'Q', 'S', 'SAMP',
            'SCRIPT', 'SELECT', 'SMALL', 'SPAN', 'STRIKE',
            'STRONG', 'STYLE', 'SUB', 'SUP', 'TABLE',
            'TEXTAREA', 'TITLE', 'TT', 'U', 'UL',
            'VAR', 'BODY', 'COLGROUP', 'DD', 'DT', 'HEAD',
            'HTML', 'LI', 'P', 'TBODY','OPTION', 
            'TD', 'TFOOT', 'TH', 'THEAD', 'TR']

NON_CLOSING_TAGS = ['AREA', 'BASE', 'BASEFONT', 'BR', 'COL', 'FRAME',
            'HR', 'IMG', 'INPUT', 'ISINDEX', 'LINK',
            'META', 'PARAM']

# create the classes
for tag in CLOSING_TAGS + NON_CLOSING_TAGS + ['TEXT']:
    exec("class %s(TAG): pass" %tag)
    
def Sum(iterable):
    """Return the concatenation of the instances in the iterable
    Can't use the built-in sum() on non-integers"""
    it = [ item for item in iterable ]
    if it:
        return reduce(lambda x,y:x+y, it)
    else:
        return ''

# whitespace-insensitive tags, determines pretty-print rendering
LINE_BREAK_AFTER = NON_CLOSING_TAGS + ['HTML','HEAD','BODY',
    'FRAMESET','FRAME',
    'TITLE','SCRIPT',
    'TABLE','TR','TD','TH','SELECT','OPTION',
    'FORM',
    'H1', 'H2', 'H3', 'H4', 'H5', 'H6',
    ]
# tags whose opening tag should be alone in its line
ONE_LINE = ['HTML','HEAD','BODY',
    'FRAMESET'
    'SCRIPT',
    'TABLE','TR','TD','TH','SELECT','OPTION',
    'FORM',
    ]


def salvar():
    diretorioBase = ''

    if os.name == 'nt':
        diretorioBase = 'C' + ':'
    else:
        diretorioBase = os.getenv("HOME")

    caminhoAbsoluto = diretorioBase + os.sep + 'SCMP' + os.sep + 'Relatório' + os.sep + 'html' + os.sep

    if not os.path.exists(caminhoAbsoluto):
        os.makedirs(caminhoAbsoluto)

    name = QFileDialog.getSaveFileName(None, 'Salvar', caminhoAbsoluto, 'HTML (*.html)')

    return name
