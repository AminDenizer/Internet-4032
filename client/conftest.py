import pytest
import subprocess
import time
import os

@pytest.fixture(scope="session", autouse=True)
def manage_servers(request):
    """
    A session-scoped fixture to manage the lifecycle of the Docker containers.
    """
    # Start servers
    subprocess.run(["sudo", "docker", "compose", "up", "-d", "--build"], check=True)

    # Wait for servers to be ready. This is a simple approach.
    # A more robust solution might involve polling the ports.
    time.sleep(5)

    yield

    # Stop servers
    subprocess.run(["sudo", "docker", "compose", "down"], check=True)
