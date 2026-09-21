# OnTrack

A live UK train tracker, inspired by FlightRadar24 — built to visualise real-time train movements across the UK rail network.

## Why

Unlike aircraft, UK trains don't broadcast GPS positions publicly. This project ingests Network Rail's real-time TRUST/TD data feeds, resolves each event to a real-world location, and (eventually) serves it as a live, interactive map.

## Status

Work in progress — currently in **Phase 3** of development.

- ✅ **Phase 1 — Ingest live train movements:** consuming Network Rail's STOMP feed and storing raw movement events in Postgres.
- ✅ **Phase 2 — Model the network:** imported CORPUS reference data to resolve location codes (STANOX) to real station/junction names.
- 🚧 **Phase 3 — Serve live state via API:** building a FastAPI service to expose train positions and history over REST/WebSocket.
- ⏳ **Phase 4 — Interpolate positions and render the map**
- ⏳ **Phase 5 — Add useful features** (search, filters, delay info)
- ⏳ **Phase 6 — ML delay prediction** (stretch goal)

## Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL + PostGIS (via Docker)
- **Live data:** Network Rail Open Data (STOMP feed), CORPUS/SMART reference data
- **Migrations:** Alembic
- **Frontend (planned):** React + Mapbox/Leaflet

## Running locally

```bash
docker compose up -d          # start Postgres + Adminer
alembic upgrade head          # apply migrations
python consumer.py            # start the STOMP consumer
```

Requires a Network Rail Open Data account and credentials set in `.env` (see `.env.example`).