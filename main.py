import os
from ipythonblocks import BlockGrid, colors


def define_env(env):
    "Hook function"

    @env.macro
    def basthon(exo: str, hauteur: int) -> str:

        "Renvoie du HTML pour embarquer un fichier `exo` dans Basthon"
        path = env.variables.io_url + env.variables.page.url
        path = '/'.join([x for x in path.rstrip('/').split('/')[:-1]])+'/'+exo
        return f"""**dir :** {os.getcwd()}
        
        **env.variables.io_url :** {env.variables.io_url}
        
        **env.variables.page.url : ** {env.variables.page.url}
        
        <iframe src="https://console.basthon.fr/?from={path}" width=100% height={hauteur}></iframe>"""
