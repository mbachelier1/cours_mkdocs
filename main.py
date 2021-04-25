import os
from ipythonblocks import BlockGrid, colors

local_deployment = True


def define_env(env):
    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        path = env.variables.github + env.variables.page.url
        path = '/'.join([x for x in path.rstrip('/').split('/')[:-1]]) + '/' + exo
        return f"""<iframe src="https://console.basthon.fr/?from={path}" width=100% height={hauteur}></iframe>"""

    @env.macro
    def script(lang: str, nom: str) -> str:
        return f"""```{lang}
--8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
```"""

    @env.macro
    def script_admo(lang: str, nom: str) -> str:
        return f"""```{lang}
    --8<---  "docs/""" + os.path.dirname(env.variables.page.url.rstrip('/')) + f"""/{nom}"
    ```"""

    @env.macro
    def py_admo(nom: str) -> str:
        return script_admo('python', "scripts/" + nom + ".py")

    @env.macro
    def pyl(expression :str)->str:
        return f"""`#!python {expression}`"""