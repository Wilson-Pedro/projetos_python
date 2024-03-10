-- CRIAR BANCO DE DADOS
CREATE DATABASE escola;

-- CRIAR TABELAS
CREATE TABLE escola.tb_aluno(
	id SERIAL NOT NULL,
    nome VARCHAR(50),
    matricula VARCHAR(20) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    data_nascimento DATE NOT NULL,
    endereco VARCHAR(100) NOT NULL
);

CREATE TABLE escola.tb_professor(
	id SERIAL NOT NULL,
    nome VARCHAR(50),
    disciplina VARCHAR(20) NOT NULL,
    email VARCHAR(20) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    endereco VARCHAR(100) NOT NULL
);

SELECT * FROM escola.tb_aluno;
SELECT * FROM escola.tb_professor;

-- DELETAR TABELAS E BANCO DE DADOS
DROP TABLE escola.tb_aluno;
DROP TABLE escola.tb_professor;
DROP DATABASE escola;