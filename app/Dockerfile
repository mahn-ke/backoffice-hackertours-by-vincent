FROM git.hanse.de/vimaster/hackertours-admin@sha256:31f9f9bf3e46ebcd92047c3e2375ee644a1f911717e8c9907b72847f6b3752ea AS runtime
COPY entrypoint.py /bootstrap/entrypoint.py
ENTRYPOINT ["python", "/bootstrap/entrypoint.py"]
CMD []

FROM runtime AS test
RUN python -c "compile(open('/bootstrap/entrypoint.py').read(), '/bootstrap/entrypoint.py', 'exec')"

FROM runtime AS final
