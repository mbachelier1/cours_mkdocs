import os
from ipythonblocks import BlockGrid, colors

local_deployment = True


def define_env(env):
    @env.macro
    def basthon(exo: str, hauteur: int) -> str:
        path = env.variables.github + env.variables.page.url
        path = '/'.join([x for x in path.rstrip('/').split('/')[:-1]]) + '/' + exo
        return f"""<iframe src="https://console.basthon.fr/?from={path}" width=100% height={hauteur}></iframe>"""

    # TODO : fix pyf
    @env.macro
    def pyf(filename: str):
        """
        Displays the file as a python source code
        :param filename: str
        :return: None
        """
        if local_deployment:
            path = env.variables.local + env.variables.page.url
            path = path + 'scripts/' + filename + '.py'
            return """```python
--8<---  "{path}"
```"""
