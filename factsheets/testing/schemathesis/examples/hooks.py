import schemathesis

@schemathesis.hooks.register
def before_call(context, request):
    pass
