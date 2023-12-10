valid_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]

valid_status_codes = [
    "200", "201", "204",
    "400", "401", "403", "404",
    "500"
]


def check_ip(ip_address: str) -> bool:
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit() or not 0 <= int(octet) <= 255 or (octet[0] == '0' and len(octet) > 1):
            return False
    return True


# parsing such strings like ‘{ip адрес} {http method} {url} {http status code}’
def parse_log(log_string: str) -> tuple[str]:
    log_parts = log_string.split()
    if len(log_parts) != 4:
        raise ValueError("Что-то пошло не так")
    ip_address, http_method, uri, http_status_code = log_parts
    if http_method not in valid_methods:
        raise ValueError("Что-то пошло не так")

    if http_status_code not in valid_status_codes:
        raise ValueError("Что-то пошло не так")

    if not check_ip(ip_address):
        raise ValueError("Что-то пошло не так")

    return (ip_address, http_method, uri, http_status_code)
