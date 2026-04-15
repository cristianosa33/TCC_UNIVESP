-- Criação da tabela de demandas ambientais e de infraestrutura
CREATE TABLE IF NOT EXISTS demandas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria TEXT NOT NULL,           -- Ex: Arborização, Resíduos, Iluminação
    descricao TEXT,                    -- Detalhamento do problema
    latitude REAL NOT NULL,            -- Coordenada GPS
    longitude REAL NOT NULL,           -- Coordenada GPS
    foto_url TEXT,                     -- Caminho do arquivo da imagem
    criticidade TEXT DEFAULT 'Média',  -- Baixa, Média ou Alta
    status TEXT DEFAULT 'Pendente',    -- Pendente, Em Análise, Resolvido
    data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    data_atualizacao DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Inserção de dados de exemplo para teste inicial
INSERT INTO demandas (categoria, descricao, latitude, longitude, criticidade)
VALUES ('Arborização', 'Árvore com risco de queda', -23.5505, -46.6333, 'Alta');

INSERT INTO demandas (categoria, descricao, latitude, longitude, criticidade)
VALUES ('Resíduos', 'Descarte irregular de entulho', -23.5590, -46.6580, 'Média');
