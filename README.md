# PyConEs 2021: Documenta sin ser un escriba

- [PyConEs 2021: Documenta sin ser un escriba](#pycones-2021-documenta-sin-ser-un-escriba)
  - [Setup](#setup)
  - [Generando documentación consistente](#generando-documentación-consistente)
    - [¿Cuando efectúo estos chequeos?](#cuando-efectúo-estos-chequeos)
  - [Construyendo la documentación](#construyendo-la-documentación)

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

### ¿Cuando efectúo estos chequeos?

Tienes muchas opciones para efectuar las comprobaciones anteriores sobre tu código, pero aqui te dejo un par de ideas:

- En el ciclo de Integración continua, ejecuta el comando de arriba para verificarlo. O mucho mejor,
- Usando la herramienta [pre-commit](https://pre-commit.com/) que ejecute el chequeo antes de comitear cambios en tu rama. Tienes una configuracion para pre-commit en este mismo repositorio.

```sh
> pre-commit install
pre-commit installed at .git/hooks/pre-commit
```

Cuando los hooks esten instalados, al hacer commit o push verás algo como esto

```sh
> git commit -m "Added a new awesome change"
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /home/japizarro/.cache/pre-commit/patch1632760228-11911.
Trim Trailing Whitespace.................................................Passed
Fix End of Files.........................................................Passed
Check Yaml...............................................................Passed
Check for added large files..............................................Passed
flake8...................................................................Passed
```

## Construyendo la documentación

Cuando alguno de los comandos anteriores falle, arregla lo que sea necesario. Una vez este listo, genera la documentación con el siguiente comando:

```sh
make -C docs html
```

Y tendrás el _site_ html con la documentación de esta estupenda calculadora en `docs/build/html` ;)

[darglint]: https://pypi.org/project/darglint/
[flake8]: https://gitlab.com/pycqa/flake8
[sphinx]: https://www.sphinx-doc.org/en/master/
[poetry]: https://python-poetry.org/
[pep8]: https://www.python.org/dev/peps/pep-0008/
