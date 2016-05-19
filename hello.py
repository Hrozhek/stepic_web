#!/usr/bin/env python 
def wsgi_application(environ, start_response):
    body = ''
    for get_request in environ[QUERY_STRING].split('&'):
        body += (get_request + '\n')
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]
    start_response(status, headers )
    return [body]
