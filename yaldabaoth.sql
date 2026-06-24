

CREATE DATABASE IF NOT EXISTS `almoxarifado`
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
USE `almoxarifado`;


SET SESSION sql_mode = 'STRICT_ALL_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO';



CREATE TABLE IF NOT EXISTS `usuarios` (
  `email` VARCHAR(100) NOT NULL,
  `nome` VARCHAR(100) NOT NULL,
  `senha` VARCHAR(255) NOT NULL, 
  `permissao` TINYINT UNSIGNED NOT NULL DEFAULT 0,
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE IF NOT EXISTS `estoque` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `nome` VARCHAR(100) NOT NULL,
  `quantidade` INT NOT NULL DEFAULT 0,
  `categoria` VARCHAR(50) NOT NULL,
  `descricao` VARCHAR(255),
  `preco` DECIMAL(10,2) DEFAULT NULL, 
  `imagem` VARCHAR(255) DEFAULT NULL, 
  `created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  INDEX (`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS `historico` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `usuario_email` VARCHAR(100) NOT NULL,
  `item_id` INT DEFAULT NULL,           
  `item_nome` VARCHAR(100) NOT NULL,    
  `quantidade` INT NOT NULL CHECK (`quantidade` > 0), 
  `movimento` ENUM('Entrada','Saída') NOT NULL,       
  `data_hora` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`usuario_email`) REFERENCES `usuarios` (`email`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`item_id`) REFERENCES `estoque` (`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


INSERT INTO `usuarios` (`email`, `nome`, `senha`, `permissao`)
VALUES
  ('admin@example.com', 'Administrator', '$2y$12$........................................', 10);

INSERT INTO `estoque` (`nome`, `quantidade`, `categoria`, `descricao`, `preco`, `imagem`)
VALUES
  ('Parafuso M4', 100, 'Fixadores', 'Parafuso hexagonal M4x10', 0.10, NULL);


INSERT INTO `historico` (`usuario_email`, `item_id`, `item_nome`, `quantidade`, `movimento`)
VALUES
