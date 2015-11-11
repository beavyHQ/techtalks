from beavy.common.rate_limits import rate_limit
from beavy.app import cache
from beavy.utils import api_only
from .blueprint import blueprint
from flask import request

@blueprint.route('extract')
@cache.memoize(15 * 60) # keep in cache for 15min
# @login_required
@rate_limit("1/second")
@api_only
def extract():
    url = request.args["url"]
    return {"url": url}
