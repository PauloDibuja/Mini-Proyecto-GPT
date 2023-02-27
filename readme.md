# Mini Proyecto GPT

Desarrollado por: PauloDibuja

Año: 2023

Versión: 1.0

	Nota: Creado únicamente por entretención del programador

## Requerimientos

Se necesita la biblioteca de OpenAI, usa el siguiente comando pip:

```pip
python -m pip install openai
```

## OpenAI API Key

Para tener una key de la API de OpenAI, debes ingresar a la página de la [Plataforma de OpenAI](platform.openai.com) y te creas una cuenta Personal.

Al entrar a la cuenta, te debe aparecer algo llamado "API Keys" y ahí puedes crear una key secreta. Lo copias y lo pegas en *"program_keys.py"*.

```python
api_key = "" 
```

## Ingresar Prompts

Para ingresar el prompts, existen dos formas:

1. Por Consola

2. Por Archivo


		Si vas a ingresar el prompt por archivo, escríbelo en el archivo "prompt.txt". Asegúrate de que ese archivo exista, porque si no es el caso el programa abortará el proceso.


## Generación de Texto

Para solicitar a la API que genere texto a partir de un prompt, se usa el siguiente código:

```python
def Generate_Text(prompt: str):
	request = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=1
	)
	return request["choices"][0]["text"]
```

Échale un vistazo a la [Documentación de la API de OpenAI](https://platform.openai.com/docs/introduction), más en específico en la sección de [Completions](https://platform.openai.com/docs/api-reference/completions)

Una vez enviado el prompt, se generará un resultado. Se podrá guardar de tres maneras posibles:

### 1) Por Consola

Solo se escribirá el resultado en la consola. (Apenas limpies la consola, se pierde el resultado)

### 2) Nuevo Archivo

Se guardará el resultado en un archivo de texto en la carpeta **"/results/"**

Podrás poner un nombre en consola, pero si dejas en blanco se guardará con el nombre por defecto **"default.txt"**

### 3) Sobreescribir Archivo Prompt

Se añadirá el resultado en texto en el archivo **"prompt.txt"** (Ideal para hacer generaciones de texto largas)

