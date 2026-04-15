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

# 🏙️ Sistema Georreferenciado de Gestão Ambiental e Urbana (TCC)

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)
![Universidade](https://img.shields.io/badge/Instituição-UNIVESP-blue?style=for-the-badge)
![Curso](https://img.shields.io/badge/Curso-Engenharia_de_Computação-orange?style=for-the-badge)

## 📝 Resumo do Projeto
Este projeto propõe o desenvolvimento de uma plataforma web georreferenciada para o registro e monitoramento de demandas ambientais e de infraestrutura no contexto urbano. A solução visa suprir lacunas na comunicação entre cidadãos e o poder público, permitindo a gestão eficiente de ocorrências como descarte irregular de resíduos e manejo de arborização urbana.

---

## 🎯 Objetivos
- **Cidadania Digital:** Permitir que o cidadão registre problemas em tempo real com fotos e localização automática.
- **Eficiência Pública:** Oferecer um painel de monitoramento (dashboard) para gestores visualizarem áreas críticas.
- **Cidades Inteligentes:** Aplicar conceitos de *Smart Cities* na estruturação e análise de dados urbanos.

---

## 🏗️ Estrutura do Repositório

| Pasta | Descrição |
| :--- | :--- |
| `📂 backend` | Servidor em Python (Flask), rotas de API e lógica de negócio. |
| `📂 frontend` | Interface do usuário, arquivos HTML e scripts do mapa (Leaflet). |
| `📂 database` | Scripts de criação do banco de dados (`.sql`) e backups. |
| `📂 docs` | Documentação teórica, manuais e referências bibliográficas. |
| `📂 static` | Arquivos de estilo (CSS), ícones e diretório de uploads de fotos. |
| `📂 images` | Imagens utilizadas na documentação e demonstração do sistema. |

---

## 🛠️ Stack Tecnológica

### **Frontend**
* **HTML5/CSS3:** Estrutura e estilização.
* **Leaflet.js:** Biblioteca open-source para mapas interativos.
* **OpenStreetMap:** Base de dados geográfica.

### **Backend**
* **Python 3.10+:** Linguagem principal.
* **Flask:** Micro-framework para gestão de rotas e servidor web.
* **SQLite/PostgreSQL:** Armazenamento de dados georreferenciados.

---

## 🚀 Como Executar o Projeto

Para rodar este projeto localmente, siga os passos abaixo:

### 1. Pré-requisitos
Certifique-se de ter o Python instalado em sua máquina.

### 2. Clonar o Repositório
```bash
git clone [https://github.com/SeuUsuario/TCC_UNIVESP.git](https://github.com/SeuUsuario/TCC_UNIVESP.git)
cd TCC_UNIVESP
