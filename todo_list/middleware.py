from channels.db import database_sync_to_async


@database_sync_to_async
def get_user(token):
    from rest_framework.authtoken.models import Token
    from django.contrib.auth.models import AnonymousUser

    try:
        return Token.objects.get(key=token).user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        from django.contrib.auth.models import AnonymousUser

        headers = dict(scope["headers"])
        auth_header = headers.get(b"authorization", b"token invalid")

        token_str = auth_header.decode("utf-8")

        key, token = token_str.split(" ")
        if key.lower() == "token":
            scope["user"] = await get_user(token)
        else:
            scope["user"] = AnonymousUser()

        return await self.app(scope, receive, send)
