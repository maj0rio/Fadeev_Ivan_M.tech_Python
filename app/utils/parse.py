# parsing such strings like ‘{ip адрес} {http method} {url} {http status code}’
def parse_log(log_string: str) -> tuple[str]:
    log_parts = log_string.split()
    if len(log_parts) != 4:
        raise ValueError("Что-то пошло не так")
    ip_address, http_method, url, http_status_code = log_parts

    valid_methods = ["GET", "POST", "PUT", "DELETE", "PATCH"]
    valid_status_codes = ["200", "201", "204", "400", "401", "403", "404", "500"]
    if http_method not in valid_methods:
        raise ValueError("Что-то пошло не так")

    if http_status_code not in valid_status_codes:
        raise ValueError("Что-то пошло не так")

    print(ip_address, http_method, url, http_status_code)
    return (ip_address, http_method, url, http_status_code)
