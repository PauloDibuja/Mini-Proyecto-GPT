import openai
import program_keys
import os

openai.api_key = program_keys.api_key

def Separating_Line():
	print("--------------------------------------")

# Obtener prompt desde consola
def Input_Prompt():
	prompt_text = ""
	while(prompt_text == ""):
		prompt_text = input("Ingrese el prompt: ")
	return prompt_text

# Obtener prompt desde el archivo "prompt.txt"
def File_Prompt():
	try:
		input_file = open("prompt.txt", "r", encoding="utf-8")
	except FileNotFoundError:
		return FileNotFoundError
	text_all = input_file.read()
	return text_all

# Función general para obtener prompt
def Prompt():
	selector = -1
	ans_selector = ""
	Separating_Line()
	while(selector not in range(0,2)):
		print("¿Qué tipo de prompt usarás?\n")
		print("0 - Por Comando")
		print("1 - Por Archivo")
		ans_selector = input("\n>> ")
		if(ans_selector.isnumeric() == True):
			selector = int(ans_selector)
	Separating_Line()
	if(selector == 0):
		return Input_Prompt()
	else:
		return File_Prompt()

# Consultar el tipo de salida del resultado de la generación
def Type_Saving():
	selector = -1
	ans_selector = ""
	while(selector not in range(0,3)):
		print("¿Cómo guardarás/escribir el resultado?\n")
		print("0 - Escribirlo en Consola")
		print("1 - Nuevo Archivo")
		print("2 - Sobreescribir Archivo Prompt")
		ans_selector = input("\n>> ")
		if(ans_selector.isnumeric() == True):
			selector = int(ans_selector)
	Separating_Line()
	return selector

# Guardar el resultado de la generación en un nuevo archivo de texto
def Save_New_File(generated_text: str):
	print("\nResultado Generado\n")
	print("Escriba el nombre del archivo en la que quiere guardar el resultado.")
	print("Presione Enter si quiere guardarlo en el archivo por defecto (default.txt)")
	filename = input(">>> ")
	if(filename == ""):
		filename = "default"
	if(filename.count(".") > 0):
		filename = filename.split(".")[0]
	output = open("results/{}.txt".format(filename), "w", encoding="utf-8")
	output.write("{}".format(generated_text))
	output.close()

# Sobreescribiendo el archivo de prompt
def Save_Prompt_File(generated_text: str):
	output_file = open("prompt.txt", "a", encoding="utf-8")
	output_file.write(generated_text)
	output_file.close()
	print("Guardando en prompt.txt")

# Imprimir en consola el resultado de la generación
def Print_Result(generated_text: str):
	text_to_print = """
	Resultado generado

	{}
	
	""".format(generated_text)

	print(text_to_print)

# Procedimiento general para la salida del resultado de la generación
def Save_Result(generated_text: str):
	Separating_Line()
	print("Texto Generado!\n")
	selector = Type_Saving()
	if(selector == 0):
		Print_Result(generated_text)
	elif(selector == 1):
		Save_New_File(generated_text)
	elif(selector == 2):
		Save_Prompt_File(generated_text)
	Separating_Line()

# Hacer la solicitud a la API para generar texto a través de un prompt
def Generate_Text(prompt: str):
	print("Generando Resultado...")
	request = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prompt,
		max_tokens=1024,
		n=1,
		stop=None,
		temperature=1
	)
	return request["choices"][0]["text"]

# Proceso General GPT
def GPT_Process():
	prompt = Prompt()
	if prompt != FileNotFoundError:
		generated_text = Generate_Text(prompt)
		Save_Result(generated_text)
	else:
		print("Error: No existe el archivo de Prompt")
		print("Descripción: Agrega el archivo 'prompt.txt'")
		Separating_Line()

# Consultar si realizar otro proceso GPT
def Will_Repeat():
	respuesta = ""
	options = ["si", "no"]
	while(respuesta not in options):
		print("\n¿Quieres ingresar un nuevo prompt?\n")
		respuesta = input("(Si o No) >>> ")
		respuesta = respuesta.lower()
	return respuesta == "si" 

if __name__ == "__main__":
	os.system("cls")
	repeat = True
	while repeat == True:
		GPT_Process()
		repeat = Will_Repeat()
	Separating_Line()
	print("\nGracias por usar el programa :D\n")