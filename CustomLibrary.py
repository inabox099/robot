from robot.api.logger import info

import dns.resolver

class CustomLibrary:

    def nsquery(self, domain):
        try:
            answers = dns.resolver.resolve(domain, 'A')
            for answer in answers:
                return answer.to_text()
            
        except dns.resolver.NXDOMAIN:
            info(f"No such domain: {domain}")
            return None
        
        except dns.resolver.NoAnswer:
            info(f"No A record found for domain: {domain}")
            return None
        
        except dns.exception.DNSException as e:
            info(f"Error querying A record for domain {domain}: {e}")
            return None
