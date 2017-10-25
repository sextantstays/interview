DROP TABLE if EXISTS property;
DROP TABLE if EXISTS owner;

CREATE TABLE property (
    id TEXT PRIMARY KEY,
    ownerId TEXT NOT NULL,
    displayPictureUrl TEXT NOT NULL,
    address TEXT NOT NULL,
    type TEXT NOT NULL,
    bedrooms FLOAT NOT NULL,
    bathrooms FLOAT NOT NULL,
    state TEXT NOT NULL,
    city TEXT NOT NULL,
    totalRevenue FLOAT NOT NULL,
    occupancyRate FLOAT NOT NULL,
    description TEXT NOT NULL
);

CREATE TABLE owner (
    id TEXT PRIMARY KEY,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
);
