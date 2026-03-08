
dig, nslookup, host


DNS server: resolves hostnames or domains to an IP on internet .. google.com -> DNS server -> IP address 

DNS Enumeration: Gathering dns information about a domain name

### host ____

~ host google.com
IPs (IPv4 or IPv6)
MX server


### to get name servers only (or any other record)
~ host -t RECORD_TYPE google.com
~ host -t ns google.com 
~ host -t mx google.com 
~ host -t a google.com 


### we can also do a reverse lookup 
~ host IP_ADRESS (of domain)
will give us a PTR record that can be used to find the domain name


## nslookup ___
gives address and server with Non-authoritative answer as we get that in host __ command


~ nslookup google.com
 
~ nslookup (press enter and you can set things)
> set type=ns
> google.com
Will give nameserves
> set type=a
> ip.com
will give IPs


## dig ___ (successor though nslookup - no longer considered)
types of records: a, any, cname, ...

~ dig google.com

~ dig google.com -t mx

~ dig google.com -t RECORD_TYPE


Get only important info

~ dig google.com -t ns +short # (only ns)


## to check if a command exists .. 
~ command -v COMMAND
~ command -v dig

~ dig @1.1.1.1 google.com # uses a diff dns server for lookup


~ dig +ttl google.com
~ dig +short google.com

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

An **Autonomous System Number (ASN)** sits at the *inter-network routing layer* of the Internet. It is not directly involved when you type a domain name, but it becomes crucial once traffic leaves your local network and traverses between large networks.

Below is the precise relationship between **domain name → DNS → IP → ASN → routing**.

---

# 1️⃣ High-Level Flow When You Enter a Domain Name

Let’s say you type:

```
www.example.com
```

The sequence is:

1. **DNS resolution** → Domain name → IP address
2. **IP routing decision** → Which network owns that IP?
3. **BGP routing between ASNs** → Path selection across the Internet
4. **Packet forwarding** → Routers deliver packets hop-by-hop

---

# 2️⃣ Domain Name and DNS

A domain name (e.g., `example.com`) is a human-readable label.

The **Domain Name System (DNS)** translates it into an IP address.

Example:

```
www.example.com → 93.184.216.34
```

DNS is handled by:

* Recursive resolvers
* Root servers
* TLD servers
* Authoritative DNS servers

DNS does **not** involve ASNs directly. It only returns an IP address.

---

# 3️⃣ IP Address

An IP address identifies a host on the Internet.

Example:

```
93.184.216.34
```

That IP belongs to an IP prefix (e.g., `93.184.216.0/24`).

IP prefixes are **allocated to organizations**, and those organizations operate within an Autonomous System.

---

# 4️⃣ What is an ASN?

An **Autonomous System (AS)** is:

* A network (or group of IP prefixes)
* Under a single administrative control
* With a defined routing policy

Each AS has a unique number: **ASN (Autonomous System Number)**.

Example:

* Google operates AS15169
* Cloudflare operates AS13335

So an ASN represents a **routing domain on the global Internet**.

---

# 5️⃣ Where ASN Comes Into Play

After DNS gives you the IP address:

1. Your device sends packets toward that IP.
2. Your ISP’s router checks its routing table.
3. If the destination IP is outside your ISP’s network:

   * It forwards traffic to another ASN.
4. Routing between ASNs uses **BGP (Border Gateway Protocol)**.

BGP exchanges:

```
IP Prefix + ASN Path
```

Example BGP route:

```
93.184.216.0/24
AS Path: 3356 15133 15133
```

This tells routers:

* Which AS originates the prefix
* Which ASes the traffic must traverse

---

# 6️⃣ How Everything Connects

Here’s the layered relationship:

| Layer               | Component   | Role                        |
| ------------------- | ----------- | --------------------------- |
| Application         | Domain name | Human-readable identifier   |
| Naming system       | DNS         | Resolves domain → IP        |
| Network addressing  | IP address  | Identifies host             |
| Routing domain      | ASN         | Identifies network operator |
| Interdomain routing | BGP         | Moves traffic between ASNs  |

---

# 7️⃣ Concrete Example End-to-End

Let’s say:

* You are connected via your ISP (AS64500)
* You visit a site hosted on Amazon Web Services

Flow:

1. Browser queries DNS.
2. DNS returns IP: `3.210.15.72`
3. That IP belongs to a prefix announced by AWS (AS16509).
4. Your ISP sees:

   ```
   3.0.0.0/8 → via AS16509
   ```
5. Using BGP, your ISP sends traffic toward AS16509.
6. Packets traverse multiple ASNs until reaching AWS.

---

# 8️⃣ Key Conceptual Separation

* **DNS answers: "What is the IP?"**
* **ASN + BGP answer: "How do I reach that IP?"**

DNS maps names to numbers.
BGP maps networks to paths.

They are separate subsystems.

---

# 9️⃣ Important Clarifications

* A single ASN can own many IP prefixes.
* A single company can operate multiple ASNs.
* A website can use multiple ASNs (CDNs, multi-homing).
* Anycast: Same IP announced by multiple ASNs (e.g., CDNs).

---

# 🔟 Mental Model

Think of it like this:

* Domain name = contact name
* IP address = street address
* ASN = postal organization that owns the neighborhood
* BGP = agreements between postal systems about delivery routes

---

----------------------------------------------------------------------------------------------------------------

