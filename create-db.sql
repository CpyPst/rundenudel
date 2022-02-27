CREATE TABLE `Accomodations`
(
 `AccomodationId` int NOT NULL AUTO_INCREMENT ,
 `HostId`         int NOT NULL ,
 `LocationId`     int NOT NULL ,
 `StartDate`      date NOT NULL ,
 `EndDate`        date NOT NULL ,
 `Capacity`       mediumint(5) NOT NULL ,
 `KidFriendly`    bit NOT NULL ,
 `PetFriendly`    bit NOT NULL ,

PRIMARY KEY (`AccomodationId`),
KEY `FK_29` (`hostId`),
CONSTRAINT `FK_27` FOREIGN KEY `FK_29` (`HostId`) REFERENCES `Hosts` (`HostId`),
KEY `FK_32` (`LocationId`),
CONSTRAINT `FK_30` FOREIGN KEY `FK_32` (`LocationId`) REFERENCES `Locations` (`LocationId`)
);

CREATE TABLE `Hosts`
(
 `HostId`    int NOT NULL AUTO_INCREMENT ,
 `FirstName` varchar(45) NOT NULL ,
 `LastName`  varchar(45) NOT NULL ,
 `Email`     varchar(45) NOT NULL ,
 `Phone`     varchar(50) NOT NULL ,

PRIMARY KEY (`HostId`)
);

CREATE TABLE `Locations`
(
 `LocationId` int NOT NULL AUTO_INCREMENT ,
 `Street`     varchar(45) NOT NULL ,
 `Zip`        char(5) NOT NULL ,
 `AptNumber`  varchar(10) NOT NULL ,
 `City`       varchar(50) NOT NULL ,
 `Additional` varchar(70) NOT NULL ,

PRIMARY KEY (`LocationId`)
);