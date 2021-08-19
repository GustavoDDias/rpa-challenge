CREATE DATABASE `db_rpa`;

USE `db_rpa`;

CREATE TABLE `db_rpa`.`pessoa` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(300) NULL,
  `Cidade` VARCHAR(300) NULL,
  `Estado` VARCHAR(150) NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `db_rpa`.`contato` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Pessoa_Id` INT NULL,
  `Email` VARCHAR(150) NULL,
  `DDD` VARCHAR(3) NULL,
  `Telefone` VARCHAR(15) NULL,
  PRIMARY KEY (`Id`));

CREATE TABLE `db_rpa`.`statusmensagemenviada` (
  `Id` INT NOT NULL AUTO_INCREMENT,
  `Pessoa_Id` INT NULL,
  `Contato_Id` INT NULL,
  `Assunto` VARCHAR(100) NULL,
  `MensagemEnviada` VARCHAR(255) NULL,
  `RetornoSite` VARCHAR(255) NULL,
  PRIMARY KEY (`Id`));