# Common DNS Record Types

1. **A (Address) Record**

   - Maps a domain name to an IPv4 address
   - Example: `example.com. IN A 192.0.2.1`

2. **AAAA (Quad-A) Record**

   - Maps a domain name to an IPv6 address
   - Example: `example.com. IN AAAA 2001:db8::1`

3. **CNAME (Canonical Name) Record**

   - Creates an alias for another domain name
   - Example: `www.example.com. IN CNAME example.com.`

4. **MX (Mail Exchanger) Record**

   - Specifies mail servers responsible for handling email for the domain
   - Example: `example.com. IN MX 10 mail.example.com.`

5. **NS (Name Server) Record**

   - Delegates a DNS zone to use the given authoritative name servers
   - Example: `example.com. IN NS ns1.example.com.`

6. **PTR (Pointer) Record**

   - Used for reverse DNS lookups, maps an IP address to a domain name
   - Example: `1.2.0.192.in-addr.arpa. IN PTR example.com.`

7. **SOA (Start of Authority) Record**

   - Specifies authoritative information about a DNS zone
   - Example: `example.com. IN SOA ns1.example.com. admin.example.com. (
2023050101 ; serial
3600       ; refresh
1800       ; retry
604800     ; expire
86400 )    ; minimum TTL`

8. **TXT (Text) Record**

   - Holds text information for sources outside of the domain
   - Often used for domain verification or SPF records
   - Example: `example.com. IN TXT "v=spf1 include:_spf.example.com ~all"`

9. **SRV (Service) Record**

   - Specifies location of servers for specified services
   - Example: `_sip._tcp.example.com. IN SRV 10 60 5060 sip.example.com.`

10. **CAA (Certification Authority Authorization) Record**

    - Specifies which certificate authorities are allowed to issue certificates for a domain
    - Example: `example.com. IN CAA 0 issue "letsencrypt.org"`

11. **DNSKEY, DS, RRSIG Records**

    - Used for DNSSEC (DNS Security Extensions)

12. **DKIM (DomainKeys Identified Mail) Record**
    - Used for email authentication
    - Example: `selector1._domainkey.example.com. IN TXT "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4..."`

## More background

1. A and AAAA records are the most fundamental, directly mapping domain names to IP addresses.

2. CNAME records are useful for creating aliases, often used for subdomains like 'www'.

3. MX records are crucial for email routing.

4. NS records are essential for delegating authority for a domain or subdomain.

5. TXT records have become increasingly important for various verification processes and security protocols.

6. SRV records are particularly useful for specifying the location of specific services.

7. Newer record types like CAA help enhance security by controlling certificate issuance.
