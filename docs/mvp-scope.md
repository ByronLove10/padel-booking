# MVP Scope and Acceptance Criteria

## ✅ In Scope (MVP features)

1. **Users & Roles**
   - Register / login with email + password.
   - Roles: `player`, `club_manager`, `admin`.

2. **Clubs & Courts**
   - Browse list of clubs and their courts.
   - CRUD operations for Club and Court (only for managers/admins).

3. **Availability & Bookings**
   - Generate configurable timeslots (60/90/120 minutes).
   - Display availability in a calendar view.
   - Create and cancel bookings.
   - Prevent overbooking with atomic operations (DB + Redis locks).

4. **Payments (Basic)**
   - Stripe Checkout integration.
   - Booking states: `PENDING → PAID / CANCELLED`.
   - Basic refunds (manual).

5. **Notifications**
   - Email confirmation and cancellation.
   - Reminder email before the match.

6. **Club Panel (Minimal)**
   - View court occupancy calendar.
   - Block courts for maintenance.

---

## 🚫 Out of Scope (for later phases)

- Mobile app / PWA.  
- Matchmaking between single players.  
- Subscriptions / prepaid credits.  
- Waiting lists.  
- Advanced reporting and dashboards.  
- Multi-currency or discount systems.  
- IoT integration (smart locks, gates, etc).

---

## 🎯 Acceptance Criteria

- A player can register and book an available court successfully.  
- The system prevents **double-booking** (two players cannot reserve the same court at the same time).  
- A successful Stripe payment moves a booking from `PENDING` to `PAID`.  
- Cancelling a booking frees the timeslot.  
- A club manager can:  
  - Create a club and courts.  
  - Block a court for maintenance.  
- Confirmation and reminder emails are delivered.  
- The whole flow works in **staging** with seeded demo data.

---
