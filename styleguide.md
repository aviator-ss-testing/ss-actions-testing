# Engineering Style Guide

## Database access

All new database queries must use SQLAlchemy 2.0 syntax — `sa.select(...)`
rather than the legacy `session.query(...)`. Legacy call sites are updated
when touched.

## Logging

Every log call passes structured named fields rather than interpolated
strings. Exceptions are logged with `exc_info`, never stringified into the
message.

## Migrations

Migration files are never hand-written. They are generated, then edited if
a tweak is needed.
