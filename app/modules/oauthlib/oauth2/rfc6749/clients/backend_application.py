# -*- coding: utf-8 -*-
"""
oauthlib.oauth2.rfc6749
~~~~~~~~~~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for consuming and providing OAuth 2.0 RFC6749.
"""
from __future__ import absolute_import, unicode_literals

from .base import Client
from ..parameters import prepare_token_request
from ..parameters import parse_token_response


class BackendApplicationClient(Client):
    """A public client utilizing the client credentials grant workflow.

    The client can request an access token using only its client
    credentials (or other supported means of authentication) when the
    client is requesting access to the protected resources under its
    control, or those of another resource owner which has been previously
    arranged with the authorization server (the method of which is beyond
    the scope of this specification).

    The client credentials grant type MUST only be used by confidential
    clients.

    Since the client authentication is used as the authorization grant,
    no additional authorization request is needed.
    """

    def prepare_request_body(self, body='', scope=None, **kwargs):
        """Add the client credentials to the request body.

        The client makes a request to the token endpoint by adding the
        following parameters using the "application/x-www-form-urlencoded"
        format per `Appendix B`_ in the HTTP request entity-body:

        :param scope:   The scope of the access request as described by
                        `Section 3.3`_.
        :param kwargs:  Extra credentials to include in the token request.

        The client MUST authenticate with the authorization server as
        described in `Section 3.2.1`_.

        The prepared body will include all provided credentials as well as
        the ``grant_type`` parameter set to ``client_credentials``::

            >>> from oauthlib.oauth2 import BackendApplicationClient
            >>> client = BackendApplicationClient('your_id')
            >>> client.prepare_request_body(scope=['hello', 'world'])
            'grant_type=client_credentials&scope=hello+world'

        .. _`Appendix B`: http://tools.ietf.org/html/rfc6749#appendix-B
        .. _`Section 3.3`: http://tools.ietf.org/html/rfc6749#section-3.3
        .. _`Section 3.2.1`: http://tools.ietf.org/html/rfc6749#section-3.2.1
        """
        return prepare_token_request('client_credentials', body=body,
                                     scope=scope, **kwargs)
