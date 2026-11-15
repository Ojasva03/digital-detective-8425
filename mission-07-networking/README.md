# Mission 7 - How computers communicate

> AI-assisted working draft. Commands and tests described as performed were run by the assistant on this computer. Review the explanations and write your final understanding in your own words. Local preparation proceeded while GitHub access was unavailable; the assignment's required push-before-next-mission sequence has not been fulfilled.

## 1. Task / objective
Explain network concepts, test connectivity and DNS, and trace a website request.

## 2. Work completed
Prepared the network table and seven-step website explanation. The first public HTTPS check and DNS lookup were blocked in the sandbox. Retried outside it: HTTPS returned HTTP/2 200, and DNS returned two public addresses for example.com.

## 3. Commands / tools used
- `curl --head --max-time 10 https://example.com`: attempted HTTPS connectivity test.
- `nslookup example.com`: attempted DNS lookup.
- No local network address, Wi-Fi name or resolver address was published.

## 4. My understanding
### Task 7.1 - Network concepts

| Concept | Explanation | Example |
|---|---|---|
| LAN | Connects devices over a limited local area | Home devices connected through a router |
| MAN | Connects sites across a metropolitan area | A city network linking municipal buildings |
| WAN | Connects networks across large distances | A company's offices in different countries |
| DNS | Looks up domain information, including address records | Resolving example.com before a connection |
| Router | Forwards packets between networks | A home router linking the LAN to an ISP |
| Protocol | Agreed rules and message formats for communication | HTTPS for encrypted web requests |
| Packet switching | Splits data into packets that share network links | A page's data crossing several routers |
| Client-server | A client requests a service that a server provides | Browser requesting a page from a web server |

### Task 7.2 - Observation interpretation

The first HTTPS check failed with `curl: (6) Could not resolve host: example.com`, and the first DNS command failed with `Operation not permitted` while creating its socket. After retrying outside the sandbox, the HTTPS request completed with exit status 0 and response HTTP/2 200. The DNS lookup completed with exit status 0 and returned public example.com addresses 104.20.23.154 and 172.66.147.243. These are the example server addresses, not the local computer's address.

An HTTPS check tests whether lookup and the required connection/HTTP exchange can complete. A DNS lookup asks for records associated with a domain; successful output may include A records for IPv4 and AAAA records for IPv6. DNS supplies an address that the client can use to contact a server; DNS itself does not download the page.

### Task 7.3 - Opening a website

1. The user enters a URL into the browser, which acts as the client.
2. If no usable address is cached, the client asks DNS to resolve the server's domain name.
3. The client sends packets toward the selected address through the local network, router and provider network.
4. For a typical HTTPS request using HTTP/1.1 or HTTP/2, the client establishes a TCP connection and a TLS session; HTTP/3 instead uses QUIC over UDP with integrated TLS security.
5. The browser sends an HTTP request to the server using the established secure connection.
6. The server handles the request and returns an HTTP response, such as HTML and references to other resources.
7. The browser parses the response, requests any additional resources and renders the page for the user.

Protocols define how participants format and exchange messages. DNS resolution, network routing, transport and HTTP have different roles in this process.

## 5. Difficulties faced
The first network commands failed inside the sandbox, and an initial retry was interrupted.

## 6. How I resolved them
Retried both commands outside the sandbox and recorded selected actual results. Omitted local network details and resolver metadata.

## 7. Evidence / files
- [Attempted network checks](../evidence/mission-07/network-attempts.txt)

## 8. Commit details
Local commit message: `Explain networking concepts and website communication`.
GitHub push: mission commits published to the public repository on 2026-11-15. Publication occurred after offline preparation; the original per-mission push sequence was not followed.
