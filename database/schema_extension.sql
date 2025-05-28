CREATE TABLE user_like (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    property_id INTEGER NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_user
        FOREIGN KEY (user_id)
        REFERENCES auth_user(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_property
        FOREIGN KEY (property_id)
        REFERENCES property(id)
        ON DELETE CASCADE
);
