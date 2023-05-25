import functions_framework
from similarProducts import findSimilarItems


@functions_framework.http
def clothesSuggestions(request):
    request_json = request.get_json()
    description, limit = None, 10

    # load description
    if request.args and "description" in request.args:
        description = request.args.get("description")
    elif request_json and "description" in request_json:
        description = request_json["description"]

    # load limit(if exists)
    if request.args and "limit" in request.args:
        limit = request.args.get("limit")
    elif request_json and "limit" in request_json:
        limit = request_json["limit"]

    if not description:
        return "description not found", 404

    return findSimilarItems(description, limit), 200
