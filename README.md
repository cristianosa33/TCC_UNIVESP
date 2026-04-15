Plataforma Web de Monitoramento Ambiental Urbano - TCC UNIVESP
Este projeto consiste em uma plataforma georreferenciada para o registro e monitoramento de demandas ambientais e de infraestrutura urbana. O objetivo é facilitar a comunicação entre cidadãos e a gestão pública através de dados precisos e visualização em mapas.

🚀 Funcionalidades Principais
Mapeamento Interativo: Visualização de ocorrências (descarte de resíduos, poda de árvores, falhas na via) em tempo real.

Registro Geolocalizado: Captura automática de coordenadas (Latitude e Longitude) via GPS do navegador.

Gestão de Dados: Organização por níveis de criticidade e categorias.

Painel Administrativo: Interface para suporte à tomada de decisão baseada em evidências.

📂 Estrutura do Repositório
/frontend: Contém o index.html e arquivos de interface (Leaflet.js para o mapa).

/backend: Lógica do servidor em Python (Flask) e processamento de rotas.

/database: Modelagem e scripts SQL para armazenamento das ocorrências.

/static: Arquivos estáticos (CSS, imagens de ícones e fotos das ocorrências).

🛠️ Tecnologias Utilizadas
Linguagem: Python 3.x

Framework Web: Flask

Mapa: Leaflet.js / OpenStreetMap

Banco de Dados: SQLite (Protótipo)

Análise de Dados: Pandas / Plotly (Futuro)

📖 Como Rodar o Projeto (Guia para o Grupo)
Certifique-se de ter o Python instalado.

Instale as dependências necessárias:

Bash
pip install flask
Acesse a pasta do projeto e execute o servidor:

Bash
python backend/app.py
Abra o navegador no endereço: http://127.0.0.1:5000

