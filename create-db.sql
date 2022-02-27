CREATE TABLE `accomodations`
(
 `AccomodationId` int NOT NULL AUTO_INCREMENT ,
 `hostId`         int NOT NULL ,
 `locationId`     int NOT NULL ,
 `startDate`      date NOT NULL ,
 `endDate`        date NOT NULL ,
 `capacity`       mediumint(5) NOT NULL ,
 `kidFriendly`    bit NOT NULL ,
 `petFriendly`    bit NOT NULL ,

PRIMARY KEY (`AccomodationId`),
KEY `FK_29` (`hostId`),
CONSTRAINT `FK_27` FOREIGN KEY `FK_29` (`hostId`) REFERENCES `host` (`HostId`),
KEY `FK_32` (`locationId`),
CONSTRAINT `FK_30` FOREIGN KEY `FK_32` (`locationId`) REFERENCES `location` (`LocationId`)
);

CREATE TABLE `host`
(
 `HostId`    int NOT NULL AUTO_INCREMENT ,
 `FirstName` varchar(45) NOT NULL ,
 `LastName`  varchar(45) NOT NULL ,
 `Email`     varchar(45) NOT NULL ,
 `Phone`     varchar(50) NOT NULL ,

PRIMARY KEY (`HostId`)
);

CREATE TABLE `location`
(
 `LocationId` int NOT NULL AUTO_INCREMENT ,
 `Street`     varchar(45) NOT NULL ,
 `Zip`        mediumint(5) NOT NULL ,
 `AptNumber`  varchar(10) NOT NULL ,
 `City`       varchar(50) NOT NULL ,
 `Additional` varchar(70) NOT NULL ,

PRIMARY KEY (`LocationId`)
);