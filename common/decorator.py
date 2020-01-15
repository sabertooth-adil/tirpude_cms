from django.shortcuts import redirect


def session_required(func):
    """
    Decorator to check the session is active or not for logged in user
    :param func: Name of function for which you have to check the session is active or not
    :return:
    """

    def wrap(request):
        """
        Wrapper function for the decorator
        :param request: request parameter for called URL
        :return:
        """
        if not request.session.get("user_id"):
            return redirect("/")
        func_return = func(request)
        return func_return

    return wrap
