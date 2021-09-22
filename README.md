# PyConEs 2021: Documenta sin ser un escriba

Este repo contiene un pequeño ejemplo acerca de como mantener un API documentada siempre consistente con el código fuente.

Para ello hace uso de las siguientes herramientas:

- [darglint][darglint] como herramienta de validación de los docstrings

De manera adicional, se hace uso de las siguientes herramientas para la validación y generación de la documentación

- [flake8][flake8] como herramienta de analisis estático de código. darglint funciona de forma aislada o como plugin de flake8
- [Sphinx][sphinx] como motor de documentación.

## Setup

El repo se basa en un proyecto [Poetry][poetry] que te permite trabajar en un entorno virtual de forma sencilla. Para ello, simplemente ejecuta este comando para empezar a probar

```sh
poetry install
```

Ese comando te creará un entorno virtual, te lo activará y a continuación te instalará las dependencias.

Si quieres hacer un setup sin poetry, la manera más sencilla de probar este repo sería instalarte las dependencias después de crearte un entorno virtual. Algo así como:

```sh
pip install darglint flake8 sphinx
```

## Generando documentación consistente

El módulo `calc` contiene un submodulo dummy el cual implementa cuatro operaciones aritméticas: suma, resta, multiplicación y división. Pero aquí lo de menos es la funcionalidad, sino cómo la documentamos.

Prueba a modificar los docstrings, los parámetros, lo que quieras. Liala parda. Y cuando quieras, ejecuta este comando:

```sh
darglint calc
```

O si quieres validar los docstrings junto con las guidelines del [PEP8][pep8], usa directamente flake8

```sh
flake8 calc
```

Cuando alguno de los comandos anteriores falle, arregla lo que sea necesario. Una vez este listo, genera la documentación con el siguiente comando:

```sh
make -C docs html
```

Y tendrás el _site_ html con la documentación de esta estupenda calculadora ;)

[darglint]: https://pypi.org/project/darglint/
[flake8]: https://gitlab.com/pycqa/flake8
[sphinx]: https://www.sphinx-doc.org/en/master/
[poetry]: https://python-poetry.org/
[pep8]: https://www.python.org/dev/peps/pep-0008/
