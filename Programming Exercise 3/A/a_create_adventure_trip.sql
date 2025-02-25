-- (a) Create the ADVENTURE_TRIP Table
CREATE TABLE ADVENTURE_TRIP (
    TRIP_ID DECIMAL(3,0) PRIMARY KEY,
    TRIP_NAME VARCHAR(75),
    START_LOCATION CHAR(50),
    STATE CHAR(2),
    DISTANCE NUMBER(4,0),
    MAX_GRP_SIZE NUMBER(4,0),
    TYPE CHAR(20),
    SEASON CHAR(20)
);