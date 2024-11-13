create table registry(
    id NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    k number,
    p number,
    ldr number,
    humidity number,
    temperature number,
    relay varchar(5),
    data date not null
);
