import logging

from flask import current_app
import jinja2
import flask

logger = logging.getLogger(__name__)

class AngularInjection(object):

    def __init__(self,app=None):
        self.app = app
        self.init_app(app)
        self.data = dict(request_args={},view_args={},data={})

    def init_app(self,app):
        app.config.setdefault('ANGULARJS_VERSION','1.5')
        app.context_processor(self.renderer)
        def inject_context(c):
            return c
        self.app.jinja_env.globals['inject_context'] = jinja2.contextfunction(inject_context)
        self.global_keys = self.app.jinja_env.globals.keys()



    def renderer(self):
        request = flask.request
        self.data['request_args'] = dict(request.args)
        # Inject route arguments
        self.data['view_args'] = dict(request.view_args)

        def angular_injection_renderer(context):
            for (key,value) in context.items():
                if key not in self.global_keys and hasattr(value,'__call__')==False:
                    self.data['data'][key] = value
            import json
            template_string = """
            <script type="text/javascript">
              angular.module('flask_injection',[])
                      .value('$flask',{{ js_string }})
            </script>
            """


            template = jinja2.Template(template_string)
            return template.render(js_string=json.dumps(self.data))
        return dict(angular_injection_renderer=angular_injection_renderer)