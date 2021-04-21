import os
from ipythonblocks import BlockGrid, colors


def define_env(env):

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        path = env.variables.io_url + env.variables.page.url
        path = '/'.join([x for x in path.rstrip('/').split('/')[:-1]])+'/'+exo
        return f"""<iframe src="https://console.basthon.fr/?from={path}" width=100% height={hauteur}></iframe>"""

