import os
from pathlib import Path
import subprocess
import sys
from urllib.parse import quote


def main():
    secrets = Path(os.environ.get("BACKOFFICE_SECRETS_DIR", "/run/backoffice-secrets"))
    os.environ["DJANGO_SECRET_KEY"] = (secrets / "django_secret_key").read_text().strip()
    os.environ["HANDOUT_PASSPHRASE"] = (secrets / "handout_passphrase").read_text().strip()
    password = quote((secrets / "database_password").read_text().strip(), safe="")
    os.environ["DATABASE_URL"] = f"postgres://backoffice:{password}@db:5432/backoffice"
    if sys.argv[1:]:
        os.execv(sys.executable, [sys.executable, *sys.argv[1:]])
    subprocess.run([sys.executable, "manage.py", "migrate", "--noinput"], check=True)
    os.execvp("gunicorn", [
        "gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000",
        "--workers", "3", "--timeout", "180",
    ])


if __name__ == "__main__":
    main()