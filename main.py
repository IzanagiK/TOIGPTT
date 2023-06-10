import requests
import json
API_KEY = "ColocarKeyAqui"
text = open("test.txt")
headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"
body_tradu =  {
    "model": id_modelo,
    "messages": [{"role": "user", "content": f"Traduza o conteudo das chaves \'en\' para o português.{text.read()}"}]

}
body_tradu = json.dumps(body_tradu)

requisicao = requests.post(link, headers=headers, data=body_tradu)
resposta = requisicao.json()
mensagem = resposta["choices"][0]["message"]["content"]
print(mensagem)


#By PetryckSlater
