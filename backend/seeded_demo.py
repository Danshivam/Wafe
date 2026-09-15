from app.database.database import (
    initialize_database,
    get_connection,
)


initialize_database()

connection = get_connection()

connection.execute(
    """
    INSERT OR IGNORE INTO incidents (
        id,
        session_id,
        call_id,
        status,
        reason,
        distress_detected,
        user_confirmed_danger
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """,
    (
        1,
        "walk_demo_001",
        "call_demo_001",
        "danger",
        "Demo user reported a fictional safety concern.",
        1,
        1,
    ),
)

connection.execute(
    """
    INSERT OR IGNORE INTO locations (
        session_id,
        latitude,
        longitude,
        accuracy
    )
    VALUES (?, ?, ?, ?)
    """,
    (
        "walk_demo_001",
        28.6139,
        77.2090,
        20.0,
    ),
)

connection.execute(
    """
    INSERT OR IGNORE INTO alerts (
        id,
        incident_id,
        session_id,
        status,
        message
    )
    VALUES (?, ?, ?, ?, ?)
    """,
    (
        1,
        1,
        "walk_demo_001",
        "new",
        "Fictional WAFE demo safety alert.",
    ),
)

connection.commit()
connection.close()

print("Fictional WAFE demo data seeded.")