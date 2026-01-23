-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               12.1.1-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             12.11.0.7065
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for videothek
CREATE DATABASE IF NOT EXISTS `videothek` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_uca1400_ai_ci */;
USE `videothek`;

-- Dumping structure for table videothek.ausleihe
CREATE TABLE IF NOT EXISTS `ausleihe` (
  `Ausleihe_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Ausleihdatum` date DEFAULT curdate(),
  `Rückgabedatum` date DEFAULT NULL,
  `Kunde_ID` int(11) DEFAULT NULL,
  `Film_ID` int(11) DEFAULT NULL,
  `Mitarbeiter_ID` int(11) DEFAULT NULL,
  KEY `Index 1` (`Ausleihe_ID`),
  KEY `Kunde_ID` (`Kunde_ID`),
  KEY `Film_ID` (`Film_ID`),
  KEY `Mitarbeiter_ID` (`Mitarbeiter_ID`),
  CONSTRAINT `Film_ID` FOREIGN KEY (`Film_ID`) REFERENCES `film` (`Film_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `Kunde_ID` FOREIGN KEY (`Kunde_ID`) REFERENCES `kunde` (`Kunde_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `Mitarbeiter_ID` FOREIGN KEY (`Mitarbeiter_ID`) REFERENCES `mitarbeiter` (`Mitarbeiter_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `Rückgabe_größer_Ausleihe` CHECK (`Rückgabedatum` > `Ausleihdatum`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table videothek.ausleihe: ~10 rows (approximately)
DELETE FROM `ausleihe`;
INSERT INTO `ausleihe` (`Ausleihe_ID`, `Ausleihdatum`, `Rückgabedatum`, `Kunde_ID`, `Film_ID`, `Mitarbeiter_ID`) VALUES
	(1, '2025-01-03', '2025-01-10', 1, 6, 9),
	(2, '2025-01-05', '2025-01-12', 7, 18, 1),
	(3, '2025-01-08', '2025-01-15', 8, 11, 4),
	(4, '2025-01-11', '2025-01-18', 13, 6, 3),
	(5, '2025-01-13', '2025-01-20', 11, 14, 7),
	(6, '2025-01-15', '2025-01-22', 9, 19, 2),
	(7, '2025-01-18', '2025-01-25', 1, 8, 6),
	(8, '2025-01-20', '2025-01-27', 3, 16, 5),
	(9, '2023-01-22', NULL, 5, 17, 8),
	(10, '2025-01-18', NULL, 10, 15, 10);

-- Dumping structure for table videothek.film
CREATE TABLE IF NOT EXISTS `film` (
  `Film_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Titel` varchar(50) DEFAULT NULL,
  `Erscheinungsjahr` int(11) DEFAULT NULL,
  `Genre` varchar(50) DEFAULT NULL,
  `Altersfreigabe` varchar(50) DEFAULT NULL,
  KEY `Index 1` (`Film_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table videothek.film: ~20 rows (approximately)
DELETE FROM `film`;
INSERT INTO `film` (`Film_ID`, `Titel`, `Erscheinungsjahr`, `Genre`, `Altersfreigabe`) VALUES
	(1, 'The Matrix', 1999, 'Science-Fiction', 'USK16'),
	(2, 'Inception', 2010, 'Science-Fiction', 'USK12'),
	(3, 'The Godfather', 1972, 'Drama', 'USK16'),
	(4, 'The Dark Knight', 2008, 'Action', 'USK12'),
	(5, 'Pulp Fiction', 1994, 'Crime', 'USK16'),
	(6, 'Forrest Gump', 1994, 'Drama', 'USK12'),
	(7, 'Gladiator', 2000, 'Action', 'USK16'),
	(8, 'Interstellar', 2014, 'Science-Fiction', 'USK12'),
	(9, 'The Shawshank Redemption', 1994, 'Drama', 'USK12'),
	(10, 'Joker', 2019, 'Thriller', 'USK16'),
	(11, 'Avengers: Endgame', 2019, 'Action', 'USK12'),
	(12, 'Parasite', 2019, 'Thriller', 'USK16'),
	(13, 'Titanic', 1997, 'Romance', 'USK12'),
	(14, 'Mad Max: Fury Road', 2015, 'Action', 'USK16'),
	(15, 'Toy Story', 1995, 'Animation', 'USK0'),
	(16, 'Alien', 1979, 'Horror', 'USK16'),
	(17, 'The Lion King', 1994, 'Animation', 'USK0'),
	(18, 'Fight Club', 1999, 'Drama', 'USK18'),
	(19, 'Jurassic Park', 1993, 'Adventure', 'USK12'),
	(20, 'The Wolf of Wall Street', 2013, 'Drama', 'USK18');

-- Dumping structure for table videothek.kunde
CREATE TABLE IF NOT EXISTS `kunde` (
  `Kunde_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Vorname` varchar(50) DEFAULT NULL,
  `Nachname` varchar(50) DEFAULT NULL,
  `Geburtstag` date DEFAULT NULL,
  `Straße_Nr` varchar(50) DEFAULT NULL,
  `PLZ` varchar(5) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  KEY `Index 1` (`Kunde_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table videothek.kunde: ~15 rows (approximately)
DELETE FROM `kunde`;
INSERT INTO `kunde` (`Kunde_ID`, `Vorname`, `Nachname`, `Geburtstag`, `Straße_Nr`, `PLZ`, `City`) VALUES
	(1, 'Sir-Lacht-viel', 'Wackelknie', '1985-04-12', 'Bananenallee 7', '12345', 'Quatschstadt'),
	(2, 'Frau-Krawall', 'Suppenkasper', '1978-11-03', 'Bratwurstweg 42', '54321', 'Knödelhausen'),
	(3, 'Captain Chaos', 'Chaosmeister', '1996-07-19', 'Pixelgasse 13', '10101', 'Nerdorf'),
	(4, 'Zappel-Zenzi', 'Zappelphilipp', '1982-02-28', 'Hampelmannstr. 5', '22222', 'Wackingen'),
	(5, 'Bierchen-Bert', 'Bierbauch', '1970-09-09', 'Hopfenring 99', '06666', 'Prostheim'),
	(6, 'Drama-Lama', 'Dramaqueen', '2001-06-21', 'Selfiestieg 1', '07777', 'Influenzia'),
	(7, 'Keksinator', 'Pustekuchen', '1965-01-15', 'Zuckergussweg 8', '88888', 'Kuchendorf'),
	(8, 'Glitzer-Gabi', 'Glitzerstern', '1994-12-04', 'Regenbogenallee 3', '99999', 'Funkelstadt'),
	(9, 'Snoozy-Siggi', 'Schlafmütze', '1988-03-30', 'Kissenweg 11', '11111', 'Snoozingen'),
	(10, 'Klugschlau-Karo', 'Besserwisserin', '1976-08-17', 'Klugscheißerplatz 6', '33333', 'Denkstadt'),
	(11, 'Turbo-Timmy', 'Rennsemmel', '1992-05-05', 'Überholspur 21', '44444', 'Turboheim'),
	(12, 'Staubi-Susi', 'Staubsauger', '1959-10-22', 'Saubermannweg 4', '05555', 'Putzdorf'),
	(13, 'Tick-Tack-Toni', 'TickTack', '2003-01-01', 'Uhrenstraße 12', '12121', 'Sekundingen'),
	(14, 'Morgenmuffel-Mia', 'Montagsmuffel', '1980-02-11', 'Kaffeeweg 9', '23232', 'Müdorf'),
	(15, 'Panik-Paule', 'Fahrstuhlphobie', '1974-06-06', 'Treppenstieg 99', '34343', 'Höhenangst');

-- Dumping structure for table videothek.mitarbeiter
CREATE TABLE IF NOT EXISTS `mitarbeiter` (
  `Mitarbeiter_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Vorname` varchar(50) DEFAULT NULL,
  `Nachname` varchar(50) DEFAULT NULL,
  KEY `Index 1` (`Mitarbeiter_ID`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_uca1400_ai_ci;

-- Dumping data for table videothek.mitarbeiter: ~10 rows (approximately)
DELETE FROM `mitarbeiter`;
INSERT INTO `mitarbeiter` (`Mitarbeiter_ID`, `Vorname`, `Nachname`) VALUES
	(1, 'Anna', 'Alleswisser'),
	(2, 'Markus', 'Müller'),
	(3, 'Excel-Emil', 'Weber'),
	(4, 'Daniel', 'Fischer'),
	(5, 'Sophie', 'Becker'),
	(6, 'Thomas', 'Hoffmann'),
	(7, 'Julia', 'Koch'),
	(8, 'Michael', 'Bauer'),
	(9, 'Nina', 'Richter'),
	(10, 'Sebastian', 'Klein');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
