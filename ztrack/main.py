"""
Rockstat Zadarma service
(c) Dmitry Rodin 2018
"""
from band import expose, logger, response, rpc, settings

START_EVENT = 'NOTIFY_START'
CTRACK = 'ctrack'
USER_BY_PHONE = 'user_by_phone'


@expose.handler()
async def main(key, data, **params):
    """
    Handle zadarma validation webhook
    """
    logger.info('request', data=data, key=key)
    zd_echo = data.pop('zd_echo', None)
    if zd_echo:
        return response.data(zd_echo)
    return {}


@expose.enricher(props=settings.props, keys=settings.use_keys)
async def enrich(key, **params):
    """
    Handle incoming calls
    """
    if key in settings.use_keys:
        phone = params.pop('phone')
        event = params.pop('event')
        if phone and event and event == START_EVENT:
            user = await rpc.request(CTRACK, USER_BY_PHONE, phone=phone)
            if user:
                logger.info('user', u=user)
                uid = user.get('uid', None)
                sess_no = user.get('sess_no', None)
                if uid:
                    return {'uid': str(uid), 'sess_no': sess_no}
    return {}
