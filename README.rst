brzipcode
=========

``brzipcode`` é uma lib Python simples para retornar o endereço a partir do CEP, com dados provenientes do webservice ``brzipcode.appspot.com``.

Para instalar execute: ::

    pip install brzipcode


E então usar conforme abaixo: ::
    
    >>> from brzipcode import BRZipCode
    >>> print BRZipCode.get('04538132', token='ycmVyGJO3HAw...') # *
    {u'status': True, u'city': u'S\xe3o Paulo', u'state': u'SP', u'neighborhood': u'Itaim Bibi', u'address': u'Avenida Brigadeiro Faria Lima - de 3252 ao fim - lado par'}

** Para solicitar um token acesse http://brzipcode.appspot.com/ **

Caso não encontre nenhum resultado: ::
    
    >>> print BRZipCode.get('00000000', token='ycmVyGJO3HAw...')
    {u'status': False, u'error_message': u'not_found'}


Suporte a projetos Django
-------------------------

Para utilizar em seu projeto Django, inclua ``BRZIPCODE_TOKEN`` e atualize o ``INSTALLED_APPS`` no arquivo ``settings.py`` ::

    BRZIPCODE_TOKEN = 'ycmVyGJO3HAw...'
    
    ...
    
    INSTALLED_APPS = (
        ...
        'brzipcode',
    )

Adicionar a url do serviço no ``urls.py`` ::

    urlpatterns = patterns('',
        ...
        url(r'^brzipcode/', include('brzipcode.urls')),
    )


E acesse: ::
    
    http://localhost:8000/brzipcode/?zip_code=04538132
