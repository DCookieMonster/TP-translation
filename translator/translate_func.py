__author__ = 'dor'

# import functools
# import requests
# import re
# import json
import RegexTxt
# from requests import Request, Session
# from requests.adapters import HTTPAdapter
import logging
import goslate
logger = logging.getLogger(__name__)

# __all__ = ['push_url', 'translator']
#
# def push_url(interface):
#     '''
#     Decorates a function returning the url of translation API.
#     Creates and maintains HTTP connection state
#
#     Returns a dict response object from the server containing the translated
#     text and metadata of the request body
#
#     :param interface: Callable Request Interface
#     :type interface: Function
#     '''
#
#     @functools.wraps(interface)
#     def connection(*args, **kwargs):
#         """
#         Extends and wraps a HTTP interface.
#
#         :return: Response Content
#         :rtype: Dictionary
#         """
#         session = Session()
#         session.mount('http://',  HTTPAdapter(max_retries=2))
#         session.mount('https://', HTTPAdapter(max_retries=2))
#
#         request  = Request(**interface(*args, **kwargs))
#         prepare  = session.prepare_request(request)
#         response = session.send(prepare, verify=True)
#
#         if response.status_code != requests.codes.ok:
#             response.raise_for_status()
#
#         cleanup = re.subn(r',(?=,)', '', response.content.decode('utf-8'))[0]
#
#         return json.loads(cleanup.replace(r'\xA0', r' ').replace('[,', '[1,'), encoding='UTF-8')
#
#     return connection
#
# @push_url
# def translator(source, target, phrase, version='0.0 test', charset='utf-8'):
#     # """
#     # Returns the url encoded string that will be pushed to the translation
#     # server for parsing.
#     #
#     # List of acceptable language codes for source and target languages
#     # can be found as a JSON file in the etc directory.
#     #
#     # Some source languages are limited in scope of the possible target languages
#     # that are available.
#     #
#     # .. code-block:: python
#     #
#     #     >>> from translate import translator
#     #     >>> translator('en', 'zh-TW', 'Hello World!')
#     #
#     # :param source: Language code for translation source
#     # :type source: String
#     #
#     # :param target: Language code that source will be translate into
#     # :type target: String
#     #
#     # :param phrase: Text body string that will be url encoded and translated
#     # :type phrase: String
#     #
#     # :return: Request Interface
#     # :rtype: Dictionary
#     # """
#
#     url     = 'https://translate.google.com/translate_a/single'
#     agent   = 'User-Agent',   'py-translate v{}'.format(version)
#     content = 'Content-Type', 'application/json; charset={}'.format(charset)
#
#     params  = {'client': 'a', 'ie': charset, 'oe': charset,
#                    'dt': 't', 'sl':  source, 'tl':  target,  'q': phrase}
#
#     request = {'method': 'GET',
#                   'url': url,
#                'params': params,
#               'headers': dict([agent, content])}
#
#     return request

def translate_text(txt, source="en", target="iw"):
    try:
        gs = goslate.Goslate()
        translate = gs.translate(txt,target,source)
        logger.info("translate: "+str(translate.__len__()))
        # translate_dict = []
        return RegexTxt.ReverseTxt(translate)
    except:
        return ""


