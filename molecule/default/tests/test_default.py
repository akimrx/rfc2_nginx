
def test_nginx(host):
    """Checking the installation and operation of the NTP service."""
    nginx = host.package("nginx")
    nginx_service = host.service("nginx")
    assert nginx.is_installed, "NGINX is not installed"
    assert nginx_service.is_running, "NGINX service is not running"
    assert nginx_service.is_enabled, "NGINX service is not enabled"
