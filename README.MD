# Hackertours Backoffice

Deployment repository for https://backoffice.hackertours.by.vincent.mahn.ke/.
Application source and image builds live in https://git.hanse.de/ViMaSter/hackertours-admin.
Compose pulls the pinned Forgejo image directly. The Dockerfile only mirrors that
same prebuilt image for the shared deployment workflow; it does not build application source.

The app uses PostgreSQL and a persistent media volume. It connects to the existing
handout/Gotenberg services over `handout-hackertours_default`.

The external Docker volume `backoffice-hackertours-secrets` must contain
`database_password`, `django_secret_key`, and `handout_passphrase`. Its directory
is owned by UID 1000 with mode 0700; secret files have mode 0400. Values are never
committed to this repository. PostgreSQL's root entrypoint reads its password file;
the app reads its files through `docker/entrypoint.py` before running migrations.

For management commands in Portainer's app-container console, use:

```sh
python /bootstrap/entrypoint.py manage.py createsuperuser
python /bootstrap/entrypoint.py manage.py import_event /tmp/event.zip
```

The operational test events are imported separately, not on each startup. Runtime
credentials and accounts are not included in event exports.