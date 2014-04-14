from .models import get_root

def includeme(config):
    config.set_root_factory(get_root)
    config.include('pyramid_chameleon')
    config.scan('.views')
