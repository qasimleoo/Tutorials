
# 1. 
### Backend from First Principles

We'll look into the below in depth for a better understanding and perspective

i. A high level understanding
ii. HTTP protocol (Structure, Status codes, headers, caching, http 1, 1.1, 2.0. 3.0, Compression, TLS/SSL)
iii. Routing (params, query params, dynamic, catch all, versioning, deperacactions, grouping, permissions, middlewares)
iv. Serialization & Deserialization (in deiff langauges, json, nesting, native DS - dict, objects, errors, null vals, time zone issues, custom, error handling, data conversion errors, schema, performance, compression, text based, binary formats, )
v. Authentication & Authorization (jwt, auth, oauth, api keys, multi factor, salting, hashing, security, cookies, audits, failed login attempts, edge cases, consistency accross failures, timing attacks, )
vi. Validation and Transformations  (valid dates, phones, DoB, Semantic validations, Type validations, Best practices, Client (UI) and server side (true security) validations, in transformations - type casting, type conversions, Normalization [country codes, lower casing emails], conditional validation, chain validation, error handling client based, invalid json)
vii. Middlewares (what?, use cases, role in a request cycle, chaining, security middlewares, mw that add cors headers, rout protexting to our apps, error handlign mws, compressionn or perfromance middlewares, scalability mws)
viii. Request Context (means metadata that is passed to request services, lifecycle of a request, maintaining states)
ix. Handlers and controllers
x. CRUD Operations (deepdive)
xi. REST Best practices (limiting payload, redacting sensitive fields, openapis, content negotiation, optimizing large requests)
xii. Databases (relational, non-relational, joins, design, indexing, querying optimization, data integrity, ORM, Tradeoffs, DB migrations)
xiii. Business logic layer - BBL  (role, layers of requesting cycle, fall in persentation layer, core business logic, seprations of code, single responsibility, business tools, design best practices, servive layer to presentation layer)
xiv. Caching (need, how differs from DB persistence, client side vs server side, read thru, LRU, FIFO, TTL, manual, levels - [in memory , network distributed, hirarichal comines first 2], large and small cache, redis, cache miss ration)
xv. Transactional emails
xvi. Task querying and scheduling (rate limiting, blocking, crons, task priotitizing)
xvii. Elasticsearch (shards, use cases, indexing, log analytics, comments, querying, relevance, optimziing, boosting, pagination , filtering, kibana, user friendly way, numbering shards, wildcards)
xviii. Error Handling (fail safe, prevention, custom, global, user facing erros, centary, ELK stack)
xix. Config Management (best practices, types - dynamic, static, sensitive, sources of configs, diff between stack files, env vars)
xx. Logging, monitoring and observability (structured vs unstrcutured, avoiding sensitive data, types, tools used in logging, prometheus, grafana, alerts - three pillars of observability - logs, metrics, traces)
xxi. Graceful shutdown (need, use cases, scaling, microservices, signal handle, diff steps - capturing a signal, closing, opening files)
xxii. Security
xxiii. Scaling and performance
xxiv. Concurrency and parallelism
xxv. Object storage and large files
xxvi. Realtime backend systems (ws, server sent events)
xxvii. Testing and code quality (all types, in ci/cd)
xxviii. 12 factor app principles
xxix. OpenAPI standard (swagger, UI, postman, openapi 3.0, api first development)
xxx. Webhooks (use cases, sending notifications, apis vs webhooks, key components, http methods, signature verification, testing webhooks, slack)
xxxi. Devops for backend engineers (core concepts, CI/CD, infrastructure, containers in docker, orchestrating in k8s, ci/cd pipelines, scaling, red-green deployemt, rolling deployment)



# 2. 
## Walk the path of a true backend engineer

Expections
----|---------------------------------
	|		     	|				|
Story and      Implementation  Production
philosphy					  Level Projs
 E


# 3. 
## What is backend, how do they work and why do we need them?

Backend is a computer that is listening for a http, websocket, grpc, etc.. to an open port like 80, 443 .. which a client can access (make requests to send and get the data)


How a request is sent to a http(s) that is configured via a domain name to an aws instace with nginx


`Request (domain) -> DNS resovler -> aws firewall -> instance -> nginx -> locahost`


#### Why do we need backends?
- runtime is server

### Why can't we use just frontend? 
- runtime is browser
- sandbox environments (isolated from OS, limits )
- Security reasons (cors) .. browsers are too secure
- can't call external apis .. unless cors allowed
- databases (server runtime has access to all DBs .. drivers are written to work in env that can handle binary data, persistent data .. things the browsers can't do)
- computing power (FE apps are everywhere .. user might have not heavy computing power to do all compute - that's why we need servers for Backend logic)


# 4.
Benifits of learning BE engineering from first principles

you are asked to fix a bug in backend code .. you don't know anything about BE.. where do you start .. or how do you make a new api .. you are asked to get into any other lang without breaking anything Or anything else like that .. how do you apply exisiting knowledge to make new things .. 

You should start with

i. Seeing the big picture / Filtering things in big picture (isolate things .. routes, databases..)

ii. Faster onboarding (stay clear about basics .. like http working, dbs interactions with apis, don't need read docs, tutorials)

iii. 10x faster in new projects

iv. Syntax Fatigue (from one lang to other .. easily)

v. Choosing the right tool for the right Job

vi. More Employable (become the one who can solve problems easily)