import json
from jinja2 import Environment, FileSystemLoader
from models.pessoa import Pessoa

def carregar_dados(caminho_json):
    with open(caminho_json, "r", encoding="utf-8") as file:
        return json.load(file)

def criar_pessoa(dados_json):
    return Pessoa(
        nome=dados_json["nome"],
        email=dados_json["email"],
        telefone=dados_json["telefone"],
        resumo=dados_json["resumo"],
        habilidades=dados_json["habilidades"],
        experiencias=dados_json["experiencias"]
    )

def gerar_curriculo_html(pessoa, template_path="templates", template_name="curriculo.html", output_file="curriculo_gerado.html"):
    env = Environment(loader=FileSystemLoader(template_path))
    template = env.get_template(template_name)
    html_renderizado = template.render(pessoa=pessoa)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(html_renderizado)

    print(f"✅ Currículo gerado com sucesso: {output_file}")

if __name__ == "__main__":
    dados = carregar_dados("dados/dados.json")
    pessoa = criar_pessoa(dados)
    gerar_curriculo_html(pessoa)
