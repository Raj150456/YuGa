import http.server
import ssl
import subprocess
import os

# Generate self-signed SSL cert using PowerShell/OpenSSL or Python if needed
cert_file = "cert.pem"
key_file = "key.pem"

if not os.path.exists(cert_file):
    # Use PowerShell to generate a self-signed certificate and export pem
    ps_cmd = """
    $cert = New-SelfSignedCertificate -DnsName "192.168.29.114", "localhost" -CertStoreLocation "cert:\\CurrentUser\\My"
    $pwd = ConvertTo-SecureString -String "password" -Force -AsPlainText
    Export-PfxCertificate -Cert $cert -FilePath "cert.pfx" -Password $pwd
    """
    subprocess.run(["powershell", "-Command", ps_cmd], capture_output=True)

    # Use python cryptography or openssl if available to write simple pem, or fallback
    # Alternatively we can write a simple ssl server script using Python's ssl context
