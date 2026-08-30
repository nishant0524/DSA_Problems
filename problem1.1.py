# Write a function that parses these logs to identify which services are failing repeatedly. 
# Specifically, find all services that have thrown an error status code ($4xx$ or $5xx$) 
# more than once.

def analyze_logs(logs):
    failed_services = set()
    services = set()
    for parts in logs:
        part = parts.split(" | ")
        if int(part[1]) < 400:
            continue 
        if part[2] in services:
            failed_services.add(part[2])
        else:
            services.add(part[2])
        
    return list(failed_services)


logs = [
"2026-06-23T14:30:00 | 500 | AuthService",
"2026-06-23T14:31:00 | 200 | AuthService",
"2026-06-23T14:32:00 | 404 | PaymentService",
"2026-06-23T14:30:00 | 500 | AuthService",
"2026-06-23T14:32:00 | 403 | PaymentService",
"2026-06-23T14:32:00 | 403 | LoginService"
]

print(analyze_logs(logs))

