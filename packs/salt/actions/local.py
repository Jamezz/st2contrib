import json
from requests import Session

from lib.base import SaltAction


class SaltLocal(SaltAction):

    def run(self, module, target, **kwargs):
        '''
        CLI Examples:

            st2 run salt.runner matches='web*' module=test.ping
            st2 run salt.client module=pkg.install \
                    kwargs='{"pkgs":["git","httpd"]}'
        '''
        # TODO: This is broken, fix it. I temporary disabled it to avoid pylint
        # failure.
        # Also "args" and "kwargs" action parameters are unused?
        # self.generate_package(cmd=cmd)
        _cmd = module
        self.generate_package('local', cmd=_cmd)
        if kwargs['kwargs'] is not None:
            self.data.update(arg['arg'])
        if target is not None:
        	target = target.replace('http://','')
        	self.data['tgt'] = target

        request = self.generate_request()
        request.prepare_body(json.dumps(self.data), None)
        resp = Session().send(request, verify=True)
        return resp.json()
