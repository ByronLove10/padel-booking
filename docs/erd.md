# Entity Relationship Diagram (ERD)

User -> string role  // player | club_manager | admin
Timeslot -> string status // available | blocked
Booking -> string status // pending | paid | cancelled | expired


```mermaid
erDiagram

    User {
        int id PK
        string email
        string password_hash
        string role
        string name
        string phone
    }

    Club {
        int id PK
        string name
        string location
        string description
    }

    Court {
        int id PK
        int club_id FK
        string name
        string surface_type
        bool has_lights
        decimal price_per_hour
    }

    Timeslot {
        int id PK
        int court_id FK
        datetime start_time
        datetime end_time
        string status
    }

    Booking {
        int id PK
        int user_id FK
        int court_id FK
        int timeslot_id FK
        string status
        datetime created_at
    }

    Payment {
        int id PK
        int booking_id FK
        decimal amount
        string currency
        string provider
        string status
        datetime created_at
    }

    PricingRule {
        int id PK
        int club_id FK
        int day_of_week
        string time_range
        decimal price_override
    }

    AuditLog {
        int id PK
        int user_id FK
        string action
        json metadata
        datetime timestamp
    }

    %% Relationships
    User ||--o{ Booking : "makes"
    User ||--o{ AuditLog : "generates"

    Club ||--o{ Court : "has"
    Club ||--o{ PricingRule : "defines"

    Court ||--o{ Timeslot : "offers"
    Court ||--o{ Booking : "booked in"

    Timeslot ||--o{ Booking : "reserved in"

    Booking ||--|| Payment : "paid by"
